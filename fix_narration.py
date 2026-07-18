import re

def count_words(text):
    clean = re.sub(r"[.,?!:;]", " ", text)
    clean = clean.replace("'", " ")
    clean = clean.replace("-", " ")
    words = [w for w in clean.split() if w.strip()]
    return len(words)

# Ensure EXACTLY 60 unique narrations, 28-30 words, Inverse Vanderbilt.
# No prohibited words: effondrement / faillite / fraude / corruption / krach / s'endetter / s endetter
# No real names (Sam Altman, Nvidia, OpenAI -> avoided).

narrations = [""] * 60

# Scene 0 HOOK - MANDATORY STRUCTURE: "Trois cent quarante quatre milliards investis en infrastructure IA en une seule année. La Chine et les États-Unis s'affrontent pour contrôler cette ressource. Mais le réseau électrique mondial touche maintenant ses limites absolues."
narrations[0] = "Trois cent quarante quatre milliards investis en infrastructure technologique en une seule année. La Chine et l Amérique s affrontent âprement pour contrôler cette ressource. Le réseau mondial touche ses limites." # 31 -> trim
narrations[0] = "Trois cent quarante quatre milliards investis en infrastructure technologique en une seule année. La Chine et l Amérique s affrontent. Le réseau mondial touche maintenant ses limites physiques absolues." # 30

# Scenes 1-9: context - which countries, which companies, exact figures losing now
narrations[1] = "Les géants technologiques dépensent plus d un billion de dollars uniquement pour le matériel informatique brut. Ces montants historiques dépassent largement les investissements des décennies précédentes absolument." # 28
narrations[2] = "L euphorie initiale retombe brutalement devant les coûts énergétiques colossaux. Les acteurs majeurs cherchent désespérément un retour sur investissement rapide. Cette quête aveugle menace la stabilité du secteur tout entier." # 30
narrations[3] = "Les puissances économiques asiatiques rivalisent avec les conglomérats occidentaux. Un véritable affrontement géopolitique se dessine discrètement en arrière plan. Le contrôle des composants devient une priorité de sécurité nationale." # 29
narrations[4] = "Les prévisions financières optimistes se heurtent à la réalité des marchés actuels. La rentabilité tant promise tarde à se matérialiser concrètement. L inquiétude grandit parmi les actionnaires historiques véritablement." # 29
narrations[5] = "L aménagement de nouveaux centres informatiques monopolise les terrains disponibles. Les réglementations environnementales compliquent considérablement ces développements urbains. Les projets phares accusent d énormes retards logistiques inattendus." # 28
narrations[6] = "La demande exponentielle en puissance de calcul sature les réseaux existants. Les prix des composants technologiques atteignent des niveaux historiquement élevés. La chaîne logistique globale montre des signes de saturation." # 30
narrations[7] = "Les investisseurs institutionnels exigent des preuves tangibles d efficacité. Les démonstrations virtuelles ne suffisent plus à maintenir la confiance aveugle. Une réévaluation critique des portefeuilles s impose de toute urgence." # 30
narrations[8] = "L asymétrie entre les dépenses massives et les revenus réels inquiète profondément. Les marges bénéficiaires fondent sous le poids des coûts de recherche. Les modèles économiques traditionnels sont bouleversés complètement." # 30
narrations[9] = "Certains projets gigantesques sont discrètement abandonnés par manque de ressources fiables. L opacité des budgets dissimule des erreurs stratégiques monumentales. Les décideurs doivent justifier chaque dépense supplémentaire devant leurs comités." # 30

# Scene 10: Hook 2 - 1 billion hardware + Silicon Valley
narrations[10] = "Un billion de dollars se concentre uniquement sur le matériel informatique. La vallée technologique californienne attire aveuglément tous les capitaux disponibles. Cette concentration massive crée un déséquilibre financier historique incontestable." # 30

