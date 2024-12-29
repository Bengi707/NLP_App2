DT = [
    ["that", {"number": "SG"}],
    [["this", {"number": "SG"}]],
    [["a", {"number": "SG"}]],
    [["the", {"number": "any"}]],  # Neutral to singular/plural
    [["an", {"number": "SG"}]],
    [["these", {"number": "PL"}]],
    [["those", {"number": "PL"}]],
]

NN = [
    [["book", {"number": "SG"}]],
    [["flight", {"number": "SG"}]],
    [["meal", {"number": "SG"}]],
    [["money", {"number": "SG"}]],
    [["present", {"number": "SG"}]],
    [["school", {"number": "SG"}]],
    [["music", {"number": "SG"}]],
    [["movie", {"number": "SG"}]],
    [["friend", {"number": "SG"}]],
    [["apple", {"number": "SG"}]],
    [["face", {"number": "SG"}]],
    [["market", {"number": "SG"}]],
    [["dog", {"number": "SG"}]],
    [["cat", {"number": "SG"}]],
    [["house", {"number": "SG"}]],
    [["car", {"number": "SG"}]],
    [["teacher", {"number": "SG"}]],
    [["child", {"number": "SG"}]],
    [["idea", {"number": "SG"}]],
    [["story", {"number": "SG"}]],
    [["game", {"number": "SG"}]],
    [["photo", {"number": "SG"}]],
    [["river", {"number": "SG"}]],
    [["city", {"number": "SG"}]],
    [["garden", {"number": "SG"}]],
    [["song", {"number": "SG"}]],
    [["phone", {"number": "SG"}]],
    [["computer", {"number": "SG"}]],
    [["table", {"number": "SG"}]],
    [["bottle", {"number": "SG"}]],
    [["shirt", {"number": "SG"}]],
    [["painting", {"number": "SG"}]],
    [["fruit", {"number": "SG"}]],
    [["watermelon", {"number": "SG"}]],
    [["mother", {"number": "SG"}]],
    [["summer", {"number": "SG"}]],
    [["village", {"number": "SG"}]],
]

NNS = [
    [["books", {"number": "PL"}]],
    [["flights", {"number": "PL"}]],
    [["meals", {"number": "PL"}]],
    [["presents", {"number": "PL"}]],
    [["schools", {"number": "PL"}]],
    [["friends", {"number": "PL"}]],
    [["apples", {"number": "PL"}]],
    [["faces", {"number": "PL"}]],
    [["markets", {"number": "PL"}]],
    [["dogs", {"number": "PL"}]],
    [["cats", {"number": "PL"}]],
    [["houses", {"number": "PL"}]],
    [["cars", {"number": "PL"}]],
    [["teachers", {"number": "PL"}]],
    [["children", {"number": "PL"}]],
    [["ideas", {"number": "PL"}]],
    [["stories", {"number": "PL"}]],
    [["games", {"number": "PL"}]],
    [["photos", {"number": "PL"}]],
    [["rivers", {"number": "PL"}]],
    [["cities", {"number": "PL"}]],
    [["gardens", {"number": "PL"}]],
    [["songs", {"number": "PL"}]],
    [["phones", {"number": "PL"}]],
    [["computers", {"number": "PL"}]],
    [["tables", {"number": "PL"}]],
    [["bottles", {"number": "PL"}]],
    [["shirts", {"number": "PL"}]],
    [["paintings", {"number": "PL"}]],
    [["fruits", {"number": "PL"}]],
    [["watermelons", {"number": "PL"}]],
    [["mothers", {"number": "PL"}]],
    [["summers", {"number": "PL"}]],
    [["villages", {"number": "PL"}]],
]

# Base form verbs (non-past tense)
VB = [
    [["prefer", {"person": "any", "tense": "any"}]],
    [["include", {"person": "any", "tense": "any"}]],
    [["eat", {"person": "any", "tense": "any"}]],
    [["take", {"person": "any", "tense": "any"}]],
    [["want", {"person": "any", "tense": "any"}]],
    [["watch", {"person": "any", "tense": "any"}]],
    [["spend", {"person": "any", "tense": "any"}]],
    [["enjoy", {"person": "any", "tense": "any"}]],
    [["book", {"person": "any", "tense": "any"}]],
    [["present", {"person": "any", "tense": "any"}]],
    [["build", {"person": "any", "tense": "any"}]],
    [["sing", {"person": "any", "tense": "any"}]],
    [["dance", {"person": "any", "tense": "any"}]],
    [["paint", {"person": "any", "tense": "any"}]],
    [["write", {"person": "any", "tense": "any"}]],
    [["call", {"person": "any", "tense": "any"}]],
    [["drive", {"person": "any", "tense": "any"}]],
    [["buy", {"person": "any", "tense": "any"}]],
    [["sell", {"person": "any", "tense": "any"}]],
    [["read", {"person": "any", "tense": "any"}]],
    [["open", {"person": "any", "tense": "any"}]],
    [["close", {"person": "any", "tense": "any"}]],
    [["fix", {"person": "any", "tense": "any"}]],
    [["carry", {"person": "any", "tense": "any"}]],
    [["create", {"person": "any", "tense": "any"}]],
    [["explore", {"person": "any", "tense": "any"}]],
    [["face", {"person": "any", "tense": "any"}]],
]

