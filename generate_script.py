import random
import re

def count_words(text):
    text = text.replace("'", "' ")
    text = re.sub(r'\s*([?!:])', r' \1', text)
    words = text.split()
    return len(words)

# RULE 5: 14 distinct camera movements. Max 5 uses per movement, zero repetition within 10 scenes.
camera_movements = [
    "Steadicam push-in, extreme",
    "Crane shot, brutal descent",
    "Dutch angle, aggressive",
    "Pull back, total reveal",
    "Fast lateral tracking shot",
    "Low angle, power rise",
    "Overhead, plunging",
    "Dolly zoom (Hitchcock)",
    "Orbital arc around the subject",
    "Handheld, intimate close",
    "Oner, continuous tracking",
    "Push-out, final reveal",
    "Extreme macro, financial close-up",
    "Tilt up, monumental final"
]

def get_camera_movement(scene_idx):
    if scene_idx == 0:
        return "steadicam push-in / short orbital arc / dutch angle / low angle / total orbital pull back — five distinct movements, hard cuts between each flash"
    else:
        # Cycle through 14 movements to guarantee no repetition within 10 scenes
        idx = (scene_idx - 1) % 14
        return camera_movements[idx]

colorimetry = "Deep black shadows. Precise, cold gold light. Soft ivory highlights."
crisis_colorimetry = "Deep black shadows. Precise, cold gold light. Deep red collapse accent replacing the gold. Soft ivory highlights."

# RULE 1: Outfits. 54 unique, alternating colors.
outfit_colors = ["midnight blue", "burgundy", "cream", "black", "taupe", "emerald green", "charcoal", "ivory", "ruby red", "slate grey", "sapphire", "camel", "olive", "pearl white", "deep plum"]
outfit_materials = ["silk", "wool", "satin", "tweed", "cashmere", "velvet", "linen", "crepe"]
outfit_styles = ["structured blazer", "tailored suit", "cropped jacket", "long coat", "double-breasted jacket", "asymmetric vest", "trench coat"]

outfits = []
prev_color = ""
for i in range(1, 55):
    # Ensure color doesn't repeat consecutively
    color_options = [c for c in outfit_colors if c != prev_color]
    # To avoid repeating the exact same color visually, we cycle through the palette
    color = color_options[i % len(color_options)]
    material = outfit_materials[i % len(outfit_materials)]
    style = outfit_styles[i % len(outfit_styles)]
    outfits.append(f"Wearing a {color} {material} {style}.")
    prev_color = color

# RULE 4: 54 Coherent Locations + RULE 2 (Narrator Action) + RULE 3 (Props)
# Phase 1: 1-7 (Monopoly)
loc_phase1 = [
    ("Luxurious high-frequency trading floor with curved OLED screens, 2025", "walking between sleek trading desks", "analyzing real-time market graphs on a terminal", "reviewing printed financial contracts"),
    ("Elite financial analyst cabinet with brushed steel walls, 2025", "pointing to a holographic market projection", "sorting through dense investment portfolios", "comparing silicon supply chain reports"),
    ("Modern hyper-scale data center corridor with cold blue LEDs, 2025", "striding down the endless server aisle", "monitoring server rack thermal outputs", "inspecting a fiber-optic cable connection"),
    ("Silicon Valley executive boardroom with a massive smart glass table, 2025", "leaning over the conference table signing documents", "handling a sealed architectural blueprint", "adjusting a multi-screen presentation"),
    ("High-tech venture capital conference room with panoramic displays, 2025", "gesturing toward a glowing 3D processor schematic", "examining a rare 8-inch silicon wafer", "typing on a transparent glass keyboard"),
    ("Ultra-secure Swiss banking vault retrofitted as a private server room, 2025", "unlocking a biometric data cabinet", "inspecting a raw gold bullion next to a server", "verifying encrypted ledger entries"),
    ("High-end minimalist architectural studio overlooking a metropolis, 2025", "sketching on an interactive drafting table", "examining a 3D-printed chip housing prototype", "reviewing structural thermal plans")
]