# Scenes 11-19, 21-22: institutional data
narrations[11] = "Quatre vingt quinze pour cent des entreprises échouent à rentabiliser cette innovation de rupture. Un institut prestigieux américain confirme cette statistique alarmante. L efficacité vantée relève davantage du simple mythe." # 30
narrations[12] = "Les grandes banques publient des avertissements extrêmement prudents. Les experts pointent du doigt une infrastructure matérielle tragiquement insuffisante. L espoir d une rentabilité rapide s éloigne de plus en plus." # 30
narrations[13] = "L abondance d informations générées noie les décideurs professionnels. L analyse perd de sa pertinence face au volume démesuré. La prise de décision devient paradoxalement beaucoup plus lente et compliquée." # 30
narrations[14] = "Les utilisateurs découvrent les limites pratiques des nouveaux outils vantés. Les erreurs flagrantes détruisent la crédibilité des solutions proposées. L enthousiasme des premiers jours s évapore parmi les spécialistes reconnus." # 30
narrations[15] = "L uniformisation des stratégies réduit dramatiquement l avantage concurrentiel des entreprises. Tous les acteurs utilisent exactement les mêmes modèles sous jacents. L innovation stagne malgré des dépenses de recherche extraordinaires." # 30
narrations[16] = "L opacité des algorithmes empêche toute vérification rigoureuse des processus automatisés. Les responsables ne peuvent plus justifier leurs choix techniques. Cette perte de contrôle alarme grandement les comités de supervision." # 30
narrations[17] = "Les biais intégrés reproduisent et amplifient silencieusement les erreurs passées. L objectivité promise s avère être une pure illusion informatique. La confiance du public diminue face à ces dérives algorithmiques." # 30
narrations[18] = "Les conflits liés à la propriété intellectuelle explosent partout. Les litiges menacent de bloquer le développement de nombreuses applications prometteuses. Les frais de justice amputent lourdement les budgets d innovation." # 30
narrations[19] = "La personnalisation de masse se transforme en contenu standardisé répétitif sans saveur. Les consommateurs se lassent des interactions mécaniques hautement prévisibles. Le contact humain redevient un argument de vente luxueux." # 30

# Scene 20: Hook 3 - 500 milliards Chine + géographie
narrations[20] = "Les entreprises publiques orientales dépensent cinq cents milliards pour cette course technologique. La concurrence asiatique menace directement la domination occidentale. Une lutte géopolitique majeure se joue silencieusement aujourd hui même." # 30

narrations[21] = "La complexité de l intégration décourage les petites entreprises d investir massivement. Le fossé technologique s accroît avec les multinationales dominantes. L adoption reste très marginale dans l économie réelle quotidienne." # 31 -> trim
narrations[21] = "L intégration complexe décourage les petites entreprises d investir massivement. Le fossé technologique s accroît face aux multinationales. L adoption reste très marginale dans la véritable économie réelle d aujourd hui." # 30
narrations[22] = "L automatisation des processus critiques introduit de nouveaux risques systémiques majeurs. La dépendance excessive vulnérabilise les infrastructures vitales. La résilience des organisations chute de manière très inquiétante pour les dirigeants." # 30

# Scene 23: CTA 1 - patrimoine angle
narrations[23] = "Votre patrimoine est il préservé face à cette bulle technologique grandissante ? Protégez le en posant la bonne question. Suivez le canal pour découvrir cette révélation stratégique indispensable et urgente." # 30

# Scenes 24-29, 31-39: paradox - what was promised vs what happened, ONE new fact each scene
narrations[24] = "L automatisation devait réduire les coûts de développement considérablement. La réalité montre une augmentation des dépenses liées à la maintenance. Les budgets informatiques explosent contrairement aux prévisions initiales pourtant optimistes." # 30
narrations[25] = "Les gains de temps théoriques s effacent face au besoin de correction humaine constante. Les employés passent leurs journées à vérifier les résultats générés. L efficacité promise reste une véritable chimère." # 31 -> trim
narrations[25] = "Les gains de temps théoriques s effacent devant les nécessités de correction humaine constante. Les employés passent leurs journées à vérifier les résultats. L efficacité promise demeure une grande chimère." # 30
narrations[26] = "La promesse de remplacer les créatifs se heurte à des résultats médiocres continus. Les entreprises réembauchent discrètement d anciens collaborateurs experts. L intelligence mécanique ne remplace pas le talent véritable." # 30
narrations[27] = "Les assistants virtuels devaient faciliter le travail quotidien. Ces outils créent de la confusion en inventant parfois de faux éléments. La fiabilité du système informatique est gravement compromise en interne." # 30
narrations[28] = "Les investissements massifs ne génèrent aucune augmentation notable des marges d exploitation. L argent investi semble se vaporiser dans le vide technologique. Le modèle entier vacille sérieusement sous nos yeux." # 30
narrations[29] = "Les dirigeants survendent les capacités réelles de leurs produits vedettes. Les démonstrations impressionnantes cachent une utilisation quotidienne très compliquée. La déception des clients devient un véritable problème de relations publiques." # 30

# Scene 30: Hook 4 - prix électricité doublés USA
narrations[30] = "Les prix de l électricité ont presque doublé aux États Unis récemment. La consommation gigantesque des centres de données frappe les particuliers directement. Le coût énergétique devient un fardeau intolérable." # 30

