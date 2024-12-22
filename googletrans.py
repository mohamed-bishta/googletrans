from googletrans import Translator, LANGUAGES  

Translator = Translator()

def translate_text(text, src_lang="auto", dest_lang="en"):
    translation = Translator.translate(text, src=src_lang, dest=dest_lang)  # Fixed typo here
    return translation.text

def display_languages():
    print("\nSupported languages:")
    for code, name in LANGUAGES.items():
        print(f"{code} - {name}")
        
print("Welcome to the Google Translator")
print("===============================")
        
while True:
    display_languages()
    text = input("\nEnter text to translate: ").strip()
    src_lang = input("Enter source language code: ")
    dest_lang = input("Enter destination language code: ").strip()
    
    try:
        translated_text = translate_text(text, src_lang, dest_lang)  # Fixed indentation here
        print(f"\nTranslated text: {translated_text}")
        
    except Exception as e:
        print(f"\nError: {e}")
        
    choice = input("\nDo you want to continue? (y/n): ").strip().lower()
    if choice.lower() != "y":
        break
    
print("\nThank you for using the Google Translator")
# python googole.py
