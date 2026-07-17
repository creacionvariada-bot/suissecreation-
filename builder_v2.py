import re

def count_fr_words(text):
    t = re.sub(r"[’']", " ", text)
    t = re.sub(r"[^\w\s]", "", t)
    return len(t.split())

# 1. Base locations alternating exterior/interior (59 total)
exteriors = [
    "escaliers de palais royaux", "places financières historiques",
    "quais de ports marchands anciens", "jardins de résidences privées",
    "colonnades de banques centrales historiques", "terrasses panoramiques de gratte-ciels classiques",
    "cours intérieures de palais Renaissance", "parvis de cathédrales financières",
    "ponts historiques au lever du jour", "façades de bourses mondiales historiques",
    "parvis d'anciens marchés boursiers", "jardins suspendus de demeures aristocratiques",
    "allées majestueuses de domaines privés", "belvédères dominant d'anciens quartiers d'affaires",
    "quais pavés de comptoirs d'importation", "marches de marbre d'anciennes douanes",
    "terrasses de villas patriciennes", "ponts de pierre enjambant des canaux marchands",
    "cours d'honneur de fondations bancaires", "avenues bordées d'arbres centenaires",
    "places pavées entourées de monuments financiers", "jardins géométriques de manoirs historiques",
    "balcons sculptés dominant le port", "parvis de grands hôtels de la monnaie",
    "esplanades face à d'antiques bourses maritimes", "terrasses empierrées d'anciens palais consulaires",
    "escaliers monumentaux de ministères historiques", "cours d'arcades de vieux palais marchands",
    "jardins d'hiver de demeures bourgeoises", "frontons sculptés d'anciennes résidences de banquiers"
]

interiors = [
    "cryptes de banques souterraines", "ateliers de graveurs de monnaies anciennes",
    "salles des coffres monumentales", "galeries de tableaux financiers",
    "salles de cartographie antique", "laboratoires d'assayeurs d'or",
    "cabinets de notaires historiques", "salles de télégraphe financier",
    "loges de négociants en soieries", "observatoires astronomiques privés",
    "fonderies de métaux précieux", "chambres fortes en granit",
    "salles de pesée de lingots", "ateliers d'horlogerie de précision",
    "galeries souterraines de lingots", "bibliothèques de traités financiers manuscrits",
    "salles de cartographie nautique", "chambres d'imprimerie de billets de banque",
    "archives notariales en parchemin", "salons de négociation diplomatique",
    "bureaux privés lambrissés d'ébène", "salles de tri de pierres précieuses",
    "caves voûtées abritant des réserves d'argent", "salons de réception tendus de velours",
    "cabinets de curiosités d'investisseurs", "salles de lecture de correspondances marchandes",
    "chambres de comptage aux lourdes portes", "ateliers de reliure de registres comptables",
    "galeries d'exposition de joyaux couronnés", "salons d'archives tapissés de cuir repoussé"
]

# Alternate them to get 59 unique ones
locations = []
for i in range(30):
    if i < len(exteriors):
        locations.append(exteriors[i])
    if i < len(interiors) and len(locations) < 59:
        locations.append(interiors[i])

locations = locations[:59]