# Phase 2: 8-18 (Disruption)
loc_phase2 = [
    ("Futuristic R&D laboratory with pristine white concrete surfaces, 2025", "examining a glowing micro-processor prototype", "adjusting an electron microscope lens", "recording data on a glowing tablet"),
    ("Stylized semiconductor fabrication cleanroom bathed in amber light, 2025", "observing automated robotic arms behind glass", "holding a reflective 12-inch silicon wafer", "checking atmospheric purity gauges"),
    ("Marble-clad patent attorney office with smart-glass walls, 2025", "stamping an open legal dossier", "reviewing dense intellectual property documents", "examining a proprietary circuit diagram"),
    ("Silicon Valley penthouse overlooking the tech campus at night, 2025", "standing by the floor-to-ceiling window holding a tablet", "analyzing global tech stock tickers", "pouring a glass of water while reading news"),
    ("Exclusive private jet interior featuring holographic projection tables, 2025", "swiping through holographic data streams", "studying a competitor's chip spec sheet", "monitoring international flight paths"), # REMOVE JET (No aircraft) -> Replaced below
    ("Pristine white tech incubation room with floating magnetic displays, 2025", "interacting with a floating code repository", "adjusting a holographic cooling schematic", "typing on a seamless metallic console"),
    ("Modern Asian villa with integrated smart-home tech and dark wood, 2025", "walking through the zen garden with a smart-pad", "reviewing automated security protocols", "checking environmental control systems"),
    ("Underground quantum computing facility with extreme cooling tubes, 2025", "monitoring the sub-zero temperature gauges", "calibrating a quantum state sensor", "recording anomalous energy spikes"),
    ("Elite tech-billionaire's private library with digital archives, 2025", "scrolling through historical hardware patents", "handling a rare first-edition computing manual", "activating a hidden server rack"),
    ("Sleek corporate server monitoring hub with wall-to-wall graphs, 2025", "pointing at a sudden spike in processing efficiency", "cross-referencing bandwidth optimization charts", "adjusting a physical master control dial"),
    ("Minimalist glass cube office suspended over a manufacturing floor, 2025", "looking down at the automated assembly line", "reviewing production yield statistics", "examining a flawed circuit board under light")
]
# Fix Jet (No aircraft)
loc_phase2[4] = ("Exclusive high-speed magnetic train carriage with private tech suites, 2025", "swiping through holographic data streams", "studying a competitor's chip spec sheet", "monitoring international market speeds")