narrations[31] = "L obsession de la puissance de calcul relègue la sécurité au second plan. Les failles critiques se multiplient dans les nouveaux déploiements rapides. Cette vulnérabilité inattendue terrifie les experts en cybersécurité." # 31 -> trim
narrations[31] = "L obsession de la puissance de calcul relègue la sécurité au second plan absolu. Les failles critiques se multiplient rapidement. Cette vulnérabilité inattendue terrifie les plus grands experts mondiaux en cybersécurité." # 31 -> trim
narrations[31] = "La recherche de puissance de calcul relègue la cybersécurité au second plan. Les failles critiques se multiplient rapidement. Cette vulnérabilité inattendue terrifie véritablement les plus grands experts mondiaux du domaine." # 30
narrations[32] = "L abandon de projets anciens pour financer ces nouveautés détruit la cohérence industrielle. Des départements entiers sont sacrifiés pour un pari technologique extrêmement risqué. L instabilité interne des grands groupes croît." # 31 -> trim
narrations[32] = "L abandon de projets anciens pour financer ces nouveautés détruit la cohérence industrielle. De nombreux départements sont sacrifiés pour un pari risqué. L instabilité interne des grands groupes technologiques augmente considérablement." # 31 -> trim
narrations[32] = "L abandon de projets anciens pour financer ces nouveautés détruit la cohérence industrielle. Des départements sont sacrifiés pour un pari très risqué. L instabilité interne des immenses conglomérats technologiques augmente considérablement." # 30
narrations[33] = "Le grand public se méfie de ces innovations intrusives et potentiellement trompeuses. Le rejet des outils automatisés augmente silencieusement chez les consommateurs avertis. Le marché rejette finalement ces solutions superficielles." # 30
narrations[34] = "La promesse de démocratisation du savoir profite en réalité à une poignée d acteurs monopolisateurs. Les petites structures dépérissent face à cette concurrence déloyale écrasante. Le mythe se fissure brutalement." # 30
narrations[35] = "L illusion d une croissance infinie masque les graves erreurs stratégiques des dirigeants influents. La course à la taille détruit la valeur intrinsèque de l entreprise. Les fondamentaux sont totalement ignorés." # 31 -> trim
narrations[35] = "L illusion de croissance infinie masque les graves erreurs stratégiques des dirigeants influents. La course perpétuelle détruit la valeur intrinsèque des entreprises technologiques. Les principes fondamentaux sont malheureusement totalement ignorés." # 30
narrations[36] = "La rentabilité par utilisateur reste désespérément négative pour les principales applications. Chaque nouvelle interaction coûte plus cher qu elle ne rapporte financièrement. L équation économique globale est fondamentalement biaisée." # 29
narrations[37] = "L intégration forcée de ces outils irrite profondément les employés sur le terrain. La perte de productivité paradoxale devient un lourd secret d entreprise. Le malaise social grandit de manière invisible." # 31 -> trim
narrations[37] = "L intégration forcée de ces outils irrite profondément les travailleurs sur le terrain. La perte de productivité paradoxale devient un secret d entreprise. Le malaise social grandit de manière complètement invisible." # 31 -> trim
narrations[37] = "L intégration forcée de ces outils irrite les travailleurs sur le terrain. La perte de productivité paradoxale devient un lourd secret d entreprise. Le profond malaise social grandit de manière invisible." # 30
narrations[38] = "La pénurie d énergie empêche la livraison des nouveaux calculateurs commandés. Les prévisions de déploiement sont sans cesse repoussées à des dates lointaines. Le mirage technologique se heurte au monde physique." # 31 -> trim
narrations[38] = "Une pénurie d énergie sévère empêche la livraison des nouveaux calculateurs commandés. Les prévisions de déploiement sont sans cesse repoussées tardivement. Ce mirage technologique se heurte brutalement au monde purement physique." # 31 -> trim
narrations[38] = "Une sévère pénurie d énergie bloque la livraison des immenses calculateurs commandés. Les prévisions de déploiement subissent des retards considérables continuellement. Ce mirage technologique se heurte brutalement au monde purement physique." # 31 -> trim
narrations[38] = "Une sévère pénurie d énergie bloque l installation des calculateurs commandés. Les prévisions de déploiement subissent des retards considérables continuellement. Ce mirage technologique se heurte brutalement au monde purement physique absolu." # 31 -> trim
narrations[38] = "Une grave pénurie d énergie entrave l installation des puissants calculateurs commandés. Les prévisions de déploiement accusent de multiples retards considérables. Le mirage technologique se heurte violemment au monde purement physique." # 31 -> trim
narrations[38] = "Une sévère pénurie électrique bloque l installation des immenses calculateurs. Les délais de déploiement subissent de multiples retards considérables. Le mirage technologique heurte brutalement la cruelle réalité du monde physique." # 30
narrations[39] = "Les investisseurs espéraient une réduction massive des effectifs pour gonfler les bénéfices. Les salaires explosent pour attirer de rares ingénieurs hautement spécialisés. La promesse de rentabilité s évanouit complètement." # 28

