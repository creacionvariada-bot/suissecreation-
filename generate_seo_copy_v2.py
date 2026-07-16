import re

def count_words(text):
    clean_text = re.sub(r'[^\w\s]', ' ', text)
    return len(clean_text.split())

def validate():
    fb_title_a = "Quatre-vingt-quinze pour cent de projets IA sans aucun retour sur investissement."
    fb_title_b = "Cent millions de procès : comment l'IA détruit secrètement la stratégie des élites."
    ig_title = "Dix-neuf mille milliards de valorisation IA : la grande correction."

    # Target: 300-400 characters
    fb_cap = "Quatre-vingt-quinze pour cent des projets d'intelligence artificielle en entreprise génèrent exactement zéro retour sur investissement, selon le MIT. Pendant que les PDG annulent leurs centres de données, votre patrimoine reste exposé à cette dangereuse bulle. Suivez le canal pour la prochaine révélation."

    ig_cap_b1 = "Dix-neuf mille milliards de capitaux piégés dans la bulle IA, pendant que les élites fuient."
    ig_cap_b2 = "Votre héritage survivra-t-il à cette correction brutale ? Suivez le canal pour anticiper."
    ig_cap = f"{ig_cap_b1}\n{ig_cap_b2}"

    assert count_words(fb_title_a) <= 14, f"FB Title A too long: {count_words(fb_title_a)}"
    assert count_words(fb_title_b) <= 14, f"FB Title B too long: {count_words(fb_title_b)}"
    assert count_words(ig_title) <= 10, f"IG Title too long: {count_words(ig_title)}"

    assert 300 <= len(fb_cap) <= 400, f"FB caption wrong length: {len(fb_cap)}"
    assert 150 <= len(ig_cap) <= 200, f"IG caption wrong length: {len(ig_cap)}"

    # Write output
    with open('EP09_SILICON_MONEY_FR/SEO_COPY_FINAL.txt', 'w', encoding='utf-8') as f:
        f.write("FILENAME\n")
        f.write("ai-bubble-tech-layoffs-2026.mp4\n")
        f.write("FACEBOOK TITLE A\n")
        f.write(f"{fb_title_a}\n")
        f.write("FACEBOOK TITLE B\n")
        f.write(f"{fb_title_b}\n")
        f.write("INSTAGRAM TITLE\n")
        f.write(f"{ig_title}\n")
        f.write("FACEBOOK CAPTION\n")
        f.write(f"{fb_cap}\n")
        f.write(f"COUNT: {len(fb_cap)} characters ✅\n")
        f.write("FACEBOOK HASHTAGS\n")
        f.write("#Patrimoine #AIBubble #TechLayoffs #DataCenters #AIBubbleCrash\n")
        f.write("INSTAGRAM CAPTION\n")
        f.write(f"{ig_cap_b1}\n")
        f.write(f"{ig_cap_b2}\n")
        f.write(f"COUNT: {len(ig_cap)} characters ✅\n")
        f.write("INSTAGRAM HASHTAGS\n")
        f.write("#Patrimoine #AIBubble #TechLayoffs\n")
        f.write("ALT TEXT\n")
        f.write("Un investisseur observe avec inquiétude l'effondrement des valeurs liées à l'intelligence artificielle.\n")
        f.write("THUMBNAIL\n")
        f.write("LINE 1: KRACH\n")
        f.write("LINE 2: IMMINENT\n")
        f.write("SUBTITLE KEYWORDS\n")
        f.write("KRACH — BULLE — PATRIMOINE — STRATÉGIE — LICENCIEMENTS\n")
        f.write("AFTER EFFECTS\n")
        f.write("SERIES TITLE: L'Empire de l'IA\n")
        f.write("EPISODE NUMBER: Épisode neuf\n")
        f.write("EPISODE TITLE: Pourquoi les PDG de la Tech annulent discrètement leurs plans IA\n")
        f.write("SHORT TITLE: Krach de l'IA\n")
        f.write("LOWER THIRD 1: L'Empire de l'IA\n")
        f.write("LOWER THIRD 2: Ep. 9 — Krach de l'IA\n")
        f.write("OPENING CARD: L'Empire de l'IA | Épisode 9\n")
        f.write("END CARD: Krach de l'IA\n")

if __name__ == '__main__':
    validate()
    print("SEO_COPY_FINAL.txt updated.")