# 2. 59 Unique Actor 3 actions & props
actor3_actions = [
    "Déplacer des lingots d'or sur un plateau en argent massif",
    "Dérouler lentement une immense carte financière en soie",
    "Peser des pièces d'or sur une balance de précision ancienne",
    "Sceller des enveloppes diplomatiques avec de la cire rouge fondue",
    "Graver des chiffres sur des plaques de cuivre",
    "Tendre des câbles de télégraphe entre deux points",
    "Photographier des documents avec un appareil chambre ancien",
    "Disposer des billets de banque historiques sur une table en acajou",
    "Refermer un coffre-fort monumental à combinaison",
    "Dérouler des parchemins financiers sur une table de lecture",
    "Aligner des pièces de monnaie d'époque sur du velours noir",
    "Transporter une malle en cuir clouté remplie de documents",
    "Vérifier des registres avec une règle en ivoire ancien",
    "Emballer des lingots dans du velours bordeaux",
    "Huiler les rouages d'une horloge monumentale en bronze",
    "Timbrer des documents avec un sceau en or massif",
    "Classer des obligations financières dans des casiers en chêne",
    "Compter des pièces d'or avec des gants blancs de coton",
    "Refermer un livre de comptes relié en maroquin rouge",
    "Déployer un abaque en ébène et ivoire sur la table",
    "Examiner une action historique à la loupe cerclée d'or",
    "Nettoyer un plateau de présentation en argent massif",
    "Aligner des lingots d'argent pur sur un drap de velours",
    "Affûter une plume calligraphique avec un canif en nacre",
    "Trier des diamants bruts avec une pince en or",
    "Consigner des transactions sur un registre aux bords dorés",
    "Manipuler un boulier asiatique en bois de rose",
    "Dépoussiérer un compas de marine en cuivre patiné",
    "Refermer une lourde sacoche diplomatique en crocodile",
    "Verrouiller un tiroir de dépôt avec une clé ciselée",
    "Tamponner des certificats d'action avec un encreur en argent",
    "Peser des émeraudes sur une balance d'apothicaire",
    "Ajuster le balancier d'une horloge astronomique ancienne",
    "Classer des lettres de crédit dans un semainier en ronce de noyer",
    "Examiner une gravure bancaire sous une lampe à pétrole",
    "Sceller une boîte de transport en fer forgé",
    "Tirer les fils de soie d'une reliure notariale",
    "Dépoussiérer des titres de propriété avec un pinceau en poils de martre",
    "Trier des saphirs sur un tapis de cuir vert",
    "Ajuster les poids en cuivre d'une balance à fléau",
    "Ranger des cachets de cire dans un coffret en acajou",
    "Polir un coupe-papier en argent massif",
    "Assembler des contrats sur parchemin véritable",
    "Refermer une urne de vote diplomatique en bronze",
    "Mesurer un lingot d'or avec un pied à coulisse en acier poli",
    "Envelopper des pierres précieuses dans des feuillets de soie",
    "Sceller un tube de transport de documents en laiton",
    "Tourner la manivelle d'un cryptographe mécanique en bois",
    "Ajuster un télescope en cuivre pointé vers le ciel",
    "Classer des plans d'architecture de coffres-forts",
    "Peser de la poudre d'or dans des fioles de verre soufflé",
    "Trier des sceaux royaux dans des loges de velours bleu",
    "Dépoussiérer un globe céleste antique en métal précieux",
    "Ouvrir délicatement un écrin à bijoux en marqueterie",
    "Aiguiser un stylet en ivoire sur une pierre fine",
    "Réorganiser des rouleaux de soie d'importation",
    "Vérifier le filigrane de billets anciens face à la lumière",
    "Fermer une mallette de transport de fonds blindée",
    "Nettoyer l'objectif d'une lunette d'observation maritime"
]

