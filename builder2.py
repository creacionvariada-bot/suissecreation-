import re

def count_fr_words(text):
    t = re.sub(r"[’']", " ", text)
    t = re.sub(r"[^\w\s]", "", t)
    return len(t.split())

# We will provide a clean function to generate 60 correct sentences programmatically or use a corrected list.
sentences = [
    # 0 - HOOK 1 (MIT)
    "Quatre-vingt-quinze pour cent des projets d'intelligence artificielle génèrent exactement zéro retour sur investissement mesurable, d'après les dernières recherches approfondies menées par l'institut prestigieux américain.", # 27 -> wait, "d'intelligence" is two words. Let's count properly.
]

# A much safer way: I'll write a Python script that takes a list of base sentences, counts them using the EXACT logic, and prints them out so I can adjust them to be exactly 28, 29, or 30 words.
