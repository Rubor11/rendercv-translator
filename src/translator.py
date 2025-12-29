from deep_translator import GoogleTranslator

def translate_text(text, source_lang, target_lang):
    if not text or not text.strip():
        return text

    try:
        return GoogleTranslator(
            source=source_lang,
            target=target_lang
        ).translate(text)

    except Exception as e:
        print(f"[WARN] Translation failed, keeping original text: {e}")
        return text
