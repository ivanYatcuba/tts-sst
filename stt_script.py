import jiwer
import whisper

def do_transcribe(experiment: str, lang: str):
    print(f"---{experiment}---")
    trans = transcribe_audio(f"stt/{experiment}.wav", lang=lang)
    print(trans)
    with open(f"stt/{experiment}.txt", "r", encoding="utf-8") as f:
        print(jiwer.wer(f.read().lower(), trans.lower()))

def transcribe_audio(file_path: str, lang: str, model_size: str = "small") -> str: #large
    model = whisper.load_model(model_size, device='cpu')
    result = model.transcribe(file_path, language=lang)
    return result["text"]

if __name__ == '__main__':
    do_transcribe("trump", "en")
    do_transcribe("zelensky", "uk")
    do_transcribe("jackhammer", "en")