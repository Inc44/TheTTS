from pathlib import Path
import argparse

parser = argparse.ArgumentParser(description="Process some arguments.")
parser.add_argument(
    "--api_key",
    type=str,
    default=None,
    help="Use this flag to use ClosedAI's API",
)
parser.add_argument(
    "--text_file_path",
    type=Path,
    default=Path(__file__).parent / "input",
    help="The path to the text file input (default: ./input)",
)
parser.add_argument(
    "--speech_file_dir",
    type=Path,
    default=Path(__file__).parent / "result",
    help="The directory where speech files will be saved (default: ./result)",
)
parser.add_argument(
    "--speaker_wav",
    type=str,
    default="/home/pc/TheTTS/XTTS-v2/samples/en_sample.wav",
    help="The default speaker WAV file (default: en_sample.wav)",
)
parser.add_argument(
    "--language", type=str, default="en", help="The language code (default: en)"
)
parser.add_argument(
    "--codec", type=str, default="mp3", help="The audio codec to use (default: mp3)"
)

args = parser.parse_args()
args.speech_file_dir.mkdir(exist_ok=True)
with open(args.text_file_path, "r", encoding="utf-8") as file:
    text = file.read()
speech_files = []
for i, portion in enumerate(text.split("\n\n"), start=1):
    speech_file_path = args.speech_file_dir / f"{i}.{args.codec}"
    if args.api_key:
        from openai import OpenAI
        openai = OpenAI(api_key=args.api_key)
        with openai.audio.speech.with_streaming_response.create(
            model="tts-1", voice="alloy", input=portion
        ) as response:
            response.stream_to_file(speech_file_path)
    else:
        import torch
        from TTS.api import TTS

        device = "cuda" if torch.cuda.is_available() else "cpu"
        tts = TTS(
            model_path="/home/pc/TheTTS/XTTS-v2",
            config_path="/home/pc/TheTTS/XTTS-v2/config.json",
            progress_bar=True,
        ).to(device)
        tts.tts_to_file(
            text=portion,
            speaker_wav=args.speaker_wav,
            language=args.language,
            file_path=speech_file_path,
        )
    speech_files.append(speech_file_path)
