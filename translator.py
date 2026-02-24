from gtts import gTTS
import os
import platform

def text_to_audio():
    print("===== TEXT TO AUDIO CONVERTER =====")

    # Take user input
    text = input("Enter the text you want to convert to audio:\n")

    if not text.strip():
        print("Error: Text cannot be empty!")
        return

    # Language selection
    print("\nSelect Language Code:")
    print("en - English")
    print("hi - Hindi")
    print("es - Spanish")
    print("fr - French")
    print("de - German")

    lang = input("Enter language code (default = en): ").lower()
    if lang == "":
        lang = "en"

    try:
        # Convert text to speech
        tts = gTTS(text=text, lang=lang, slow=False)

        filename = "output_audio.mp3"
        tts.save(filename)

        print(f"\n✅ Audio saved successfully as {filename}")

        # Play automatically based on OS
        system_name = platform.system()

        if system_name == "Windows":
            os.system(f"start {filename}")
        elif system_name == "Darwin":  # Mac
            os.system(f"afplay {filename}")
        elif system_name == "Linux":
            os.system(f"xdg-open {filename}")
        else:
            print("Audio file created. Please open it manually.")

    except Exception as e:
        print("❌ Error:", e)

if __name__ == "__main__":
    text_to_audio()