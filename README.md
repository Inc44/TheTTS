# Introduction

This Python script is designed to synthesize speech using state-of-the-art open and closed-source tools. It's implemented in a single file to simplify deployment and usage.

# Features

- **ClosedAI TTS**
- **Coqui TTS**

# Installation

```
git clone https://github.com/Inc44/TheTTS.git
cd TheTTS
conda create --name TheTTS python=3.10.13
conda activate TheTTS
DS_BUILD_TRANSFORMER_INFERENCE=1 pip install deepspeed
pip install openai TTS
sudo apt install git-lfs
git lfs install
git clone https://huggingface.co/coqui/XTTS-v2
cp /home/pc/TheTTS/xtts.py /home/pc/miniconda3/envs/TheTTS/lib/python3.10/site-packages/TTS/tts/models
```

# Usage

## Parameters

- `--api`: Use this flag to enable API usage (default: disabled).
- `--text_file_path`: The path to the text file input (default: ./input).
- `--speech_file_dir`: The directory where speech files will be saved (default:./result).
- `--speaker_wav`: The default speaker WAV file (default: female.wav).
- `--language`: The language code (default: en).
- `--codec`: The audio codec to use (default: mp3).

## Commands

Execute the script from the command line, providing optional parameters if needed:

```bash
conda activate TheTTS
cd TheTTS
python -O thetts.py [options]
```

# License

MIT
