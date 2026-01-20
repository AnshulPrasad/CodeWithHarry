# For Ubuntu(Linux)

from gtts import gTTS
import tempfile
from os import system, remove

l = ["Anshul", "Harry", "CodeWithHarry"]

for name in l:
    tts = gTTS(f"Shoutout to {name}")
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as f:
        filename = f.name
    tts.save(filename)
    system(f"mpg123 {filename} > /dev/null 2>&1") # run command in terminal and stop terminal logs
    remove(filename)