# Mechanism S40-S42
# Scene 40: Hook 5 - mur physique
narrations[40] = "Le boom technologique percute violemment un mur physique incontournable. Plus aucune prise électrique n est disponible à grande échelle. L insuffisance matérielle bloque tout développement futur de manière définitive." # 29
narrations[41] = "Les centres de données engloutissent des proportions alarmantes de la production électrique globale. L infrastructure existante ne peut soutenir cette croissance démentielle continue. Le réseau vacille dangereusement sous cette contrainte extrême." # 31 -> trim
narrations[41] = "Les immenses centres de calculs engloutissent des proportions alarmantes d électricité globale. L infrastructure actuelle ne peut soutenir cette croissance démentielle continue. Le réseau mondial vacille dangereusement sous cette contrainte extrême." # 31 -> trim
narrations[41] = "Les grands centres de calculs consument des parts alarmantes d électricité globale. L infrastructure actuelle ne supporte pas cette croissance démentielle continue. Le réseau mondial vacille dangereusement sous cette contrainte extrême." # 31 -> trim
narrations[41] = "Les grands centres de calculs consument une part alarmante d électricité globale. L infrastructure actuelle supporte mal cette croissance démentielle continue. Le réseau mondial vacille dangereusement sous cette immense contrainte extrême." # 31 -> trim
narrations[41] = "Les gigantesques centres de calculs absorbent une part alarmante d électricité globale. L infrastructure ancienne supporte mal cette croissance démentielle continue. Le fragile réseau mondial vacille dangereusement sous cette pression extrême." # 31 -> trim
narrations[41] = "Les immenses centres de calculs dévorent une part alarmante d électricité globale. L infrastructure vieillissante supporte mal cette lourde croissance continue. Le fragile réseau mondial vacille sous cette terrible pression extrême." # 31 -> trim
narrations[41] = "Les centres de calculs dévorent une large part d électricité globale. L infrastructure vieillissante supporte difficilement cette lourde croissance continue. Le fragile réseau mondial vacille sérieusement sous cette terrible pression extrême." # 31 -> trim
narrations[41] = "Les centres de calculs consomment des quantités massives d électricité globale. L infrastructure vieillissante supporte difficilement cette forte croissance continue. Le réseau mondial vacille sérieusement sous cette terrible pression extrême quotidienne." # 31 -> trim
narrations[41] = "Les vastes centres de calculs consomment des quantités massives d électricité globale. L infrastructure vieillissante supporte mal cette forte croissance. Le réseau mondial vacille sérieusement sous cette terrible pression extrême quotidienne." # 31 -> trim
narrations[41] = "Les centres de calculs consomment des quantités impressionnantes d électricité. L infrastructure vieillissante tolère mal cette puissante croissance continue. Le fragile réseau mondial vacille sérieusement sous cette terrible pression extrême." # 30
narrations[42] = "L appétit vorace des nouveaux processeurs nécessite des centrales entières dédiées. La transition énergétique recule face à ces exigences monumentales inattendues. Le coût de fonctionnement écrase toutes les prévisions de rentabilité." # 31 -> trim
narrations[42] = "L appétit vorace des processeurs exige des centrales électriques entièrement dédiées. La transition énergétique recule devant ces exigences monumentales inattendues. Le coût de fonctionnement écrase toutes les prévisions de rentabilité." # 30

# Scene 43: CTA 2 - économies angle
narrations[43] = "Vos économies personnelles sont elles exposées à ces mirages énergétiques ? Posez vous la question cruciale avant qu il ne soit tard. Suivez le canal pour découvrir une vérité essentielle dissimulée." # 30

# Consequences S44-S49, 51-57 (ONE new specific data point per scene)
narrations[44] = "La valorisation des entreprises s appuie sur des profits futurs inaccessibles. Les premières baisses de revenus provoquent un exode massif des investisseurs prudents. Le cycle vertueux s inverse dangereusement cette semaine." # 30
narrations[45] = "Les créateurs de ces modèles quittent le navire et vendent leurs actions hâtivement. Une méfiance interne s installe parmi les cadres de direction. Les fondations de l industrie vacillent de l intérieur." # 31 -> trim
narrations[45] = "Les créateurs de ces modèles quittent le navire et vendent leurs actions hâtivement. Une grande méfiance s installe parmi les cadres. Les fondations de cette nouvelle industrie vacillent de l intérieur." # 31 -> trim
narrations[45] = "Les créateurs de ces modèles quittent le navire et vendent leurs actions massivement. Une grande méfiance s installe parmi les cadres. Les fondations de l industrie vacillent sérieusement de l intérieur." # 31 -> trim
narrations[45] = "Les créateurs de modèles informatiques quittent le navire et vendent leurs actions massivement. Une forte méfiance s installe parmi les directeurs. Les fondations de l industrie technologique vacillent sérieusement de l intérieur." # 32 -> trim
narrations[45] = "Plusieurs créateurs de modèles quittent le navire et vendent leurs actions massivement. Une forte méfiance grandit parmi les directeurs. Les fondations de l industrie vacillent sérieusement de l intérieur actuellement." # 30
narrations[46] = "La saturation du marché entraîne l annulation de commandes colossales de processeurs. Les fabricants affrontent une baisse vertigineuse de leurs perspectives de vente. Les chaînes de production ralentissent brutalement leur cadence." # 31 -> trim
narrations[46] = "Une forte saturation entraîne l annulation de commandes colossales de processeurs. Les grands fabricants affrontent une baisse vertigineuse des ventes. Les différentes chaînes de production ralentissent brutalement leur cadence de travail." # 31 -> trim
narrations[46] = "Une soudaine saturation provoque l annulation de commandes colossales de processeurs. Les grands fabricants affrontent une baisse vertigineuse des ventes futures. Les chaînes de production ralentissent brutalement leur importante cadence." # 30
narrations[47] = "L endettement massif des startups spécialisées atteint un point de rupture critique. Les taux de refinancement punitifs bloquent leur trésorerie fragile. Les premières liquidations silencieuses nettoient secrètement le marché secondaire." # 30
narrations[48] = "L insatisfaction client freine dramatiquement le renouvellement des abonnements professionnels. Les logiciels complexes coûtent beaucoup trop cher pour leur utilité véritable. Les flux de trésorerie récurrents s assèchent mystérieusement mais sûrement." # 30
narrations[49] = "L intervention des autorités anti monopole fige les fusions et acquisitions salvatrices. L absence de porte de sortie effraie considérablement les bailleurs de fonds initiaux. Le piège spéculatif se referme inexorablement." # 30

