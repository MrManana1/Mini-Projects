from googletrans import Translator, LANGUAGES

try:
    # Display available languages
    print("Available languages:")
    for code, language in LANGUAGES.items():
        print(f"{code}: {language}")

    # Take input from the user
    text_to_translate = input("Enter the text to translate: ")
    target_language = input("Enter the language code to translate to (e.g., 'ar' for Arabic): ")
    source_language = input("Enter the language code to translate from (e.g., 'en' for English): ")

    translator = Translator()
    translated = translator.translate(text_to_translate, dest=target_language, src=source_language)

    print(f"Original text ({source_language}): {text_to_translate}")
    print(f"Translated text ({target_language}): {translated.text}")

except Exception as e:
    print(f"An error occurred: {e}")
