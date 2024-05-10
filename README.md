# FRAME RECOMPOSTER

Этот инструмент предоставляет возможность разбивки видео на кадры и восстановления видео из кадров.

## Установка

1. Создайте виртуальное окружение Python >=3.10.x

2. Клонируйте репозиторий:

3. Установите зависимости: pip install -r requirements.txt


## Использование

### Разбиение видео на кадры
python frame.py split --video_path /path/to/video.mp4 --output_folder /path/to/output/frames

Где:
- `--video_path` - путь к исходному видеофайлу.
- `--output_folder` - путь к папке, куда будут сохранены кадры.

### Восстановление видео из кадров
python video_processor.py reconstruct --frames_folder /path/to/frames --output_path /path/to/reconstructed_video.mp4 --fps 30
Где:
- `--frames_folder` - путь к папке с кадрами.
- `--output_path` - путь к файлу для сохранения восстановленного видео.
- `--fps` (необязательный) - количество кадров в секунду (по умолчанию 30).

### Использование файлов конфигурации
python frame.py split --config config.ini