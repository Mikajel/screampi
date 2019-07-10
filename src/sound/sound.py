import os

def __record_text_to_mp3(text: str, lang: str='en'):
    """
    Use this if you need a new sound
    Requires Google 'gtts' API library to transform text to speech
    Uses english language by default, can override
    """
    from gtts import gTTS

    tts = gTTS(text=text, lang=lang)
    tts.save("lib/sounds/good.mp3")

def play_sound(sound: str):
    # TODO: sudo apt-get install mpg321
    
    os.system(f"mpg321 lib/sounds/{sound}.mp3")