# Past tense verbs (same form for singular and plural)
VBD = [
    [["bought", {"person": "any", "tense": "past"}]],
    [["helped", {"person": "any", "tense": "past"}]],
    [["watched", {"person": "any", "tense": "past"}]],
    [["ate", {"person": "any", "tense": "past"}]],
    [["took", {"person": "any", "tense": "past"}]],
    [["spent", {"person": "any", "tense": "past"}]],
    [["enjoyed", {"person": "any", "tense": "past"}]],
    [["booked", {"person": "any", "tense": "past"}]],
    [["presented", {"person": "any", "tense": "past"}]],
    [["went", {"person": "any", "tense": "past"}]],
    [["was", {"person": "3", "tense": "past"}]],
    [["were", {"person": "1", "tense": "past"}]],
    [["built", {"person": "any", "tense": "past"}]],
    [["sang", {"person": "any", "tense": "past"}]],
    [["danced", {"person": "any", "tense": "past"}]],
    [["painted", {"person": "any", "tense": "past"}]],
    [["wrote", {"person": "any", "tense": "past"}]],
    [["called", {"person": "any", "tense": "past"}]],
    [["drove", {"person": "any", "tense": "past"}]],
    [["sold", {"person": "any", "tense": "past"}]],
    [["read", {"person": "any", "tense": "past"}]],
    [["opened", {"person": "any", "tense": "past"}]],
    [["closed", {"person": "any", "tense": "past"}]],
    [["fixed", {"person": "any", "tense": "past"}]],
    [["carried", {"person": "any", "tense": "past"}]],
    [["created", {"person": "any", "tense": "past"}]],
    [["explored", {"person": "any", "tense": "past"}]],
    [["faced", {"person": "any", "tense": "past"}]],
]

# 3rd person singular present verbs (tense "present" and person "3")
VBZ = [
    [["prefers", {"person": "3", "tense": "any"}]],
    [["includes", {"person": "3", "tense": "any"}]],
    [["eats", {"person": "3", "tense": "any"}]],
    [["takes", {"person": "3", "tense": "any"}]],
    [["spends", {"person": "3", "tense": "any"}]],
    [["watches", {"person": "3", "tense": "any"}]],
    [["enjoys", {"person": "3", "tense": "any"}]],
    [["books", {"person": "3", "tense": "any"}]],
    [["presents", {"person": "3", "tense": "any"}]],
    [["goes", {"person": "3", "tense": "any"}]],
    [["builds", {"person": "3", "tense": "any"}]],
    [["sings", {"person": "3", "tense": "any"}]],
    [["dances", {"person": "3", "tense": "any"}]],
    [["paints", {"person": "3", "tense": "any"}]],
    [["writes", {"person": "3", "tense": "any"}]],
    [["calls", {"person": "3", "tense": "any"}]],
    [["drives", {"person": "3", "tense": "any"}]],
    [["buys", {"person": "3", "tense": "any"}]],
    [["sells", {"person": "3", "tense": "any"}]],
    [["reads", {"person": "3", "tense": "any"}]],
    [["opens", {"person": "3", "tense": "any"}]],
    [["closes", {"person": "3", "tense": "any"}]],
    [["fixes", {"person": "3", "tense": "any"}]],
    [["carries", {"person": "3", "tense": "any"}]],
    [["creates", {"person": "3", "tense": "any"}]],
    [["explores", {"person": "3", "tense": "any"}]],
    [["faces", {"person": "3", "tense": "any"}]],
]

