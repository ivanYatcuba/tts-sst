import os

import soundfile as sf
from kokoro import KPipeline
from ukrainian_tts.tts import TTS, Voices, Stress


def do_synthesize(input_file: str, out_dir: str, func):
    with open(input_file, encoding="utf-8") as f:
        i = 1
        os.makedirs(f"tts/{out_dir}", exist_ok=True)
        for line in f:
            print('generating:', line.strip())
            func(line.strip(), f"tts/{out_dir}/{i}.wav")
            i += 1


def synthesize_and_save_ua(text, voice, stress, filename, device="cuda"):
    tts = TTS(device=device)
    with open(filename, mode="wb") as file:
        _, output_text = tts.tts(text, voice, stress, file)
    print("Accented text:", output_text)


def synthesize_and_save_en(text, voice, filename):
    pipeline = KPipeline(lang_code='a')
    generator = pipeline(text, voice=voice)
    for i, (gs, ps, audio) in enumerate(generator):
        print(i, gs, ps)
        sf.write(filename, audio, 24000)


if __name__ == '__main__':
    def ua(input: str, output: str):
        synthesize_and_save_ua(
            input,
            Voices.Oleksa.value,
            Stress.Dictionary.value,
            output
        )


    def en(input: str, output: str):
        synthesize_and_save_en(
            input,
            "af_heart",
            output
        )


    do_synthesize("tts/data_ua.txt", "out_ua", ua)
    do_synthesize("tts/data_en.txt", "out_en", en)
