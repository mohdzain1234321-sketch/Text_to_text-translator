import asyncio
from googletrans import Translator

async def translate_text(text, src_lang='en', dest_lang='kn'):
    translator = Translator()
    translation = await translator.translate(text, src=src_lang, dest=dest_lang)
    return translation.text

async def main():
    input_text = input("Enter ur text:")
    print("Original:", input_text)

    translated_text = await translate_text(input_text)
    print("Translated:", translated_text)

asyncio.run(main())