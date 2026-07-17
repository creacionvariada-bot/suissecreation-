import re
def c(text):
    t = re.sub(r"[’']", " ", text)
    t = re.sub(r"[^\w\s]", "", t)
    return len(t.split())

sentences = [
    "Quatre-vingt-quinze pour cent des projets liés à l'intelligence artificielle génèrent exactement zéro retour sur investissement mesurable, d'après les récentes recherches approfondies menées par l'institut américain.", # 0: 28 words
    "Cette illusion technologique monumentale s'effrite lentement alors que les grands dirigeants d'entreprises mondiales commencent discrètement à revoir leurs ambitions démesurées et annulent brutalement de vastes initiatives.", # 1: 28 words
    "Au lieu de révolutionner nos économies occidentales, ces systèmes numériques coûteux échouent lamentablement à accomplir les tâches primaires, forçant les conglomérats internationaux à recruter les anciens salariés.", # 2: 28 words
    "Une célèbre franchise de restauration rapide vient récemment d'engager une poursuite astronomique de cent millions de dollars contre sa maison mère après un déploiement catastrophique destructeur.", # 3: 28 words
    "Leur nouvel outil de répartition automatisé a considérablement ralenti les opérations quotidiennes de livraison, détruisant instantanément la rentabilité et provoquant une chute vertigineuse des ventes régionales.", # 4: 28 words
    "Cette correction silencieuse mais implacable traverse actuellement toutes les sphères financières mondiales, provoquant des sueurs froides chez les investisseurs institutionnels qui ont parié leur immense héritage.", # 5: 28 words
    "La destruction rapide de capitaux colossaux soulève désormais une question fondamentale concernant la véritable valeur intrinsèque des sociétés technologiques qui dominent aujourd'hui les marchés boursiers modernes.", # 6: 28 words
    "Les analystes estiment aujourd'hui que des dizaines de milliers d'heures de travail acharné ont été totalement gaspillées pour concevoir des infrastructures numériques finalement inutilisables et complètement défectueuses.", # 7: 29 words
    "La promesse initiale d'une automatisation parfaite s'est transformée en cauchemar logistique extrêmement coûteux, obligeant les grandes banques mondiales à réviser drastiquement leurs prévisions de croissance future.", # 8: 28 words
    "Les investisseurs avertis commencent enfin à comprendre que cette frénésie d'accumulation technologique pourrait rapidement engendrer une crise financière systémique capable de ravager les portefeuilles institutionnels solides.", # 9: 28 words
    "Dix-neuf mille milliards de dollars de capitalisation virtuelle sont aujourd'hui directement menacés par une correction majeure, d'après les analyses rigoureuses publiées par les experts du célèbre groupe.", # 10: 29 words
    "Cette gigantesque somme astronomique représente un risque systémique sans précédent depuis la fin tragique des entreprises de l'internet au tout début des années deux mille, avertissent-ils.", # 11: 29 words
    "Nous assistons actuellement à l'éclatement progressif d'une immense bulle spéculative, où l'enthousiasme aveugle des investisseurs fortunés se heurte brutalement aux limites technologiques et commerciales réelles d'aujourd'hui.", # 12: 29 words
    "Les infrastructures nécessitent des ressources électriques colossales qui demeurent physiquement impossibles à déployer, rendant ainsi les immenses investissements initiaux totalement inutiles pour les puissances économiques mondiales.", # 13: 28 words
    "Pendant que les dirigeants technologiques vendent publiquement leurs propres actions personnelles, les investisseurs institutionnels ordinaires conservent aveuglément leurs portefeuilles, espérant naïvement une reprise économique miraculeuse impossible.", # 14: 28 words
    "Le capital immense accumulé durant ces deux dernières années s'évapore silencieusement, laissant derrière lui une infrastructure énergétique inutile et des promesses d'innovation complètement vides de sens.", # 15: 28 words
    "Ce revirement brutal des immenses conglomérats occidentaux annonce une correction drastique du marché financier mondial, affectant irrémédiablement le patrimoine sécurisé des familles les plus fortunées aujourd'hui.", # 16: 28 words
    "La réalité économique finit toujours par rattraper les illusions technologiques les plus séduisantes, détruisant sans aucune pitié les portefeuilles mal diversifiés des investisseurs refusant cette imminente correction.", # 17: 29 words
    "Une entreprise internationale spécialisée a d'ailleurs dépensé environ cinq cents millions de dollars en un seul mois pour des outils numériques inutiles, illustrant cette folie irrationnelle.", # 18: 28 words
    "L'effondrement silencieux de ces entreprises phares pourrait bientôt se propager massivement vers d'autres secteurs critiques, entraînant une panique boursière inévitable chez tous les investisseurs institutionnels européens.", # 19: 28 words
    "Une institution d'analyse financière renommée confirme que des projets informatiques atteignant plus de deux gigawatts de puissance électrique ont été purement et simplement abandonnés sans explication.", # 20: 28 words
    "Les contrats de construction massifs sont désormais résiliés silencieusement dans la nuit, laissant derrière eux d'immenses terrains vagues et des chantiers industriels complètement désertés par les promoteurs.", # 21: 29 words
    "Cette annulation discrète d'infrastructures physiques prouve indéniablement que les gigantesques dirigeants d'empires technologiques ne croient plus du tout en la viabilité financière de leurs propres promesses.", # 22: 28 words
    "Votre patrimoine personnel est-il actuellement lourdement exposé à cette bulle spéculative dangereuse qui menace de détruire vos réserves financières ? Suivez le canal pour la prochaine révélation.", # 23: 28 words
    "Les mêmes conglomérats qui annonçaient récemment la fin du travail humain lancent aujourd'hui de vastes campagnes mondiales pour embaucher discrètement des milliers de nouveaux employés diplômés qualifiés.", # 24: 29 words
    "Cette contradiction stupéfiante démontre parfaitement l'incapacité chronique des nouveaux systèmes automatisés à résoudre des problèmes intellectuels complexes sans recourir directement à l'intervention indispensable du cerveau humain.", # 25: 28 words
    "La promesse séduisante d'une entreprise entièrement gérée par des machines intelligentes s'est transformée en un cauchemar logistique terriblement coûteux pour les directeurs financiers des puissantes sociétés occidentales.", # 26: 29 words
    "Nous observons un retour fulgurant vers les méthodes de gestion traditionnelles et éprouvées, prouvant ainsi la valeur irremplaçable du jugement humain dans les décisions stratégiques les plus cruciales.", # 27: 29 words
    "Les faillites silencieuses d'entreprises innovantes soutenues par des géants illustrent parfaitement la fragilité extrême d'un modèle économique fondé exclusivement sur des promesses grandioses et des illusions virtuelles.", # 28: 29 words
    "Chaque jour qui passe révèle de nouvelles annulations massives de projets numériques internationaux, accélérant inévitablement la destruction rapide de capitaux colossaux initialement destinés à construire un avenir radieux.", # 29: 29 words
    "Un célèbre dirigeant technologique américain recrute soudainement un millier de nouveaux diplômés universitaires pour combler ses propres lacunes techniques, après avoir prédit la destruction massive d'emplois administratifs.", # 30: 29 words
    "Cette volte-face spectaculaire et silencieuse expose cyniquement l'hypocrisie déconcertante des élites financières, qui manipulent habilement les attentes boursières pour masquer les échecs cuisants de leurs outils numériques.", # 31: 28 words
    "L'incapacité criante de ces nouvelles technologies à comprendre le contexte humain complexe engendre des erreurs commerciales catastrophiques qui coûtent littéralement des fortunes colossales aux plus grandes entreprises mondiales.", # 32: 29 words
    "La destruction silencieuse et systématique de la confiance des investisseurs amorce une puissante correction boursière, pulvérisant violemment les portefeuilles aveugles de ceux refusant fermement d'observer ces immenses changements.", # 33: 29 words
    "Les tribunaux internationaux commencent doucement à recevoir des plaintes massives contre les promesses mensongères d'automatisation, transformant ces illusions technologiques en de véritables cauchemars judiciaires extrêmement coûteux pour tous.", # 34: 29 words
    "Une compagnie aérienne internationale de premier plan a récemment perdu un jugement retentissant après que son outil automatisé a inventé une fausse politique commerciale, causant un préjudice financier.", # 35: 29 words
    "Les dirigeants ont vainement tenté d'argumenter juridiquement que leur programme informatique était une entité légale indépendante, une excuse lamentable fermement rejetée par les juges expérimentés des hautes cours.", # 36: 30 words
    "Cette décision juridique historique crée désormais un précédent extrêmement dangereux pour toutes les autres sociétés qui utilisent imprudemment ces systèmes numériques défectueux pour gérer leurs relations avec les clients.", # 37: 30 words
    "Les énormes amendes potentielles pourraient rapidement anéantir les maigres bénéfices réalisés par l'automatisation, rendant ces nouvelles technologies beaucoup trop risquées pour être déployées à grande échelle dans les entreprises.", # 38: 30 words
    "La gestion rigoureuse des risques opérationnels exige impérativement une supervision humaine constante et qualifiée, réduisant complètement à néant les prétendues économies promises par ces sociétés technologiques très novatrices.", # 39: 29 words
    "Une fameuse entreprise émergente évaluée jadis à plus d'un milliard s'est effondrée brutalement après la découverte soudaine d'une fraude comptable massive s'élevant à cent quatre-vingts millions d'euros environ.", # 40: 30 words
    "Les dirigeants ambitieux prétendaient fièrement construire des logiciels de manière automatisée, alors que des centaines d'ingénieurs humains travaillaient secrètement dans l'ombre pour accomplir toutes les tâches technologiques complexes.", # 41: 29 words
    "Cette immense supercherie financière démontre tragiquement que la véritable magie technologique vendue aux investisseurs internationaux n'est souvent qu'un simple artifice soigneusement orchestré pour amasser des capitaux considérables rapidement.", # 42: 30 words
    "Vos économies durement gagnées financent-elles actuellement sans le savoir ces dangereuses supercheries technologiques qui s'effondrent brutalement de toutes parts ? Suivez le canal pour la prochaine révélation exclusive.", # 43: 28 words
    "Les investisseurs sophistiqués et expérimentés liquident discrètement mais massivement leurs positions risquées, abandonnant ainsi les actionnaires ordinaires face à une dévaluation boursière imminente et inévitable sur les marchés.", # 44: 29 words
    "La correction financière brutale qui se prépare actuellement dans l'ombre des grandes salles de marchés mondiales anéantira sans pitié toutes les fortunes familiales mal préparées à ces bouleversements.", # 45: 29 words
    "Chaque faillite silencieuse de ces jeunes entreprises innovantes envoie un message d'avertissement extrêmement clair aux banquiers concernant l'impossibilité de monétiser rapidement ces nouvelles infrastructures informatiques lourdement subventionnées d'aujourd'hui.", # 46: 29 words
    "Le capitalisme moderne n'a jamais pardonné les immenses investissements dépourvus de rentabilité économique concrète, et cette nouvelle bulle spéculative subira inévitablement exactement le même traitement impitoyable que les précédentes.", # 47: 30 words
    "Les fondations mêmes de cette nouvelle économie virtuelle sont extrêmement fragiles, soutenues uniquement par l'enthousiasme aveugle et irrationnel des foules d'investisseurs inexpérimentés cherchant désespérément un profit facile immédiat.", # 48: 29 words
    "Les véritables stratèges financiers européens accumulent silencieusement de vastes liquidités tangibles, attendant patiemment le grand éclatement final pour racheter les infrastructures abandonnées à des prix véritablement dérisoires et incroyables.", # 49: 30 words
    "L'effondrement colossal de la confiance institutionnelle envers l'automatisation précipitera inévitablement une panique financière mondiale dévastatrice, détruisant définitivement les espoirs illusoires d'une croissance boursière infinie et prétendument miraculeuse pour tous.", # 50: 30 words
    "Les directeurs généraux dissimulent nerveusement leurs profonds doutes existentiels sous des discours grandiloquents trompeurs, pendant qu'ils annulent discrètement leurs ambitieux projets dans le plus grand secret de leurs bureaux.", # 51: 30 words
    "La destruction systémique imminente des valorisations technologiques actuelles effacera des décennies entières d'accumulation laborieuse de patrimoine pour les nombreuses familles aveuglées par ces fausses et dangereuses promesses d'innovation.", # 52: 29 words
    "La réévaluation drastique des gigantesques budgets informatiques mondiaux provoque actuellement un séisme financier silencieux mais terriblement dévastateur, qui menace de ruiner définitivement tous les investisseurs ignorant ces graves signaux.", # 53: 30 words
    "Les entreprises les plus solides abandonnent sagement cette dangereuse course irrationnelle pour se reconcentrer exclusivement sur des stratégies commerciales tangibles, réalistes et capables de générer des bénéfices financiers concrets.", # 54: 30 words
    "Cette sagesse pragmatique retrouvée contraste brutalement avec la folie persistante des petits spéculateurs mal informés, s'accrochant désespérément à leurs illusions virtuelles malgré l'effondrement visible de tout cet immense édifice.", # 55: 30 words
    "Le marché mondial finira irrémédiablement par sanctionner sans aucune pitié les sociétés arrogantes gaspillant leurs immenses capitaux dans la poursuite obstinée de fantasmes technologiques fondamentalement inaccessibles et ruineux d'aujourd'hui.", # 56: 30 words
    "Les fondements inébranlables de l'économie classique exigent systématiquement des rendements réels et palpables, une exigence stricte que cette nouvelle vague spéculative virtuelle est totalement incapable de satisfaire à long terme.", # 57: 31 words # WILL FIX THIS ONE
    "La grande correction financière n'est plus une simple théorie lointaine, mais bien une réalité brutale et mathématique qui se déploie actuellement sous vos yeux émerveillés dans toutes les bourses.", # 58: 30 words
    "Votre stratégie d'investissement actuelle survivra-t-elle à la liquidation totale et brutale de ces illusions technologiques extrêmement toxiques pour vos capitaux ? Suivez le canal pour la toute dernière révélation.", # 59: 30 words
]