# Phase 3: 19-36 (Financial Impact)
loc_phase3 = [
    ("Historic desert opera house completely devoid of audience, 2025", "standing center stage facing the empty hall", "adjusting the main spotlight controls", "reviewing an old acoustic blueprint"), # CTA 1 (Sc19)
    ("Luxurious Asian stock exchange VIP viewing gallery, 2025", "watching the turbulent digital trading floor below", "analyzing real-time equity crashes", "coordinating emergency sell-offs on a terminal"),
    ("Governmental crisis response room with massive digital maps, 2025", "leaning on the central command table", "tracking global silicon embargo zones", "reviewing national security supply chain reports"),
    ("Exclusive venture capital private club with dark leather booths, 2025", "sitting at a booth reviewing a startup pitch", "handling a physical gold coin and a chip", "signing a high-stakes investment contract"),
    ("Ultra-luxury superyacht interior retrofitted with a trading floor, 2025", "monitoring offshore server connections", "reviewing maritime satellite uplink data", "analyzing encrypted oceanic data streams"), # Changed to interior, avoid boats if possible but yacht interior is okay? No aircraft/helicopter.
    ("Elite hedge fund manager's office with panoramic city views, 2025", "pacing the floor while dictating trades", "shredding obsolete financial forecasts", "examining a stark red portfolio graph"),
    ("High-end art gallery where classical art meets tech installations, 2025", "observing a server rack displayed as modern art", "adjusting the gallery's climate control", "cataloging a piece of vintage computing hardware"),
    ("Billionaire tech investor's fortified concrete residence, 2025", "walking through the brutalist concrete hallway", "unlocking a biometric security vault", "reviewing private intelligence dossiers"),
    ("Underground data bunker built into a solid granite mountain, 2025", "inspecting the reinforced steel blast doors", "checking the backup diesel generator logs", "monitoring seismic sensor readouts"),
    ("Exclusive rooftop infinity pool area transformed into an outdoor office, 2025", "sitting by the water's edge with a waterproof terminal", "analyzing liquid cooling flow rates", "reviewing thermal dissipation charts"),
    ("Private observatory with a massive telescope and digital star maps, 2025", "aligning a digital sensor array", "comparing cosmological data to neural networks", "calibrating deep-space communication uplinks"),
    ("Sleek underground luxury garage housing autonomous server vehicles, 2025", "inspecting a mobile processing unit", "checking the autonomous navigation logs", "connecting a massive power umbilical"),
    ("Elite private hospital diagnostic center powered by AI, 2025", "reviewing a high-resolution neural scan", "monitoring real-time biometric processing", "calibrating a precise surgical laser"),
    ("Exclusive bespoke tailor shop doubling as a secure meeting room, 2025", "examining a fabric swatch next to a microchip", "measuring a physical server dimension", "reviewing a disguised blueprint"),
    ("High-tech subterranean botanical reserve with artificial sunlight, 2025", "monitoring automated environmental sensors", "recording exotic plant growth data", "adjusting the UV light spectrum"),
    ("Private underground cinema screening complex financial data, 2025", "watching a massive red market crash graph", "adjusting the projection contrast", "taking notes on a glowing pad"),
    ("Sleek modern kitchen in a penthouse used as a makeshift lab, 2025", "examining a processor under the bright island lights", "measuring chemical solvent temperatures", "cleaning a delicate silicon component"),
    ("Exclusive high-altitude cable car station designed for VIPs, 2025", "monitoring the encrypted communication relay", "checking the alpine weather station data", "calibrating the main transmission dish")
]

# Phase 4: 37-54 (Consequences)
loc_phase4 = [
    ("Panoramic industrial loft overlooking a sprawling factory complex, 2025", "standing by the vast window observing the smoke", "reviewing automated manufacturing logs", "measuring a new raw material sample"), # CTA 2 (Sc37)
    ("Futuristic geopolitical think-tank with holographic globes, 2025", "manipulating a glowing 3D map of the world", "tracking international trade blockades", "reviewing strategic resource distributions"),
    ("Massive tech conference amphitheater completely empty, 2025", "standing at the podium testing the microphone", "adjusting the massive LED backdrop", "reviewing the keynote presentation slides"),
    ("Presidential suite in a 5-star hotel converted into a war room, 2025", "striding across the thick carpet with a tablet", "monitoring multiple news broadcasts", "organizing classified financial documents"),
    ("Secret underground gallery housing early computer mainframes, 2025", "walking past towering vintage tape drives", "inspecting a vacuum tube", "cataloging a magnetic core memory board"),
    ("Towering glass penthouse utilizing smart-glass privacy features, 2025", "tapping the glass to turn it opaque", "reviewing stealth corporate acquisition plans", "analyzing encrypted competitor data"),
    ("Experimental quantum server room bathed in absolute zero mist, 2025", "monitoring the extreme cryogenic systems", "checking the superconducting cable connections", "recording quantum coherence times"),
    ("Urban panoramic terrace at twilight with neon reflections, 2025", "leaning on the glass balcony railing", "watching the city's power grid fluctuations", "monitoring localized bandwidth surges"),
    ("Elite subterranean command center with brushed steel consoles, 2025", "standing at the central command nexus", "authorizing a massive data migration", "checking the biometric security logs"),
    ("Luxurious train carriage redesigned as a mobile data fortress, 2025", "walking down the narrow opulent corridor", "monitoring trackside network handoffs", "reviewing the onboard server diagnostics"),
    ("Exclusive private museum displaying the history of silicon, 2025", "examining the very first integrated circuit", "cleaning a protective glass display case", "updating a digital exhibit catalog"),
    ("High-end acoustic testing chamber lined with sound-absorbing foam, 2025", "monitoring server fan noise levels", "recording acoustic resonance frequencies", "calibrating a sensitive omnidirectional microphone"),
    ("Private island command bunker hidden beneath tropical foliage, 2025", "monitoring the underwater fiber-optic cables", "checking the desalination plant power draw", "reviewing satellite cloaking protocols"),
    ("Sleek underground racing garage repurposed for tech startups, 2025", "inspecting a liquid-cooled server rack", "calibrating a high-voltage power inverter", "checking the exhaust ventilation systems"),
    ("Exclusive bespoke jewelry workshop examining microscopic tech, 2025", "using a jeweler's loupe on a micro-processor", "polishing a gold electrical contact", "measuring a microscopic wire gauge"),
    ("High-end recording studio monitoring digital network traffic, 2025", "adjusting the massive analog mixing console", "analyzing a data sonification graph", "checking the isolated power supply lines"),
    ("Minimalist Japanese tea house with embedded tech interfaces, 2025", "kneeling by a smart-table displaying code", "preparing a precise matcha infusion", "reviewing a digital zen garden algorithm"),
    ("Modern glass house entirely isolated in a dense dark pine forest, 2025", "standing in the living room facing the dark woods", "monitoring the perimeter security sensors", "checking the off-grid solar power reserves") # CTA 3 (Sc54)
]

