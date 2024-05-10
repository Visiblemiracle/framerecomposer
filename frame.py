import cv2
import os
import argparse

def split_video(video_path, output_folder):
    # Открываем видео файл
    video_capture = cv2.VideoCapture(video_path)
    # Устанавливаем начальное значение счетчика кадров
    frame_count = 0

    # Создаем папку для сохранения кадров
    os.makedirs(output_folder, exist_ok=True)

    # Читаем видео и сохраняем кадры
    while True:
        # Считываем кадр из видео
        success, frame = video_capture.read()
        # Если кадр не считался, значит достигли конца видео
        if not success:
            break
        # Сохраняем кадр в папку
        frame_path = os.path.join(output_folder, f"frame_{frame_count}.jpg")
        cv2.imwrite(frame_path, frame)
        # Увеличиваем счетчик кадров
        frame_count += 1

    # Закрываем видео файл
    video_capture.release()
    print(f"Видео разбито на {frame_count} кадров")

def reconstruct_video(frames_folder, output_path, fps=30):
    # Получаем список кадров
    frames = [f for f in os.listdir(frames_folder) if f.endswith('.jpg')]
    # Сортируем кадры по их номеру
    frames.sort(key=lambda x: int(x.split('_')[1].split('.')[0]))
    # Получаем размер первого кадра для установки размеров видео
    first_frame = cv2.imread(os.path.join(frames_folder, frames[0]))
    frame_height, frame_width, _ = first_frame.shape

    # Создаем объект VideoWriter для записи видео
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

    # Читаем каждый кадр и добавляем его в видео
    for frame_name in frames:
        frame_path = os.path.join(frames_folder, frame_name)
        frame = cv2.imread(frame_path)
        out.write(frame)

    # Закрываем объект VideoWriter
    out.release()
    print(f"Видео восстановлено и сохранено в {output_path}")

def main():
    parser = argparse.ArgumentParser(description="CLI для разбивки видео на кадры и сбора видео из кадров")
    subparsers = parser.add_subparsers(dest="command", help="Доступные команды")

    split_parser = subparsers.add_parser("split", help="Разбить видео на кадры")
    split_parser.add_argument("video_path", type=str, help="Путь к видео файлу")
    split_parser.add_argument("output_folder", type=str, help="Путь к папке для сохранения кадров")

    reconstruct_parser = subparsers.add_parser("reconstruct", help="Собрать видео из кадров")
    reconstruct_parser.add_argument("frames_folder", type=str, help="Путь к папке с кадрами")
    reconstruct_parser.add_argument("output_path", type=str, help="Путь для сохранения восстановленного видео")
    reconstruct_parser.add_argument("--fps", type=int, default=30, help="FPS (количество кадров в секунду) для восстановленного видео")

    args = parser.parse_args()

    if args.command == "split":
        split_video(args.video_path, args.output_folder)
    elif args.command == "reconstruct":
        reconstruct_video(args.frames_folder, args.output_path, args.fps)

if __name__ == "__main__":
    main()