#!/usr/bin/python3
# -*- encoding:utf-8 -*-

familiyttt=["antipsychotiques", "antiépileptiques", "antidépresseurs", 
      "anxiolytiques", "thymorégulateurs", "somnifères", "benzodiazépines", 
      "inhibiteurs de la cholinestérase", "antiparkinsoniens"]

oneDrug=["chlorpromazine", "prazine", "atarax", "demetrin", "prazépam", "briviact", 
      "brivaracétam", "abilify", "aripiprazol", "clopixol", "clopin", "clozapine", 
      "leponex", "carbamazépine", "tégrétol", "dépakine", "valproate", "haldol", 
      "halopéridol", "entumine", "clotiapine", "fluanxol", "flupentixol", "nozinan", 
      "levomepromazine", "tiapridal", "dogmatil", "sulpride", "invega", "palipéridone", 
      "olanzapine", "zyprexa", "risperdal", "risperdone", "seroquel", "sequase", "quétiapine", 
      "solian", "amisulpride", "ethosuximide", "pétinimid", "mysoline", "primidone", 
      "phénobarbital", "aphénylbarbite", "phénytoïne", "fycompa", "pérampanel", "inovelon", 
      "rufinamide", "keppra", "levetiracetam", "lamictal", "lamotrigine", "lyrica", 
      "prégabaline", "neurontin", "gabapentine", "sabril", "vigabatrin", "taloxa", "felbamate", 
      "topamax", "topiramate", "trileptal", "oxcarbazépine", "vimpat", "lacosamide", "zonegran", 
      "zonisamide", "lexotanil", "bromazépam", "rivotril", "clonazépam", "rohypnol", 
      "flunitrazepamum", "seresta", "oxazépam", "temesta", "lorazépam", "tranxilium", 
      "clorazépate", "urbanyl", "clobazam", "valium", "diazépam", "xanax", "alprazolam",
      "anafranil", "clomipramine", "saroten", "amitriptyline", "surmontil", "trimipramine",
      "trittico", "trazodone", "lithium"]

"""

ATD :
-----
Antidépresseurs TCC (tricycliques): Anafranil; Ludiomil; Saroten; Surmontil; Tofranil; Trittico. --- OK

Antidépresseurs ISRS (inhibiteurs sélectifs de la recapture en sérotonine): Citalopram (Seropram); escitalopram 
(Cipralex); fluoxétine (Prozac); fluvoxamine (Floxyfral); Deroxat (Paroxétine); Sertraline (Zoloft).

Antidépresseurs IRSNA (inhibiteurs de la recapture de la sérotonine-noradrénaline): Venlafaxine; Duloxétine.

Inhibiteurs de la recapture de la dopamine-noradrénaline: Bupropion (wellbutrine).

IMAO sélectifs (inhibiteurs de la mono-amine oxydase): Aurorix; Moclamine.

IMAO non-sélectifs: Regitine (Phantolamine).

Antidépresseurs sélectifs: Cymbalta; Effexor; Remeron.


Somnifères :
------------
BZD hypno-inducteurs: Dalmadorm; Dormicum; Halcion; Noctamid.

Sédatifs et anxiolytiques non BZD: Atarax; Buspar; Imovane; Stilnox.

Antihistaminiques et neuroleptiques: Atarax; Benocten; Detensor; Melatonine; Nozinan; Phénegran; Truxal.

Benzodiazépines: Lexotanil; Tranxilium; Rohypnol.

Non-barbituriques: Distraneurin.

Barbituriques: Tous ceux finissant par ...barbital.

Autres hypnotiques: Stilnox CR; Circadin; Sonata.


Stabilisateurs de l'humeur : 
----------------------------
Carbamazépine; Dépakine; Lamotrigine; Lithium; Valproate; Zyprexa.

Stabilisateurs d'humeur
Stabilisateurs de l'humeur: Carbamazépine; Dépakine; Lamotrigine; Lithium; Valproate; Zyprexa.


Les benzodiazépines :
---------------------
Benzo: Dormicum, Halcion, Stilnox, Imovane, Sonata, Xanax, Lexotanil, Rohypnol, Temesta, Noctamid, 
Seresta, Urbanyl, Rivotril, Tranxilium, Valium, Dalmadorm, Demetrin.


Inhibiteurs de la cholinestérase:
---------------------------------
dopénézil (Ariecpt); galantamine (Reminyl); rivastigmine (Exelon); 
mémantine (Axura)


Contre les dyskinésies / Lévodopa + carbidopa :
-----------------------------------------------
Duodopa; Carbidopa/Levodopa; Lecapon; Sinemet


Contre les dyskinésies / Lévodopa + inhibiteur de la décarboxylase + inhibiteur de la COMT :
--------------------------------------------------------------------------------------------
Stalevo

"""