def clean_text(text):
    
    if not text:
        return ""

    text = text.strip()

    text = " ".join(text.split())

    return text