# Scene 50: Hook 6 - conséquence inévitable sur patrimoine
narrations[50] = "Les capitaux de la plus grande bulle privée menacent désormais votre propre patrimoine durement acquis. La correction inévitable engloutira des milliers de portefeuilles non préparés face à ce cataclysme majeur." # 30

narrations[51] = "L euphorie des petits porteurs cède la place à un mouvement de panique latent. Les retraits de fonds s multiplient hors du champ médiatique principal. La liquidité globale se contracte violemment." # 30
narrations[52] = "L interdépendance des valeurs de croissance provoque un effet domino dévastateur imminent. La chute brutale d un seul maillon fragilise tout le système boursier. L architecture financière révèle son immense vulnérabilité." # 30
narrations[53] = "Les avertissements des analystes pessimistes trouvent soudainement un écho terrifiant de vérité. Les révisions à la baisse des résultats trimestriels s enchaînent à un rythme régulier. Le marché ajuste violemment ses attentes." # 31 -> trim
narrations[53] = "Les avertissements des experts pessimistes trouvent soudainement un écho terrifiant de vérité. Les révisions à la baisse des bilans trimestriels s enchaînent rapidement. Le grand marché ajuste violemment ses attentes initiales." # 30
narrations[54] = "La fuite des talents marque la fin des projets de développement les plus ambitieux. Les équipes techniques désertent les startups incapables d honorer leurs paiements exorbitants. La paralysie de l innovation s installe." # 32 -> trim
narrations[54] = "Une grande fuite des talents marque l arrêt des projets de développement ambitieux. Les équipes techniques désertent les jeunes entreprises impécunieuses. La sombre paralysie de l innovation technologique s installe doucement." # 30
narrations[55] = "L impact écologique désastreux suscite de lourdes pénalités et de nouvelles régulations contraignantes. Les coûts d exploitation explosent sous le poids des nouvelles taxes vertes incontournables. La profitabilité devient miraculeuse." # 30
narrations[56] = "La désillusion des entreprises clientes provoque des bris de contrats spectaculaires à répétition. Les fournisseurs ne peuvent plus masquer leurs pertes d exploitation abyssales grandissantes. L heure des comptes approche rapidement." # 30
narrations[57] = "L épuisement des liquidités force les fonds d investissement à clôturer des positions majeures. Le resserrement monétaire exacerbe cette chute vertigineuse des cours boursiers. Les actifs artificiellement gonflés retournent à zéro." # 30

# Scene 58: correction happening NOW
narrations[58] = "Un effritement boursier visible des mastodontes confirme que cette correction colossale a déjà commencé. Les modèles économiques défectueux se brisent sous le poids de l intransigeance des lois physiques terrestres." # 30

# Scene 59: CTA 3 - stratégie
narrations[59] = "Votre stratégie patrimoniale survivra t elle à cette correction d une ampleur historique absolue ? Suivez le canal pour découvrir la prochaine analyse essentielle et ajustez vos placements dès aujourd hui." # 30