all_locations_data = loc_phase1 + loc_phase2 + loc_phase3 + loc_phase4
# Just to be safe, grab 54 distinct elements. We need 54 from 1 to 54. Scene 0 is separate.
assert len(all_locations_data) == 54

narrations = {
"Sc0": "Un ingénieur fabriqua la puce d'intelligence artificielle cinq fois moins chère que le leader mondial du marché, et pas un seul centre de données ne l'acheta jamais.", # 29
"Sc1": "Les mêmes performances, la même vitesse : trois cent cinquante réponses par seconde sur le modèle d'intelligence artificielle le plus exigeant de la planète, pour six dollars le million.", # 30
"Sc2": "Le géant technologique américain factura trente dollars pour ce même million et contrôla pendant des années la totalité de la facture électrique de l'intelligence artificielle mondiale, sans aucune concurrence.", # 30
"Sc3": "Ce tout nouveau processeur rejeta l'architecture traditionnelle, abandonna les logiciels dominants et modifia profondément la méthode de calcul habituelle utilisée par les cartes graphiques les plus puissantes du monde.", # 30
"Sc4": "Tout reposa sur une décision radicale prise dès le premier jour : détruire absolument toutes les fondations établies par le leader californien et rebâtir une puissante technologie depuis le néant.", # 30
"Sc5": "Chaque fois qu'une intelligence générative répond, un serveur lointain brûle d'énormes quantités d'énergie, consumant des milliards de dollars pour maintenir ces immenses infrastructures numériques mondiales totalement actives.", # 28
"Sc6": "La grande entreprise d'intelligence générative dépensa trois milliards de dollars l'année dernière pour alimenter ses serveurs, une facture monumentale entièrement contrôlée par un seul et grand fournisseur monopolistique.", # 30
"Sc7": "Ce fournisseur exclusif imposa ses propres tarifs sans aucune limite, dictant les conditions du marché mondial et forçant les acheteurs à accepter des marges bénéficiaires absolument colossales et inédites.", # 30
"Sc8": "L'ingénieur visionnaire décida d'attaquer ce problème financier à la racine en rejetant chaque hypothèse technique sur laquelle reposait le monopole absolu du titan technologique depuis une longue décennie.", # 30
"Sc9": "En analysant un processeur moderne, on constata qu'une immense partie de la surface en silicium n'effectuait aucune opération mathématique liée à l'intelligence artificielle en cours de calcul.", # 28
"Sc10": "Chaque entreprise qui recruta cet ingénieur devint un géant technologique mondial, et il abandonna chaque projet avant d'en voir le tout moindre résultat sur le marché mondial.", # 28
"Sc11": "Il conçut la puce qui sauva un empire technologique de la faillite, mais quitta l'entreprise en deux mille quinze, avant qu'un seul processeur n'atteigne un seul marché.", # 30
"Sc12": "Il dirige aujourd'hui sa propre startup à code ouvert depuis exactement quatre ans, soit précisément le moment où, selon son propre historique, il commence à chercher la sortie.", # 29
"Sc13": "Il posa les fondations techniques des immenses processeurs mobiles pour la marque, rendant ces téléphones les appareils portables les plus efficaces et hautement rentables de toute la planète Terre.", # 30
"Sc14": "Puis il rejoignit le constructeur automobile d'Elon Musk pour dessiner le silicium de conduite autonome, avant de repartir soudainement dix-huit mois plus tard vers une aventure technologique particulièrement ambitieuse.", # 30
"Sc15": "Chaque projet qu'il toucha se transforma en grand succès magistral, mais ces triomphes éclatants se concrétisèrent systématiquement après son départ inexpliqué vers de tout nouveaux horizons d'ingénierie globale.", # 29
"Sc16": "Les processeurs classiques suffoquaient sous des systèmes invisibles : des planificateurs complexes et des contrôleurs tentant d'anticiper la prochaine destination des immenses flux de données numériques en transit.", # 28
"Sc17": "L'ingénieur comprit que les mathématiques d'intelligence artificielle suivaient une trajectoire totalement prévisible avant l'allumage du circuit, contrairement à l'imprévisibilité totale de chaque jeu vidéo très classique.", # 30
"Sc18": "La charge de travail s'avérant totalement anticipable, il élimina physiquement tous les contrôleurs de trafic matériels, libérant ainsi un espace précieux pour des composants véritablement dédiés au calcul.", # 28
"Sc19": "Vos stratégies d'accumulation personnelles reposent-elles sur des géants technologiques surévalués qui perdront leur immense monopole mondial dès demain matin ? Suivez le canal pour la prochaine révélation.", # 28
"Sc20": "Un secret inconfortable du leader mondial des puces d'intelligence artificielle : moins de la moitié du processeur vendu effectua réellement le travail de calcul pour lequel il fut fabriqué.", # 30
"Sc21": "Le reste du silicium comprenait des planificateurs, des contrôleurs et gestionnaires de mémoire, conçus pour l'imprévisibilité des jeux vidéo, pas pour la prédiction parfaite de l'intelligence artificielle.", # 29
"Sc22": "Une startup supprima ces composants redondants, transféra l'intelligence vers un logiciel gratuit, et le coût du même travail passa de trente à six dollars par million de requêtes.", # 29
"Sc23": "En retirant les aiguilleurs physiques, la gestion des données bascula vers le logiciel, permettant au compilateur d'orchestrer chaque mouvement d'information avec une précision mathématique redoutable et totalement parfaite.", # 30
"Sc24": "Cette architecture novatrice s'articulait autour de blocs indépendants, refusant le modèle du grand processeur luttant pour ses propres ressources contre d'autres composants sur la carte mère hautement congestionnée.", # 30
"Sc25": "Chaque bloc intégrait cinq cœurs distincts possédant leur propre mémoire locale, fonctionnant sans attendre qu'un composant termine sa tâche, éliminant tous les terribles goulots d'étranglement de l'industrie.", # 30
"Sc26": "Puisque le matériel ne réalisait plus aucune prédiction, la magie ne résidait plus dans le silicium, mais dans un compilateur ouvert et accessible gratuitement à l'ensemble de l'humanité.", # 30
"Sc27": "Ce système alignait trois cent cinquante-deux cœurs sur une seule puce, opérant de façon autonome sans horloge globale, offrant une flexibilité incroyable aux développeurs de systèmes d'intelligence générative.", # 29
"Sc28": "Cependant, une lecture de la fiche technique révélait une faille apparente : le refus catégorique d'utiliser la mémoire ultra-rapide qui rendait les puces traditionnelles plus chères qu'une voiture.", # 30
"Sc29": "L'entreprise opta pour une mémoire standard bon marché, semblable à celle des consoles de jeux, malgré sa bande passante extrêmement faible comparée aux standards de l'industrie actuelle.", # 29
"Sc30": "Le plus grand fabricant de puces d'intelligence artificielle au monde paya vingt milliards de dollars pour faire disparaître un concurrent technologique avant que le marché ne le découvre.", # 29
"Sc31": "Il ne construisit pas une meilleure puce, ne baissa pas les prix : il acheta simplement le silence de l'unique équipe qui menaçait son propre monopole technologique mondial.", # 29
"Sc32": "La startup qui survécut ne vendit pas, et fabrique aujourd'hui la puce qui fait le même travail à cinq fois moindre coût, avec une architecture entièrement libre et gratuite.", # 30
"Sc33": "Cette limitation apparente ne freinait pas le processeur, car l'espace libéré par les anciens planificateurs hébergeait deux cents mégaoctets de mémoire intégrée, compensant largement cette bande passante inférieure.", # 29
"Sc34": "Le logiciel préchargeait exactement les données nécessaires depuis la mémoire lente avant l'exécution du calcul, garantissant que les cœurs ne patientaient jamais devant un flux d'informations interrompu.", # 29
"Sc35": "Néanmoins, les modèles linguistiques massifs pesant des dizaines de gigaoctets exposèrent les limites de ce préchargement, redonnant temporairement l'avantage de performance aux cartes graphiques classiques dotées de mémoires colossales.", # 30
"Sc36": "L'équipe anticipait totalement ce blocage dès l'origine, sachant qu'une entreprise ne déploie jamais une seule puce pour bâtir un centre de données, mais en achète des milliers.", # 30
"Sc37": "Votre portefeuille financier personnel survivra-t-il au vaste effondrement imminent des grands monopoles technologiques mondiaux qui soutiennent vos propres actions boursières ? Suivez le canal pour la toute prochaine révélation.", # 29
"Sc38": "Dès que plusieurs processeurs se connectaient pour gérer un modèle géant, ils gaspillaient d'énormes quantités d'énergie à communiquer entre eux, retardant les opérations mathématiques de l'intelligence artificielle.", # 30
"Sc39": "Le géant monopolistique surmontait ce mur de communication grâce à de puissantes connexions propriétaires ultrarapides, facturant ce réseau exclusif à des prix exorbitants, équivalents aux processeurs de très haute pointe.", # 30
"Sc40": "Un hôpital qui utilise l'intelligence artificielle pour le diagnostic médical ne peut fonctionner avec une puce compatible à neuf sur dix : le dixième peut littéralement coûter une vie.", # 30
"Sc41": "Les dix pour cent d'incompatibilité n'inquiètent pas un développeur indépendant, mais paralysent une banque, un hôpital et tout gouvernement gérant une infrastructure numérique nationale critique à grande échelle.", # 30
"Sc42": "Le géant technologique continua de facturer trente dollars par million alors qu'une puce à six existait : le coût du risque de migration dépassa celui de l'économie réalisée.", # 30
"Sc43": "Certaines entreprises technologiques reliaient leurs machines avec d'immenses commutateurs externes, ajoutant de nombreuses couches de chaleur étouffante, de latence extrême et de complexité totalement inutile dans chaque serveur.", # 29
"Sc44": "La réponse de la startup fut d'une brutalité saisissante : elle intégra un vaste réseau de quatre cents gigabits directement dans le silicium, transformant chaque processeur en routeur autonome.", # 30
"Sc45": "Ce compilateur révolutionnaire qui calculait les mouvements de données internes commença à cartographier chaque flux à travers l'ensemble du réseau matériel avant le premier lancement de la moindre opération.", # 30
"Sc46": "La brèche logicielle inquiercée effrayait les grandes banques mondiales exigeant une sécurité totale pour leurs propres infrastructures informatiques hautement critiques face à de très dangereuses menaces numériques.", # 28 (WAIT let's replace this. Original Sc46 was 30 words. Let's keep original.)
"Sc47": "Le logiciel ouvert manquait d'années d'optimisation face au puissant code dominant, mais cette nature accessible permit à une vaste communauté mondiale d'accélérer son développement de façon spectaculaire.", # 30
"Sc48": "Contrairement à ses exploits passés, le grand ingénieur ne travaillait plus comme architecte salarié pour une autre marque prestigieuse : il portait enfin le prestigieux titre de directeur général.", # 29
"Sc49": "Il construisait pour la première fois son propre futur technologique, défiant ouvertement le géant mondial qui détenait un vaste monopole incontesté sur les infrastructures d'intelligence artificielle de la planète.", # 30
"Sc50": "Trente-deux puces reliées ne se comportèrent plus comme trente-deux composants séparés : elles devinrent un cerveau unifié d'intelligence artificielle capable de traiter des milliards de calculs sans aucun délai.", # 30
"Sc51": "Relier trente-six de ces immenses serveurs suffit à créer un supercalculateur de plus de mille puces, toutes coordonnées par un logiciel gratuit, sans commutateurs externes ni latence supplémentaire.", # 28
"Sc52": "Le géant technologique résolut le problème avec des câbles propriétaires aussi coûteux que les puces elles-mêmes : cette architecture le résolut en gravant le réseau directement dans le silicium.", # 29
"Sc53": "Un puissant modèle linguistique open source tournait brillamment sur cette architecture révolutionnaire, atteignant trois cent cinquante mots par seconde lors de tests vérifiés par la grande communauté des développeurs mondiaux.", # 30
"Sc54": "Vos très grandes stratégies d'accumulation de richesse tiennent-elles compte de la révolution matérielle écrasante qui anéantira les valorisations actuelles ? Suivez le canal pour la prochaine révélation." # 28
}
narrations["Sc46"] = "La brèche logicielle inquiétait toujours les acheteurs institutionnels, car la compatibilité partielle des applications effrayait les grandes banques mondiales exigeant une sécurité totale pour leurs propres infrastructures informatiques hautement critiques." # 30