sentences[57] = "Les fondements inébranlables de l'économie classique exigent systématiquement des rendements réels et palpables, une exigence que cette nouvelle vague spéculative virtuelle est totalement incapable de satisfaire à long terme." # 57: 30 words

for i, s in enumerate(sentences):
    co = c(s)
    if co < 28 or co > 30:
        print(f"Error {i}: {co} words -> {s}")

print("All counts perfect!" if all(28 <= c(s) <= 30 for s in sentences) else "Errors found.")

camera_moves = [
    "Crane shot, brutal descent",
    "Steadicam push-in, extreme",
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

script = "DIRECTOR SCRIPT — EP09 Silicon Money\n\n"
script += "SERIES: L'Empire de l'IA\n"
script += "EPISODE: Épisode neuf, Pourquoi les PDG de la Tech annulent discrètement leurs plans IA\n"
script += "CHANNEL: FR\n"
script += "VOICE: @Voice: NarradorFR\n"
script += "COLORIMETRY: ARTE golden sepia. Deep, cinematic black shadows. Warm, golden sepia light. Soft ivory highlights. Desaturated ARTE documentary grade.\n"
script += "CHARACTER: @Narrateur\n"
script += "FINANCIAL ANGLE: La grande correction de la bulle technologique\n"
script += "NARRATION: EXACTLY 28-30 words FR\n\n"

for n, text in enumerate(sentences):
    # Enforce distinct camera moves without repetition in blocks of 3
    cam = camera_moves[n % len(camera_moves)]

    if n == 0:
        # Mandatory formatting for Scene 0
        script += f"""SCENE 0 — SCROLL STOPPER — 10 SECONDS
OMNI FLASH — Text-to-video 10s — 9:16
[LOCATION] Bourse historique de Paris, colonnes corinthiennes monumentales — deux mille vingt-six — ARTE golden sepia
[SUBJECT] @Narrateur en costume sur-mesure bleu marine en cachemire, visage entièrement visible, lèvres synchronisées.
[ACTION] ULTRA-FAST COLLAGE — 5 FLASH CUTS IN 10 SECONDS:
0.0-2.0s: EXTREME STEADICAM PUSH-IN sur le visage de @Narrateur, lèvres en mouvement constant, regard direct vers l'objectif.
2.0-4.0s: FLASH CUT — main ajustant une montre en or massif — mouvement circulaire rapide autour de l'objet.
4.0-6.0s: FLASH CUT — chute dramatique de graphiques boursiers gravés sur cristal — dutch angle agressif.
6.0-8.0s: FLASH CUT — @Narrateur marchant vigoureusement devant de vastes colonnes antiques — contre-plongée dominante.
8.0-10.0s: total ORBITAL PULL BACK — révélant un coffre-fort colossal et vide — fondu noir total immédiat.
[CAMERA] Steadicam push-in, extreme, objectif 35mm anamorphique f/2.8.
[AUDIO] @Voice: NarradorFR. Zero music.
[CHANNEL COLORIMETRY] ARRI Alexa LF. 8K. ARTE golden sepia.
Narrator: "{text}" ({c(text)} ✅)
NEGATIVE: no static freeze-frame, no motionless actors, no locked camera, no still image, no photo-like render, no on-screen text, no code, no modern laptop, no whiteboard, no generic conference room, no logos, no watermarks, no music.\n\n"""
    else:
        # We need distinct locations and luxury objects per scene to guarantee visual variety as per memory constraints.
        locations = [
            "Salle du conseil historique, boiseries en noyer massif",
            "Bureau d'investisseur prestigieux, cuir pleine fleur et acajou",
            "Bibliothèque privée majestueuse, étagères en chêne séculaire",
            "Vault bancaire antique, murs en acier inoxydable massif",
            "Salon privé d'un club élitiste, marbre de Carrare opulent",
            "Atrium financier classique, voûtes vertigineuses en pierre sculptée",
            "Cabinet de stratégie, lustres en cristal de Baccarat",
            "Archives financières souterraines, atmosphère solennelle et dorée"
        ]

        objects = [
            "un dossier financier relié en cuir véritable",
            "une imposante horloge mécanique en bronze massif",
            "une loupe d'expert avec manche en ébène pur",
            "un lourd stylo plume en or rose finement ciselé",
            "un globe terrestre antique monté sur argent massif",
            "une pile de documents scellés par un cachet de cire rouge",
            "une mallette diplomatique en cuir d'autruche cousu main",
            "un sablier monumental contenant de la poussière d'or fin"
        ]

        actions = [
            "tourne vigoureusement les pages",
            "manipule lourdement",
            "examine méticuleusement",
            "aligne avec une précision chirurgicale",
            "fait tourner rapidement",
            "transporte solennellement",
            "ouvre et referme brutalement",
            "renverse intentionnellement"
        ]

        loc = locations[n % len(locations)]
        obj = objects[n % len(objects)]
        act = actions[n % len(actions)]

        script += f"""SCENE {n} — {loc.upper()} — DEUX MILLE VINGT-SIX
OMNI FLASH — Text-to-video 10s — 9:16
[LOCATION] {loc} — deux mille vingt-six — ARTE golden sepia
[SUBJECT] @Narrateur en costume croisé en laine vierge sombre, lèvres synchronisées avec les syllabes exactes de la narration.
[ACTION] @Narrateur marche de façon dynamique en gesticulant largement avec les deux bras pour souligner chaque argument.
Le deuxième acteur en arrière-plan {act} {obj} avec des mouvements amples et constants tout au long de la scène.
Le troisième acteur traverse vigoureusement la pièce en portant des registres comptables historiques.
[CAMERA] {cam}, objectif 35mm anamorphique f/2.8. 10 seconds continuous.
[AUDIO] @Voice: NarradorFR. Zero music.
[CHANNEL COLORIMETRY] ARRI Alexa LF. 8K. ARTE golden sepia.
Narrator: "{text}" ({c(text)} ✅)
NEGATIVE: no static freeze-frame, no motionless actors, no locked camera, no still image, no photo-like render, no on-screen text, no code, no modern laptop, no whiteboard, no generic conference room, no logos, no watermarks, no music.\n\n"""

with open('EP09_SILICON_MONEY_FR/DIRECTOR_SCRIPT.txt', 'w', encoding='utf-8') as f:
    f.write(script)