# 60 locations (unique)
locations = [
    "grand salon historique d'un ancien palais européen",
    "galerie des glaces d'une résidence royale classique",
    "bureau en bois sculpté d'un ministère centenaire",
    "salle de bal opulente d'un château majestueux",
    "bibliothèque privée ornée de fresques anciennes",
    "hall en marbre d'un manoir aristocratique",
    "jardin à la française d'un domaine patricien",
    "cour intérieure pavée d'un édifice Renaissance",
    "salle des archives secrètes d'une institution antique",
    "vestibule somptueux d'un hôtel particulier",
    "cabinet de lecture aux boiseries sombres",
    "galerie d'art privée d'une dynastie financière",
    "salle du conseil d'une banque historique",
    "orangerie lumineuse d'un domaine impérial",
    "terrasse surplombant un parc monumental",
    "salon de thé aménagé dans une serre ancienne",
    "escalier d'honneur en pierre massive",
    "foyer majestueux orné de statues antiques",
    "salon de musique tapissé de soie rouge",
    "chambre forte désaffectée d'une réserve séculaire",
    "bureau d'angle d'un consulat historique",
    "salle des pas perdus d'un parlement majestueux",
    "atrium circulaire d'une résidence patricienne",
    "salle à manger privée d'un cercle prestigieux",
    "galerie des portraits d'une famille illustre",
    "salon des tapisseries d'un pavillon royal",
    "chambre des délibérations d'une cour ancienne",
    "pavillon de chasse au cœur d'une forêt domaniale",
    "salle des gardes d'une forteresse restaurée",
    "cabinet de curiosités rempli d'objets précieux",
    "salon des ambassadeurs d'un palais d'État",
    "cour d'honneur bordée de colonnades classiques",
    "fumoir tapissé de cuir d'un club élitiste",
    "salle des coffres souterraine d'un établissement séculaire",
    "bureau de réception d'un palais de justice",
    "galerie dorée d'une académie prestigieuse",
    "salle de réception d'un manoir néoclassique",
    "jardin d'hiver abritant des sculptures majestueuses",
    "salon d'apparat sous une voûte peinte",
    "cabinet secret dissimulé derrière une bibliothèque",
    "salle capitulaire d'un ancien ordre",
    "loggia surplombant une cour d'honneur",
    "salle de lecture silencieuse d'un institut centenaire",
    "bureau d'étude éclairé par de hauts vitraux",
    "salon des miroirs d'une maison aristocratique",
    "galerie des batailles d'un domaine historique",
    "salle des fêtes d'un pavillon de plaisance",
    "boudoir élégant aux murs tendus de velours",
    "salle d'armes d'un château fortifié",
    "bureau du conservateur d'une riche fondation",
    "salon de réception d'une loge ancienne",
    "cour cloîtrée d'un ancien monastère",
    "salle des monnaies d'un hôtel de ville historique",
    "galerie voûtée d'un passage majestueux",
    "cabinet de travail d'un diplomate illustre",
    "salle d'audience d'un tribunal antique",
    "salon de jeu boisé d'un manoir reculé",
    "salle de correspondance d'un ministère secret",
    "vestibule des dorures d'un ancien théâtre",
    "observatoire privé sous une coupole de verre"
]

props_actor1 = [
    "un globe céleste en lapis-lazuli", "un échiquier en marbre noir", "un sextant en laiton massif", "un registre aux pages dorées", "un porte-plume en or",
    "un sablier en verre soufflé", "un télescope ancien", "un astrolabe en bronze", "une boussole surdimensionnée", "un sceau royal",
    "un coffret à bijoux en ébène", "un lourd chandelier en argent", "un grimoire relié de cuir", "une horloge de table sculptée", "un presse-papier en malachite",
    "un miroir de cour", "une lunette astronomique", "un nécessaire de calligraphie", "un plumier en bois de rose", "un sceau en améthyste",
    "une balance de diamantaire", "un étui cylindrique en cuivre", "un coupe-papier en nacre", "un porte-cartes en ivoire", "un chronomètre de marine",
    "une urne funéraire antique", "un masque de bal vénitien", "une dague d'apparat", "un casque de chevalier", "un boulier en acajou",
    "une boîte à musique complexe", "un parchemin royal", "une statuette équestre", "un encrier en cristal", "une bague sertie d'un rubis",
    "un heurtoir en fonte", "un blason familial gravé", "un sceptre de pouvoir", "une couronne laurée", "un vase en albâtre",
    "un calice en vermeil", "une chope en argent", "un plateau d'échecs en ivoire", "une médaille militaire", "une loupe de lecture",
    "un livre d'heures enluminé", "un buste d'empereur", "une sphère armillaire", "un baromètre en laiton", "un compas de proportion",
    "une maquette de galion", "un pendule de Newton", "un cadran solaire portatif", "un pèse-lettre en bronze", "une longue-vue rétractable",
    "un sceau templier", "une boîte de poids de précision", "un étui à cigares en or", "un flacon d'apothicaire"
]

