# transcribe-video-to-text

## Requisitos

Necesitas tener instalado Python 3.9 e instalar la dependencia de Whisper y PyTube:

    pip install git+https://github.com/openai/whisper.git
    pip install pytube

También necesitas tener instalado `ffmpeg`. Según tu sistema operativo se instala de esta forma:

```bash
# Ubuntu
sudo apt update && sudo apt install ffmpeg
# Arch Linux
sudo pacman -S ffmpeg
#  MacOS con Homebrew (https://brew.sh/)
brew install ffmpeg
# Windows con Chocolatey (https://docs.chocolatey.org/en-us/choco/setup)
choco install ffmpeg
# Windows con Scoop (https://scoop.sh/)
scoop install ffmpeg
```

## Cómo usar la línea de comandos

Necesitas indicar la URL del vídeo de YouTube que quieres transcribir:

```sh
python3 transcript.py -h

python3 transcript.py --video "https://www.youtube.com/watch?v=oHrjAbDanpw"

# también puedes indicar el modelo de IA que usará Whisper
# cuanto más grande, más tardará en descargarlo la primera vez
python3 transcript.py --video "https://www.youtube.com/watch?v=oHrjAbDanpw" --model "large"