# Non-3rd person singular present verbs (no "s" ending, plural subjects)
VBP = [
    [["prefer", {"person": "1", "tense": "any"}]],
    [["include", {"person": "1", "tense": "any"}]],
    [["eat", {"person": "1", "tense": "any"}]],
    [["take", {"person": "1", "tense": "any"}]],
    [["spend", {"person": "1", "tense": "any"}]],
    [["watch", {"person": "1", "tense": "any"}]],
    [["enjoy", {"person": "1", "tense": "any"}]],
    [["book", {"person": "1", "tense": "any"}]],
    [["present", {"person": "1", "tense": "any"}]],
    [["build", {"person": "1", "tense": "any"}]],
    [["sing", {"person": "1", "tense": "any"}]],
    [["dance", {"person": "1", "tense": "any"}]],
    [["paint", {"person": "1", "tense": "any"}]],
    [["write", {"person": "1", "tense": "any"}]],
    [["call", {"person": "1", "tense": "any"}]],
    [["drive", {"person": "1", "tense": "any"}]],
    [["buy", {"person": "1", "tense": "any"}]],
    [["sell", {"person": "1", "tense": "any"}]],
    [["read", {"person": "1", "tense": "any"}]],
    [["open", {"person": "1", "tense": "any"}]],
    [["close", {"person": "1", "tense": "any"}]],
    [["fix", {"person": "1", "tense": "any"}]],
    [["carry", {"person": "1", "tense": "any"}]],
    [["create", {"person": "1", "tense": "any"}]],
    [["explore", {"person": "1", "tense": "any"}]],
    [["face", {"person": "1", "tense": "any"}]],
]


# Personal pronouns
PRP = [
    [["I"], {"person": "1"}],
    [["she"], {"person": "3"}],
    [["we"], {"person": "1"}],
    [["you"], {"person": "1"}],
    [["her"], {"person": "3"}],
    [["he"], {"person": "3"}],
    [["it"], {"person": "3"}],
    [["they"], {"person": "1"}],
    [["them"], {"person": "1"}]
]

NNP= [["Houston"], ["NWA"]]  # Singular proper nouns
# Prepositions
IN= [
    ["from"], ["to"], ["on"], ["near"], ["through"], ["with"], ["under"], ["over"], ["beside"],
    ["between"], ["before"], ["after"], ["inside"], ["outside"], ["around"], ["above"], ["below"]
]
# Adverbs
RB= [
    ["quickly"], ["slowly"], ["often"], ["always"], ["never"], ["here"], ["yesterday"],
    ["today"], ["tomorrow"], ["carefully"], ["happily"], ["sadly"], ["silently"], ["loudly"],
    ["angrily"], ["eagerly"]
]
# Modal verbs
MD = [
    [["will"], {"tense": "future"}],
    [["can"], {"tense": "any"}],
    [["should"], {"tense": "any"}],
    [["would"], {"tense": "past"}],
    [["may"], {"tense": "any"}],
    [["might"], {"tense": "any"}],
    [["must"], {"tense": "any"}]
]

VBG= [
    ["playing"], ["running"], ["watching"], ["painting"], ["calling"], ["helping"], ["working"], ["riding"], ["moving"],
    ["jumping"], ["cooking"], ["fighting"], ["dreaming"], ["dancing"], ["kissing"], ["planning"], ["visiting"],
    ["starting"], ["ending"], ["going"], ["eating"], ["spending"], ["enjoying"], ["taking"], ["including"],
    ["preferring"]
]
# Possible wh-words
Wh_Word= [
    ["what"], ["where"], ["when"], ["why"], ["how"]
]
JJ= [
    ["red"], ["blue"], ["big"], ["small"], ["delicious"], ["beautiful"], ["interesting"], ["important"], ["happy"],
    ["sad"], ["fast"], ["slow"], ["heavy"], ["light"], ["young"], ["old"], ["rich"], ["poor"], ["strong"], ["weak"],
    ["friendly"], ["angry"], ["quiet"], ["loud"], ["clean"], ["dirty"], ["long"], ["short"], ["thick"], ["thin"],
    ["hot"], ["cold"], ["warm"], ["cool"], ["soft"], ["hard"], ["sharp"], ["smooth"], ["rough"], ["expensive"],
    ["cheap"], ["sweet"], ["sour"], ["bitter"], ["spicy"], ["tall"], ["short"], ["early"], ["late"], ["kind"],
    ["generous"], ["selfish"], ["brave"], ["breathtaking"], ["gorgeous"], ["active"], ["funny"], ["serious"],
    ["polite"],
    ["rude"], ["creative"], ["boring"], ["beautiful"], ["ugly"], ["pleasant"], ["unpleasant"], ["calm"], ["nervous"]
]