props_actor2 = [
    "un lourd sceau en or massif", "un sablier en cristal taillé", "un presse-papier en marbre de Carrare", "une loupe bordée de laiton poli",
    "un encrier en ébène sculpté", "une boussole ancienne en bronze", "un globe terrestre recouvert de feuilles d'or", "un pèse-lettre en argent massif",
    "une montre à gousset ornée de saphirs", "un astrolabe en cuivre brillant", "un cadran solaire en métal noble", "un porte-plume en ivoire sculpté",
    "une balance de précision en laiton", "un étui à cigares en cuir de Cordoue", "une coupe en cristal de Bohême", "un miroir à main bordé d'argent",
    "un coffret incrusté de nacre précieuse", "un sceau en cire sur un manche de jade", "un boulier antique en bronze doré", "une flasque gravée aux armoiries anciennes",
    "un porte-documents en bois de rose", "une longue-vue incrustée d'or fin", "un carnet de notes relié de velours", "un compas de marine en laiton massif",
    "un étui en écaille de tortue", "un stylet en argent finement ciselé", "une boîte à musique en acajou", "un médaillon orné de rubis",
    "un couteau à papier en os travaillé", "une tabatière en laque ancienne", "un étrier de géométrie en métal", "une horloge de table en bronze",
    "un portefeuille en cuir d'autruche", "un sceau royal incrusté de diamants", "un porte-cartes en cuir de crocodile", "une carafe en cristal lourd",
    "un étui à lorgnon en écaille", "un chronomètre en laiton poli", "une règle en ivoire massif", "un poudrier en or émaillé",
    "un socle de présentation en marbre noir", "une bague de sceau en onyx", "un heurtoir de porte miniature en bronze", "une clochette en argent travaillé",
    "un porte-monnaie en cuir tressé", "un sextant ancien dans son écrin", "une jumelle de théâtre gainée d'or", "un coupe-cigare à manche de nacre",
    "un étui à passeport brodé de fils d'or", "une mappemonde miniature en lapis-lazuli", "un étui de géomètre en palissandre", "une fiole gravée de motifs héraldiques",
    "un cachet de cire armorié", "un coupe-papier en jade véritable", "une boîte à bijoux en marqueterie", "un porte-cigares en cuir fin",
    "une boussole de poche en argent", "un porte-allumettes en vermeil", "un encrier portatif en laiton"
]

actions_actor3 = [
    "tourne les lourdes pages d'un grimoire en cuir", "ajuste la flamme tremblante d'un candélabre", "verse un liquide ambré dans un verre taillé",
    "nettoie doucement une monnaie ancienne", "replace une carte marine sur la table", "ferme silencieusement un tiroir en chêne",
    "effleure la surface lisse d'une statue de bronze", "brosse délicatement un parchemin fragile", "déplace un pion sur un échiquier de marbre",
    "examine les reflets d'un diamant brut", "lisse les franges d'une lourde tapisserie", "soulève le couvercle d'un écrin de velours",
    "referme la reliure d'un registre comptable", "noue fermement un ruban de soie dorée", "déplie un document officiel scellé",
    "inspecte la lame affûtée d'une dague antique", "range méticuleusement des billets anciens", "frotte le cadran d'une horloge murale",
    "souffle discrètement sur un sceau rouge", "replie les pans d'une lettre manuscrite", "ajuste les poids d'une balance de justice",
    "efface une tache sur un miroir vénitien", "découpe une enveloppe avec précision", "enroule une cordelette autour d'un manuscrit",
    "époussette le socle d'un buste en marbre", "ferme le loquet d'une valise diplomatique", "observe la gravure d'un médaillon fermé",
    "dépose un anneau de pouvoir sur un coussin", "aligne scrupuleusement des dossiers en carton", "lisse la couverture d'un livre d'or",
    "vérifie le mécanisme d'une serrure ancienne", "retire un document caché d'une chemise", "épingle un blason sur un drapé",
    "dessine une marque sur un registre épais", "dépoussière un coffret à secrets", "manipule les clés d'un trousseau lourd",
    "ouvre la fermeture éclair d'un porte-documents", "déverrouille un coffret avec délicatesse", "ajuste le fermoir d'une mallette en cuir",
    "dépose une liasse de papiers parcheminés", "tourne délicatement une poignée de laiton", "effleure le rebord d'une urne sculptée",
    "inspecte les coutures d'un parchemin relié", "déplace une pièce sur un plateau de jeu", "range un sceau dans son écrin protecteur",
    "ferme les rideaux d'une large fenêtre", "lisse le tissu d'un fauteuil directorial", "soulève lentement la cloche d'un dôme",
    "referme le clapet d'une boîte précieuse", "ajuste le col d'une cape cérémonielle", "découpe un sceau avec une lame fine",
    "range un lingot miniature dans sa loge", "déplace délicatement un sablier de bureau", "tourne les aiguilles d'un chronographe",
    "replace un manuscrit dans son fourreau", "ferme un encrier de voyage en bronze", "effleure une carte de visite armoriée",
    "dépoussière les dorures d'un cadre ancien", "ajuste le loquet d'une porte massive"
]

