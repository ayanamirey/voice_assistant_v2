import torch
import sounddevice as sd
import time

language = 'ru'
model_id = 'ru_v3'
sample_rate = 48000
speaker = 'baya'  # aidar, baya, kseniya, xenia, random
put_accent = True
put_yo = True
device = torch.device('cpu')  # cpu или gpu
text = "Добрый день, Санжар, удачной и продуктивной вам работы"
model, _ = torch.hub.load(repo_or_dir='snakers4/silero-models',
                          model='silero_tts',
                          language=language,
                          speaker=model_id)

model.to(device)

audio = model.apply_tts(text=text,
                        speaker=speaker,
                        sample_rate=sample_rate,
                        put_accent=put_accent,
                        put_yo=put_yo)

# Воспроизводим
print(text)

sd.play(audio, sample_rate)
time.sleep(len(audio) / sample_rate)
sd.stop()