for i in range(55):
    assert 28 <= count_words(narrations[f"Sc{i}"]) <= 30, f"Word count for scene {i} failed: {count_words(narrations[f'Sc{i}'])} - {narrations[f'Sc{i}']}"

negative_prompt = "no text, no letters, no symbols, no wall carvings, no murals, no wigs, no children, no four actors, no modern elements, no music, no watermarks, no logos, no camera overlays, no technical text, no year numbers, no brand names, no subtitles, no captions, no UI elements, no helicopters, no aircraft"

with open("EP01_TENSTORRENT_FR/DIRECTOR_SCRIPT_FR.txt", "w") as f:
    f.write("SERIES: NODESWIS\n")
    f.write("EPISODE: 1 - La fin du monopole des semi-conducteurs\n")
    f.write("CHANNEL: FR\n")
    f.write("VOICE: @Voice: NarradorFR\n")
    f.write(f"COLORIMETRY: {colorimetry}\n")
    f.write("CHARACTER: @Narrateur\n")
    f.write("FINANCIAL ANGLE: Tech Monopoly and Market Threat\n")
    f.write("NARRATION: EXACTLY 28-30 words FR\n")
    f.write("SCENE 0: brutal scroll-stopper hook — ultra-fast summary of the full series — face fully visible from the first two seconds — lips moving\n\n")

    for i in range(55):
        if i == 0:
            nar = narrations[f"Sc{i}"]
            wc = count_words(nar)
            f.write("SCENE 0 — SCROLL STOPPER — 10 SECONDS\n")
            f.write("OMNI FLASH — Text-to-video 10s — 9:16\n")
            f.write(f"[LOCATION] Modern skyscraper boardroom with panoramic city views, 2025 — {colorimetry}\n")
            f.write("[SUBJECT] @Narrateur : femme blonde, brushing impeccable, traits fins, maquillage luxueux discret, posture de dirigeante internationale, 30-45 ans. Wearing a tailored midnight blue silk suit.\n")
            f.write("[ACTION] ULTRA-FAST COLLAGE — 5 FLASH CUTS IN 10 SECONDS:\n")
            f.write("0.0-2.0s: EXTREME STEADICAM PUSH-IN on @Narrateur's face, lips already moving, gaze rising toward the lens.\n")
            f.write("2.0-4.0s: FLASH CUT — iconic physical detail — hands holding a raw silicon wafer — brutal close-up — short orbital arc around the detail\n")
            f.write("4.0-6.0s: FLASH CUT — most dramatic moment of the series — aggressive dutch angle — maximum contrast\n")
            f.write("6.0-8.0s: FLASH CUT — @Narrateur facing camera in front of the monumental set — human scale vs. monumental scale — low angle power shot\n")
            f.write("8.0-10.0s: total ORBITAL PULL BACK — reveals the full extent — final frame total black\n")
            f.write("Hard brutal cut between each flash — zero fade — pure cinema\n")
            f.write("[CAMERA] steadicam push-in / short orbital arc / dutch angle / low angle / total orbital pull back — five distinct movements, hard cuts between each flash\n")
            f.write("[AUDIO] @Voice: NarradorFR. Zero music.\n")
            f.write(f"[CHANNEL COLORIMETRY] {colorimetry}\n")
            f.write("ARRI Alexa LF. 8K. 35mm anamorphique f/2.8. Motion blur on secondary actors.\n")
            f.write(f'Narrator: "{nar}" ({wc} ✅)\n')
            f.write("Zero text. Zero music. Zero watermarks.\n")
            f.write(f"NEGATIVE: {negative_prompt}\n\n")
        else:
            nar = narrations[f"Sc{i}"]
            wc = count_words(nar)
            col = crisis_colorimetry if i == 5 else colorimetry
            loc, action1, action2, action3 = all_locations_data[i-1]
            outfit = outfits[i-1]
            cam = get_camera_movement(i)

            f.write(f"SCENE {i} — [{loc.split('with')[0].strip().upper()}]\n")
            f.write("OMNI FLASH — Text-to-video 10s — 9:16\n")
            f.write(f"[LOCATION] {loc} — {col}\n")
            f.write(f"[SUBJECT] @Narrateur : femme blonde, brushing impeccable, traits fins, maquillage luxueux discret, posture de dirigeante internationale, 30-45 ans. {outfit}\n")
            f.write(f"[ACTION] @Narrateur lips moving clearly, {action1} the full ten seconds.\n")
            f.write(f"Second actor in continuous physical motion — {action2} — hands moving throughout the ten seconds.\n")
            f.write(f"Third actor in continuous physical motion — {action3} — adjusting or manipulating throughout the ten seconds.\n")
            f.write("All three actors in continuous physical motion the full ten seconds — camera in continuous motion the full ten seconds.\n")
            f.write(f"[CAMERA] {cam}. 10 seconds continuous.\n")
            f.write("[AUDIO] @Voice: NarradorFR. Zero music. Zero effects.\n")
            f.write(f"[CHANNEL COLORIMETRY] {col}\n")
            f.write("ARRI Alexa LF. 8K. 35mm anamorphique f/2.8.\n")
            f.write(f'Narrator: "{nar}" ({wc} ✅)\n')
            f.write("Zero text. Zero music. Zero watermarks.\n")
            f.write(f"NEGATIVE: {negative_prompt}\n\n")

    f.write("===FIN===\n")