# 3. 59 Unique Actor 2 Props & Actions
actor2_actions_props = [
    "feuillette lentement les pages d'un atlas maritime historique",
    "examine un lourd candélabre en cristal taillé à la main",
    "caresse le revêtement en cuir de Cordoue d'un coffret",
    "manipule un globe terrestre en bronze patiné",
    "ajuste ses boutons de manchette en platine pur",
    "aligne des jetons de comptage en nacre véritable",
    "fait tourner un lourd sablier rempli de poudre d'argent",
    "ouvre une tabatière en ronce de noyer et or",
    "examine un astrolabe en laiton finement ciselé",
    "soulève le couvercle d'une boîte à cigares en ébène massif",
    "trace des lignes avec un compas d'architecte en or",
    "déplace une statuette de taureau en bronze massif",
    "observe le reflet de la lumière sur un diamant monté en bague",
    "referme doucement un livre d'heures aux enluminures d'or",
    "ajuste le fermoir en acier trempé d'une sacoche de coursier",
    "examine les rouages d'une montre de gousset ouverte",
    "manipule un coupe-papier à manche en lapis-lazuli",
    "tourne délicatement une clé monumentale en fer forgé",
    "lisse les bords d'un traité d'alliance sur parchemin",
    "positionne des pièces d'échecs en marbre et albâtre",
    "observe un rubis à travers une lentille en cristal",
    "referme les fermoirs en laiton d'un lourd dossier de cuir",
    "déploie une carte des routes commerciales en toile",
    "ajuste la mèche d'une lampe de bureau en bronze ouvragé",
    "fait glisser une chaîne de gousset en or massif entre ses doigts",
    "aligne des encriers en verre taillé sur son bureau",
    "caresse le bois laqué d'une maquette de navire marchand",
    "examine un sceau diplomatique taillé dans l'ivoire",
    "souffèse une lourde pièce d'or de huit escudos",
    "referme le clapet d'une bourse en velours cramoisi",
    "déplace un étouffoir à bougie en argent ciselé",
    "manipule une longue règle de calcul en palissandre",
    "tourne les pages d'un répertoire des marchés financiers",
    "ajuste le couvercle d'un coffret à thé en marqueterie",
    "observe un lingot d'argent à travers son reflet",
    "referme un carnet de bord aux ferrures de laiton",
    "caresse les maillons d'une gourmette en or gris",
    "déplace un poids de balance en acier poli brillant",
    "examine un télescope portatif recouvert de cuir",
    "manipule un boulier aux tiges d'argent massif",
    "tourne la molette d'un calendrier perpétuel en cuivre",
    "ajuste les aiguilles d'une pendulette de voyage en or",
    "lisse un document officiel orné d'un ruban de soie",
    "fait glisser un sceau en améthyste véritable",
    "observe les graduations d'un pied à coulisse ancien",
    "referme le tiroir d'un meuble de tri en acajou massif",
    "déplace un encrier de voyage en cuir bouilli",
    "manipule un chronomètre de marine dans son coffret en bois",
    "tourne les pages d'un annuaire d'armateurs du siècle passé",
    "ajuste la base d'un baromètre en laiton massif",
    "caresse le manche en ivoire sculpté d'un sceau",
    "déplace un porte-plume en cristal taillé",
    "examine la serrure complexe d'une caisse à obligations",
    "manipule un compas d'épaisseur en acier bleui",
    "tourne délicatement le barillet d'une combinaison de coffre",
    "ajuste la focale d'une longue-vue d'officier de marine",
    "observe les reflets d'une monnaie byzantine ancienne",
    "referme le fermoir d'un lourd cahier de quittances",
    "déplace une statuette symbolisant la bourse en fonte de fer"
]

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