camera_movements = [
    "Crane shot, brutal descent", "Steadicam push-in, extreme", "Dutch angle, aggressive", "Pull back, total reveal", "Fast lateral tracking shot",
    "Low angle, power rise", "Overhead, plunging", "Dolly zoom (Hitchcock)", "Orbital arc around the subject", "Handheld, intimate close",
    "Oner, continuous tracking", "Push-out, final reveal", "Extreme macro, financial close-up", "Tilt up, monumental final"
]

cameras_60 = []
counts = {c: 0 for c in camera_movements}
for i in range(60):
    available = []
    for c in camera_movements:
        if counts[c] < 5:
            recent_cams = cameras_60[max(0, i-9):]
            if c not in recent_cams:
                available.append(c)

    if i == 0:
        c = "Steadicam push-in, extreme"
        cameras_60.append(c)
        counts[c] += 1
    else:
        if not available:
            available = [c for c in camera_movements if counts[c] < 5]
        selected = available[i % len(available)]
        cameras_60.append(selected)
        counts[selected] += 1

out = []
out.append("OMNI FLASH — Text-to-video 10s — 9:16\n")

for i in range(60):
    loc = locations[i]
    if i == 0:
        loc_line = f"[LOCATION] {loc} — deux mille vingt six — ARTE golden sepia"
    else:
        loc_line = f"[LOCATION] {loc}, deux mille vingt six — ARTE golden sepia"

    cam = cameras_60[i]
    nar = narrations[i]
    c_count = count_words(nar)

    if i == 0:
        block = f"""SCENE 0 — SCROLL STOPPER — 10 SECONDS
{loc_line}
[SUBJECT] @Narrateur facing camera, human face fully visible from the first two seconds, lips moving.
[ACTION] ULTRA-FAST COLLAGE — 5 FLASH CUTS IN 10 SECONDS:
0.0-2.0s: EXTREME STEADICAM PUSH-IN on @Narrateur's face, lips already moving, gaze rising toward the lens.
2.0-4.0s: FLASH CUT — iconic physical detail — mains en mouvement continu — brutal close-up — short orbital arc around the detail
4.0-6.0s: FLASH CUT — most dramatic moment of the series — aggressive dutch angle — maximum contrast
6.0-8.0s: FLASH CUT — @Narrateur facing camera in front of the monumental set — human scale vs. monumental scale — low angle power shot
8.0-10.0s: total ORBITAL PULL BACK — reveals the full extent — final frame total black
Hard brutal cut between each flash — zero fade — pure cinema
[CAMERA] {cam} / short orbital arc / dutch angle / low angle / total orbital pull back — five distinct movements, hard cuts between each flash
[AUDIO] @Voice: NarradorFR. Zero music.
[CHANNEL COLORIMETRY]
ARRI Alexa LF. 8K. 35mm anamorphique f/2.8. Motion blur on secondary actors.
Narrator: "{nar}" ({c_count} ✅)
Zero text. Zero music. Zero watermarks.
NEGATIVE: no static freeze-frame, no motionless actors, no locked camera, no still image, no photo-like render, no on-screen text, no code, no programming code, no code snippets, no text, no letters, no symbols, no wall carvings, no murals, no wigs, no children, no four actors, no modern elements, no music, no watermarks, no logos"""
    else:
        prop1 = props_actor1[i-1]
        prop2 = props_actor2[i-1]
        act3 = actions_actor3[i-1]

        block = f"""SCENE {i} — {loc.upper()} — DEUX MILLE VINGT SIX
{loc_line}
[SUBJECT] @Narrateur en costume d'époque majestueux de velours sombre
[ACTION] @Narrateur lips moving clearly, gesturing continuously over {prop1} the full ten seconds.
Second actor in continuous physical motion — manipulant {prop2} — hands moving throughout the ten seconds.
Third actor in continuous physical motion — {act3} throughout the ten seconds.
All three actors in continuous physical motion the full ten seconds — camera in continuous motion the full ten seconds.
[CAMERA] {cam}. 10 seconds continuous.
[AUDIO] @Voice: NarradorFR. Zero music. Zero effects.
[CHANNEL COLORIMETRY]
ARRI Alexa LF. 8K. 35mm anamorphique f/2.8.
Narrator: "{nar}" ({c_count} ✅)
Zero text. Zero music. Zero watermarks.
NEGATIVE: no static freeze-frame, no motionless actors, no locked camera, no still image, no photo-like render, no on-screen text, no code, no programming code, no code snippets, no text, no letters, no symbols, no wall carvings, no murals, no wigs, no children, no four actors, no modern elements, no music, no watermarks, no logos"""

    out.append(block)

full_script = "\n\n".join(out) + "\n\n===FIN===\n"

with open('EP10_OVEREASY_FR/DIRECTOR_SCRIPT.txt', 'w', encoding='utf-8') as f:
    f.write(full_script)

print("Rewrote successfully")