JJR= [
    ["bigger"], ["smaller"], ["more delicious"], ["more beautiful"], ["more interesting"], ["happier"], ["sadder"],
    ["faster"], ["slower"], ["heavier"], ["lighter"], ["younger"], ["older"], ["richer"], ["poorer"], ["stronger"],
    ["weaker"], ["friendlier"], ["angrier"], ["quieter"], ["louder"], ["cleaner"], ["dirtier"], ["longer"], ["shorter"],
    ["thicker"], ["thinner"], ["hotter"], ["colder"], ["warmer"], ["cooler"], ["softer"], ["harder"], ["sharper"],
    ["smoother"], ["rougher"], ["more expensive"], ["cheaper"], ["sweeter"], ["sourer"], ["more bitter"], ["spicier"],
    ["taller"], ["shorter"], ["earlier"], ["later"], ["kinder"], ["more generous"], ["more selfish"], ["braver"],
    ["cowardlier"], ["lazier"], ["more active"], ["funnier"], ["more serious"], ["more polite"], ["ruder"],
    ["more creative"], ["more boring"], ["more beautiful"], ["uglier"], ["more pleasant"], ["more unpleasant"],
    ["calmer"], ["more nervous"]
]

JJS= [
    ["biggest"], ["smallest"], ["fastest"], ["slowest"], ["youngest"], ["oldest"], ["happiest"],
    ["saddest"], ["strongest"], ["weakest"], ["brightest"], ["darkest"], ["smartest"],
    ["most delicious"], ["most beautiful"], ["most interesting"], ["most important"]
]

AUX= [["does"], ["did"], ["do"], ["am"], ["is"], ["are"]]
Neg= [["not"]]
DO= [["do"]]



grammar_rules = {
    "S": [
        ["NP", "VP"],    # Declarative

        # Declarative Negation Rules
        ["X7", "VP"],    # Declarative with negation

        # VP : Imperative
        VB,  # Base form verb  ["VB"]
        VBD,  # Past tense verb ["VBD"]
        [VBZ, "NP"],  # 3rd person singular present verb + NP
        [VBP, "NP"],  # Non-3rd person singular present verb + NP
        [VBD, "NP"],  # Past tense verb + NP
        ["X1", "PP"],  # Base form verb + NP + PP
        ["VP", "PP"],  # VP + PP
        # Imperative sentence rule:
        [VB, "NP"],
        [AUX, VBG],

        # Imperative Negation Rules
        ["X8",VB],

        # Questions
        ["X4", "VP"],  # Yes/No Question: Modal verb + NP + VP
        ["X3", "X2"]  # Wh-Question: Wh-word + Modal verb + NP + VP

    ],

    "NP": [
        PRP,  # Pronoun  ["PRP"]
        NNP,  # Singular Proper Noun ["NNP"]
        [DT, "Nominal"]  # Determiner + Nominal
    ],

    "Nominal": [
        NN,  # Singular Noun ["NN"]
        NNS,  # Plural Noun   ["NNS"]
        ["Nominal", NN],  # Nominal + Singular Noun
        ["Nominal", "PP"],  # Nominal + Prepositional Phrase
        [JJ, "Nominal"],  # Base Adjective + Nominal
        [JJR, "Nominal"],  # Comparative Adjective + Nominal
        [JJS, "Nominal"],  # Superlative Adjective + Nominal
        VBG # Gerund as Nominal
    ],

    "VP": [
        # Declarative sentence rule:
        VB,  # Base form verb  ["VB"]
        VBD,  # Past tense verb ["VBD"]
        [VBZ, "NP"],  # 3rd person singular present verb + NP
        [VBP, "NP"],  # Non-3rd person singular present verb + NP
        [VBD, "NP"],  # Past tense verb + NP
        ["X1", "PP"],  # Base form verb + NP + PP
        ["VP", "PP"],  # VP + PP
        # Imperative sentence rule:
        [VB, "NP"],
        [AUX, VBG],
    ],

    "X1":[
        [VB, "NP"],
    ],

    "X2":[
        ["NP", "VP"],
    ],

    "X3":[
        [Wh_Word, MD],
    ],

    "X4":[
        [MD, "NP"],
    ],

    "X5": [
        [AUX,Neg]
    ],

    "X6": [
        [MD,Neg]
    ],

    "X7": [

        ["NP","X5"],
        ["NP","X6"],

    ],
    "X8": [
        [DO, Neg]
    ],


    "PP": [
        [IN, "NP"]  # Preposition + NP
    ]

}