# Read sentences from v4 output or recreate them with the word changes
sentences = [
    "Quatre-vingt-quinze pour cent des projets liés à l'intelligence artificielle génèrent exactement zéro retour sur investissement mesurable, d'après les récentes recherches approfondies menées par l'institut américain.", # 0
    "Cette illusion technologique monumentale s'effrite lentement alors que les grands dirigeants d'entreprises mondiales commencent discrètement à revoir leurs ambitions démesurées et annulent brutalement de vastes initiatives.", # 1
    "Au lieu de révolutionner radicalement nos économies occidentales, ces systèmes numériques coûteux échouent lamentablement à accomplir les tâches primaires, forçant les immenses conglomérats internationaux à recruter les anciens salariés.", # 2
    "Une très célèbre franchise de restauration rapide vient récemment d'engager une poursuite astronomique de cent millions de dollars contre sa maison mère européenne après un déploiement véritablement catastrophique destructeur.", # 3
    "Leur nouvel outil complexe de répartition automatisé a considérablement ralenti les opérations quotidiennes de livraison, détruisant instantanément la rentabilité globale et provoquant une chute vertigineuse des ventes régionales immédiates.", # 4
    "Cette correction silencieuse mais totalement implacable traverse actuellement toutes les sphères financières mondiales, provoquant de terribles sueurs froides chez les investisseurs institutionnels qui ont parié leur immense héritage.", # 5
    "La destruction rapide de capitaux inédits soulève désormais une question fondamentale concernant la véritable valeur intrinsèque des immenses sociétés technologiques qui dominent aujourd'hui les marchés boursiers modernes et volatils.", # 6
    "Les analystes estiment aujourd'hui que des dizaines de milliers d'heures de travail acharné ont été totalement gaspillées pour concevoir des infrastructures numériques finalement inutilisables et complètement défectueuses.", # 7
    "La promesse initiale d'une automatisation parfaite s'est transformée en cauchemar logistique extrêmement coûteux, obligeant les grandes banques mondiales à réviser drastiquement leurs prévisions de croissance future.", # 8
    "Les investisseurs avertis commencent enfin à comprendre que cette frénésie d'accumulation technologique pourrait engendrer une sévère crise financière systémique capable de ravager totalement les portefeuilles institutionnels particulièrement solides.", # 9
    "Dix-neuf mille milliards de dollars de capitalisation virtuelle sont aujourd'hui directement menacés par une correction majeure, d'après les analyses rigoureuses publiées par les experts du célèbre groupe.", # 10
    "Cette gigantesque somme astronomique représente un danger et un risque systémique sans précédent historique depuis la fin tragique des entreprises de l'internet au tout début des années deux mille.", # 11
    "Nous assistons à l'éclatement progressif d'une vaste bulle spéculative, où l'enthousiasme aveugle des investisseurs fortunés se heurte brutalement aux innombrables limites technologiques réelles d'aujourd'hui.", # 12
    "Les colossales infrastructures informatiques nécessitent des ressources électriques qui demeurent physiquement impossibles à déployer correctement, rendant ainsi les immenses investissements initiaux totalement inutiles pour les grandes puissances mondiales.", # 13
    "Pendant que les dirigeants technologiques vendent lâchement leurs propres actions personnelles, les investisseurs institutionnels ordinaires conservent aveuglément leurs portefeuilles, espérant naïvement une reprise économique miraculeuse absolument impossible et illusoire.", # 14
    "Le capital immense accumulé durant ces deux dernières années s'évapore silencieusement, laissant derrière lui une infrastructure énergétique inutile et des promesses d'innovation complètement vides de sens.", # 15
    "Ce revirement brutal des immenses conglomérats occidentaux annonce une sévère correction drastique du marché financier mondial, affectant irrémédiablement le précieux patrimoine sécurisé des familles les plus fortunées aujourd'hui même.", # 16
    "La dure réalité économique finit toujours par rattraper les illusions technologiques les plus séduisantes, détruisant sans aucune pitié les portefeuilles mal diversifiés des investisseurs refusant fièrement cette imminente correction.", # 17
    "Une grande entreprise internationale spécialisée a follement dépensé environ cinq cents millions de dollars en un seul mois pour des outils numériques totalement inutiles, illustrant parfaitement cette folie financière irrationnelle.", # 18
    # Scene 19 correction: "L'effondrement silencieux" -> "Le retournement silencieux"
    "Le retournement silencieux de ces immenses entreprises phares pourrait bientôt se propager vers d'autres secteurs critiques, entraînant une vaste panique boursière inévitable chez tous les grands investisseurs institutionnels européens.", # 19
    "Une prestigieuse institution d'analyse financière confirme que d'immenses projets informatiques atteignant plus de deux gigawatts de puissance électrique totale ont été purement et simplement abandonnés sans aucune explication.", # 20
    "Les contrats de construction massifs sont désormais résiliés silencieusement dans la nuit, laissant derrière eux d'immenses terrains vagues et des chantiers industriels complètement désertés par les promoteurs.", # 21
    "Cette annulation discrète d'infrastructures physiques prouve indéniablement que les gigantesques dirigeants d'empires technologiques ne croient plus du tout en la viabilité financière de leurs propres promesses.", # 22
    "Votre propre patrimoine personnel est-il actuellement lourdement exposé à cette bulle spéculative très dangereuse qui menace brutalement de détruire vos précieuses réserves financières ? Suivez le canal pour la révélation.", # 23
    "Les mêmes conglomérats qui annonçaient récemment la fin du travail humain lancent aujourd'hui de vastes campagnes mondiales pour embaucher discrètement des milliers de nouveaux employés diplômés qualifiés.", # 24
    "Cette contradiction stupéfiante démontre parfaitement l'incapacité chronique des nouveaux systèmes automatisés à résoudre des problèmes intellectuels complexes sans recourir directement à l'intervention indispensable du cerveau humain.", # 25
    "La promesse séduisante d'une entreprise entièrement gérée par des machines intelligentes s'est transformée en un cauchemar logistique terriblement coûteux pour les directeurs financiers des puissantes sociétés occidentales.", # 26
    "Nous observons un retour fulgurant vers les méthodes de gestion traditionnelles et éprouvées, prouvant ainsi la valeur irremplaçable du jugement humain dans les décisions stratégiques les plus cruciales.", # 27
    # Scene 28 correction: "Les faillites silencieuses" -> "Les dissolutions silencieuses"
    "Les dissolutions silencieuses d'entreprises innovantes soutenues par des géants illustrent parfaitement la fragilité extrême d'un modèle économique fondé exclusivement sur des promesses grandioses et des illusions virtuelles.", # 28
    "Chaque jour qui passe révèle de nouvelles annulations massives de projets numériques internationaux, accélérant inévitablement la destruction rapide de capitaux colossaux initialement destinés à construire un avenir radieux.", # 29
    "Un célèbre dirigeant technologique américain recrute soudainement un millier de nouveaux diplômés universitaires pour combler ses propres lacunes techniques, après avoir prédit la destruction massive d'emplois administratifs.", # 30
    "Cette volte-face spectaculaire et silencieuse expose cyniquement l'hypocrisie déconcertante des élites financières, qui manipulent habilement les attentes boursières pour masquer les échecs cuisants de leurs outils numériques.", # 31
    "L'incapacité criante de ces nouvelles technologies à comprendre le contexte humain complexe engendre des erreurs commerciales catastrophiques qui coûtent littéralement des fortunes colossales aux plus grandes entreprises mondiales.", # 32
    "La destruction silencieuse et systématique de la confiance des investisseurs amorce une puissante correction boursière, pulvérisant violemment les portefeuilles aveugles de ceux refusant fermement d'observer ces immenses changements.", # 33
    "Les tribunaux internationaux commencent doucement à recevoir des plaintes massives contre les promesses mensongères d'automatisation, transformant ces illusions technologiques en de véritables cauchemars judiciaires extrêmement coûteux pour tous.", # 34
    "Une compagnie aérienne internationale de premier plan a récemment perdu un jugement retentissant après que son outil automatisé a inventé une fausse politique commerciale, causant un préjudice financier.", # 35
    "Les dirigeants ont vainement tenté d'argumenter juridiquement que leur programme informatique était une entité légale indépendante, une excuse lamentable fermement rejetée par les juges expérimentés des hautes cours.", # 36
    "Cette décision juridique historique crée désormais un précédent extrêmement dangereux pour toutes les autres sociétés qui utilisent imprudemment ces systèmes numériques défectueux pour gérer leurs relations avec les clients.", # 37
    "Les énormes amendes potentielles pourraient rapidement anéantir les maigres bénéfices réalisés par l'automatisation, rendant ces nouvelles technologies beaucoup trop risquées pour être déployées à grande échelle dans les entreprises.", # 38
    "La gestion rigoureuse des risques opérationnels exige impérativement une supervision humaine constante et qualifiée, réduisant complètement à néant les prétendues économies promises par ces sociétés technologiques très novatrices.", # 39
    # Scene 40 correction: "s'est effondrée brutalement" -> "s'est désintégrée brutalement", "fraude comptable" -> "irrégularités comptables massives"
    "Une fameuse entreprise émergente s'est désintégrée brutalement après la découverte soudaine d'irrégularités comptables massives et colossales s'élevant à exactement cent quatre-vingts millions d'euros cette année.", # 40. Wait, "fraude comptable" (2) -> "irrégularités comptables massives" (3). Let's check counts later.
    "Les dirigeants ambitieux prétendaient fièrement construire des logiciels de manière automatisée, alors que des centaines d'ingénieurs humains travaillaient secrètement dans l'ombre pour accomplir toutes les tâches technologiques complexes.", # 41
    "Cette immense supercherie financière démontre tragiquement que la véritable magie technologique vendue aux investisseurs internationaux n'est souvent qu'un simple artifice soigneusement orchestré pour amasser des capitaux considérables rapidement.", # 42
    # Scene 43 correction: "qui s'effondrent brutalement" -> "qui se disloquent brutalement"
    "Vos économies durement gagnées financent-elles actuellement sans le savoir ces dangereuses supercheries technologiques qui se disloquent brutalement de toutes parts ? Suivez le canal pour la prochaine révélation exclusive.", # 43
    "Les investisseurs sophistiqués et expérimentés liquident discrètement mais massivement leurs positions risquées, abandonnant ainsi les actionnaires ordinaires face à une dévaluation boursière imminente et inévitable sur les marchés.", # 44
    "La correction financière brutale qui se prépare actuellement dans l'ombre des grandes salles de marchés mondiales anéantira sans pitié toutes les fortunes familiales mal préparées à ces bouleversements.", # 45
    # Scene 46 correction: "Chaque faillite" -> "Chaque dissolution"
    "Chaque dissolution de ces jeunes entreprises innovantes envoie un message d'avertissement clair aux banquiers concernant l'impossibilité de monétiser rapidement ces colossales infrastructures informatiques lourdement subventionnées par les états.", # 46
    "Le capitalisme moderne n'a jamais pardonné les immenses investissements dépourvus de rentabilité économique concrète, et cette nouvelle bulle spéculative subira inévitablement exactement le même traitement impitoyable que les précédentes.", # 47
    "Les fondations mêmes de cette nouvelle économie virtuelle sont extrêmement fragiles, soutenues uniquement par l'enthousiasme aveugle et irrationnel des foules d'investisseurs inexpérimentés cherchant désespérément un profit facile immédiat.", # 48
    "Les véritables stratèges financiers européens accumulent silencieusement de vastes liquidités tangibles, attendant patiemment le grand éclatement final pour racheter les infrastructures abandonnées à des prix véritablement dérisoires et incroyables.", # 49
    # Scene 50 correction: "L'effondrement colossal" -> "Le retournement colossal"
    "Le retournement colossal de la confiance envers l'automatisation précipitera inévitablement une panique financière mondiale extrêmement dévastatrice, détruisant définitivement les espoirs d'une croissance boursière infinie et miraculeuse pour tous.", # 50
    "Les directeurs généraux dissimulent nerveusement leurs profonds doutes existentiels sous des discours grandiloquents trompeurs, pendant qu'ils annulent discrètement leurs ambitieux projets dans le plus grand secret de leurs bureaux.", # 51
    "La destruction systémique imminente des valorisations technologiques actuelles effacera des décennies entières d'accumulation laborieuse de patrimoine pour les nombreuses familles aveuglées par ces fausses et dangereuses promesses d'innovation.", # 52
    "La réévaluation drastique des gigantesques budgets informatiques mondiaux provoque actuellement un vaste séisme financier silencieux mais terriblement dévastateur, qui menace de ruiner définitivement tous les investisseurs ignorant ces signaux.", # 53
    "Les entreprises les plus solides abandonnent sagement cette dangereuse course irrationnelle pour se reconcentrer exclusivement sur des stratégies commerciales tangibles, réalistes et capables de générer des bénéfices financiers concrets.", # 54
    # Scene 55 correction: "l'effondrement de cet immense édifice" -> "la désintégration de cet immense édifice"
    "Cette sagesse pragmatique retrouvée contraste brutalement avec la folie des petits spéculateurs mal informés, s'accrochant désespérément à leurs illusions virtuelles malgré la désintégration de cet immense édifice financier.", # 55
    "Le marché mondial finira par sanctionner sans pitié les sociétés arrogantes gaspillant leurs immenses capitaux dans la poursuite obstinée de fantasmes technologiques inaccessibles et extrêmement ruineux d'aujourd'hui.", # 56
    "Les fondements inébranlables de l'économie classique exigent systématiquement des rendements réels et palpables, une exigence que cette nouvelle vague spéculative virtuelle est totalement incapable de satisfaire à long terme.", # 57
    "La grande correction financière n'est plus une simple théorie lointaine, mais bien une réalité brutale et mathématique qui se déploie actuellement sous vos yeux émerveillés dans toutes les bourses.", # 58
    "Votre stratégie d'investissement actuelle survivra-t-elle à la liquidation totale et brutale de ces illusions technologiques extrêmement toxiques pour vos capitaux ? Suivez le canal pour la toute dernière révélation.", # 59
]

# Adjust scene 40 to perfectly hit 28-30
# "Une fameuse entreprise émergente s'est désintégrée brutalement après la découverte soudaine d'irrégularités comptables massives et colossales s'élevant à exactement cent quatre-vingts millions d'euros cette année." # 29
sentences[40] = "Une fameuse entreprise émergente s'est désintégrée brutalement après la découverte soudaine d'irrégularités comptables massives et colossales s'élevant à exactement cent quatre-vingts millions d'euros cette année."

# Verify counts
has_error = False
for i, s in enumerate(sentences):
    co = count_fr_words(s)
    if co < 28 or co > 30:
        print(f"Error {i}: {co} -> {s}")
        has_error = True

if has_error:
    exit(1)

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
    cam = camera_moves[n % len(camera_moves)]

    if n == 0:
        script += f"""SCENE 0 — SCROLL STOPPER — 10 SECONDS
OMNI FLASH — Text-to-video 10s — 9:16
[LOCATION] Bourse historique de Paris, colonnes corinthiennes monumentales — deux mille vingt-six — ARTE golden sepia
[SUBJECT] @Narrateur en costume sur-mesure bleu marine en cachemire, visage entièrement visible, lèvres synchronisées avec la narration.
[ACTION] ULTRA-FAST COLLAGE — 5 FLASH CUTS IN 10 SECONDS:
0.0-2.0s: EXTREME STEADICAM PUSH-IN sur le visage de @Narrateur, lèvres en mouvement constant, regard direct vers l'objectif.
2.0-4.0s: FLASH CUT — main ajustant une montre en or massif — mouvement circulaire rapide autour de l'objet.
4.0-6.0s: FLASH CUT — chute dramatique de graphiques boursiers gravés sur cristal — dutch angle agressif.
6.0-8.0s: FLASH CUT — @Narrateur marchant vigoureusement devant de vastes colonnes antiques — contre-plongée dominante.
8.0-10.0s: total ORBITAL PULL BACK — révélant un coffre-fort colossal et vide — fondu noir total immédiat.
[CAMERA] Steadicam push-in, extreme, objectif 35mm anamorphique f/2.8.
[AUDIO] @Voice: NarradorFR. Zero music.
[CHANNEL COLORIMETRY] ARRI Alexa LF. 8K. ARTE golden sepia.
Narrator: "{text}" ({count_fr_words(text)} ✅)
NEGATIVE: no static freeze-frame, no motionless actors, no locked camera, no still image, no photo-like render, no on-screen text, no code, no modern laptop, no whiteboard, no generic conference room, no logos, no watermarks, no music.\n\n"""
    else:
        loc = locations[n-1]
        act3 = actor3_actions[n-1]
        act2 = actor2_actions_props[n-1]

        script += f"""SCENE {n} — {loc.upper()} — DEUX MILLE VINGT-SIX
[LOCATION] {loc} — deux mille vingt-six — ARTE golden sepia
[SUBJECT] @Narrateur en costume croisé en laine vierge sombre, lèvres synchronisées avec les syllabes exactes de la narration.
[ACTION] @Narrateur marche de façon dynamique en gesticulant largement avec les deux bras pour souligner chaque argument.
Le deuxième acteur en arrière-plan {act2} avec des mouvements amples, visibles et constants tout au long de la scène.
Le troisième acteur {act3.lower()} avec un effort physique visible sans s'arrêter.
[CAMERA] {cam}, objectif 35mm anamorphique f/2.8. 10 seconds continuous.
[AUDIO] @Voice: NarradorFR. Zero music.
[CHANNEL COLORIMETRY] ARRI Alexa LF. 8K. ARTE golden sepia.
Narrator: "{text}" ({count_fr_words(text)} ✅)
NEGATIVE: no static freeze-frame, no motionless actors, no locked camera, no still image, no photo-like render, no on-screen text, no code, no modern laptop, no whiteboard, no generic conference room, no logos, no watermarks, no music.\n\n"""

with open('EP09_SILICON_MONEY_FR/DIRECTOR_SCRIPT_v2.txt', 'w', encoding='utf-8') as f:
    f.write(script.strip() + "\n")

print("DIRECTOR_SCRIPT_v2.txt generated.")
