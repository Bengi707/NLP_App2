class Word:
    def __init__(self, text, number="any",person="any",tense="any"):
        self.text = text
        self.person = person
        self.number = number
        self.tense = tense

DT = [
    [Word("that","SG")],[Word("this","SG")],
    [Word("a","SG")],[Word("the")],# Neutral to singular/plural
    [Word("an","SG")],[Word("these","PL",)],
    [Word("those","PL")],
]

NN = [
    [Word("book","SG")],[Word("flight","SG")],[Word("meal","SG")],
    [Word("money","SG")],[Word("present","SG")],[Word("school","SG")],
    [Word("music","SG")],[Word("movie","SG")],[Word("friend","SG")],
    [Word("apple","SG")],[Word("face","SG")],[Word("market","SG")],
    [Word("face","SG")],[Word("dog","SG")],[Word("cat","SG")],
    [Word("house","SG")],[Word("teacher","SG")],[Word("child","SG")],
    [Word("story","SG")],[Word("photo","SG")],[Word("river","SG")],
    [Word("city","SG")],[Word("garden", "SG")],[Word("song", "SG")],
    [Word("phone", "SG")],[Word("computer", "SG")],[Word("table", "SG")],
    [Word("bottle", "SG")],[Word("shirt", "SG")],[Word("painting", "SG")],
    [Word("fruit", "SG")],[Word("watermelon", "SG")],[Word("mother", "SG")],
    [Word("summer", "SG")],[Word("village", "SG")],
]

NNS = [
    [Word("books","PL")],[Word("flights","PL")],[Word("meals","PL")],
    [Word("presents","PL")],[Word("schools","PL")],[Word("friends","PL")],
    [Word("apples","PL")],[Word("faces","PL")],[Word("markets","PL")],
    [Word("dogs","PL")],[Word("cats","PL")],[Word("houses","PL")],
    [Word("cars","PL")],[Word("teachers","PL")],[Word("children","PL")],
    [Word("ideas","PL")],[Word("books","PL")],[Word("stories","PL")],
    [Word("games","PL")],[Word("photos","PL")],[Word("rivers","PL")],
    [Word("cities","PL")],[Word("gardens","PL")],[Word("songs","PL")],
    [Word("phones","PL")],[Word("computers","PL")],[Word("tables","PL")],
    [Word("bottles","PL")],[Word("shirts","PL")],[Word("paintings","PL")],
    [Word("watermelons","PL")],[Word("mothers","PL")],[Word("summers","PL")],
    [Word("villages","PL")]
]

# Base form verbs (non-past tense)
VB = [
    [Word("prefer", "any", "any", "any")],[Word("include", "any", "any", "any")],
    [Word("eat", "any", "any", "any")],[Word("take", "any", "any", "any")],
    [Word("want", "any", "any", "any")],[Word("watch", "any", "any", "any")],
    [Word("spend", "any", "any", "any")],[Word("enjoy", "any", "any", "any")],
    [Word("book", "any", "any", "any")],[Word("present", "any", "any", "any")],
    [Word("build", "any", "any", "any")],[Word("sing", "any", "any", "any")],
    [Word("dance", "any", "any", "any")],[Word("paint", "any", "any", "any")],
    [Word("write", "any", "any", "any")],[Word("call", "any", "any", "any")],
    [Word("drive", "any", "any", "any")],[Word("buy", "any", "any", "any")],
    [Word("sell", "any", "any", "any")],[Word("read", "any", "any", "any")],
    [Word("open", "any", "any", "any")],[Word("close", "any", "any", "any")],
    [Word("fix", "any", "any", "any")],[Word("carry", "any", "any", "any")],
    [Word("create", "any", "any", "any")],[Word("explore", "any", "any", "any")],
    [Word("face", "any", "any", "any")],
]

# Past tense verbs (same form for singular and plural)
VBD = [
    [Word("bought", "any", "past", "any")],[Word("helped", "any", "past", "any")],
    [Word("watched", "any", "past", "any")],[Word("ate", "any", "past", "any")],
    [Word("took", "any", "past", "any")],[Word("spent", "any", "past", "any")],
    [Word("enjoyed", "any", "past", "any")],[Word("booked", "any", "past", "any")],
    [Word("presented", "any", "past", "any")],[Word("went", "any", "past", "any")],
    [Word("was", "3", "past", "any")],[Word("were", "1", "past", "any")],
    [Word("built", "any", "past", "any")],[Word("sang", "any", "past", "any")],
    [Word("danced", "any", "past", "any")],[Word("painted", "any", "past", "any")],
    [Word("wrote", "any", "past", "any")],[Word("called", "any", "past", "any")],
    [Word("drove", "any", "past", "any")],[Word("sold", "any", "past", "any")],
    [Word("read", "any", "past", "any")],[Word("opened", "any", "past", "any")],
    [Word("closed", "any", "past", "any")],[Word("fixed", "any", "past", "any")],
    [Word("carried", "any", "past", "any")],[Word("created", "any", "past", "any")],
    [Word("explored", "any", "past", "any")],[Word("faced", "any", "past", "any")],
]

# 3rd person singular present verbs (tense "present" and person "3")
VBZ = [
    [Word("prefers", "3", "any", "any")],[Word("includes", "3", "any", "any")],
    [Word("eats", "3", "any", "any")],[Word("takes", "3", "any", "any")],
    [Word("spends", "3", "any", "any")],[Word("watches", "3", "any", "any")],
    [Word("enjoys", "3", "any", "any")],[Word("books", "3", "any", "any")],
    [Word("presents", "3", "any", "any")],[Word("goes", "3", "any", "any")],
    [Word("builds", "3", "any", "any")],[Word("sings", "3", "any", "any")],
    [Word("dances", "3", "any", "any")],[Word("paints", "3", "any", "any")],
    [Word("writes", "3", "any", "any")],[Word("calls", "3", "any", "any")],
    [Word("drives", "3", "any", "any")],[Word("buys", "3", "any", "any")],
    [Word("sells", "3", "any", "any")],[Word("reads", "3", "any", "any")],
    [Word("opens", "3", "any", "any")],[Word("closes", "3", "any", "any")],
    [Word("fixes", "3", "any", "any")],[Word("carries", "3", "any", "any")],
    [Word("creates", "3", "any", "any")],[Word("explores", "3", "any", "any")],
    [Word("faces", "3", "any", "any")],
]

# Non-3rd person singular present verbs (no "s" ending, plural subjects)
VBP = [
    [Word("prefer", "1", "any", "any")],[Word("include", "1", "any", "any")],
    [Word("eat", "1", "any", "any")],[Word("take", "1", "any", "any")],
    [Word("spend", "1", "any", "any")],[Word("watch", "1", "any", "any")],
    [Word("enjoy", "1", "any", "any")],[Word("book", "1", "any", "any")],
    [Word("present", "1", "any", "any")],[Word("build", "1", "any", "any")],
    [Word("sing", "1", "any", "any")],[Word("dance", "1", "any", "any")],
    [Word("paint", "1", "any", "any")],[Word("write", "1", "any", "any")],
    [Word("call", "1", "any", "any")],[Word("drive", "1", "any", "any")],
    [Word("buy", "1", "any", "any")],[Word("sell", "1", "any", "any")],
    [Word("read", "1", "any", "any")],[Word("open", "1", "any", "any")],
    [Word("close", "1", "any", "any")],[Word("fix", "1", "any", "any")],
    [Word("carry", "1", "any", "any")],[Word("create", "1", "any", "any")],
    [Word("explore", "1", "any", "any")],[Word("face", "1", "any", "any")],
]

# Personal pronouns
PRP = [
    [Word("I", "1", "any", "any")],
    [Word("she", "3", "any", "any")],
    [Word("we", "1", "any", "any")],
    [Word("you", "1", "any", "any")],
    [Word("her", "3", "any", "any")],
    [Word("he", "3", "any", "any")],
    [Word("it", "3", "any", "any")],
    [Word("they", "1", "any", "any")],
    [Word("them", "1", "any", "any")],
]

# Singular proper nouns
NNP = [
    [Word("Houston", "any", "any", "any")],
    [Word("NWA", "any", "any", "any")]
]

# Prepositions
IN = [
    [Word("from", "any", "any", "any")],
    [Word("to", "any", "any", "any")],
    [Word("on", "any", "any", "any")],
    [Word("near", "any", "any", "any")],
    [Word("through", "any", "any", "any")],
    [Word("with", "any", "any", "any")],
    [Word("under", "any", "any", "any")],
    [Word("over", "any", "any", "any")],
    [Word("beside", "any", "any", "any")],
    [Word("between", "any", "any", "any")],
    [Word("before", "any", "any", "any")],
    [Word("after", "any", "any", "any")],
    [Word("inside", "any", "any", "any")],
    [Word("outside", "any", "any", "any")],
    [Word("around", "any", "any", "any")],
    [Word("above", "any", "any", "any")],
    [Word("below", "any", "any", "any")]
]

# Adverbs
RB = [
    [Word("quickly", "any", "any", "any")],
    [Word("slowly", "any", "any", "any")],
    [Word("often", "any", "any", "any")],
    [Word("always", "any", "any", "any")],
    [Word("never", "any", "any", "any")],
    [Word("here", "any", "any", "any")],
    [Word("yesterday", "any", "any", "any")],
    [Word("today", "any", "any", "any")],
    [Word("tomorrow", "any", "any", "any")],
    [Word("carefully", "any", "any", "any")],
    [Word("happily", "any", "any", "any")],
    [Word("sadly", "any", "any", "any")],
    [Word("silently", "any", "any", "any")],
    [Word("loudly", "any", "any", "any")],
    [Word("angrily", "any", "any", "any")],
    [Word("eagerly", "any", "any", "any")]
]

# Modal verbs
MD = [
    [Word("will", "any", "future", "any")],
    [Word("can", "any", "any", "any")],
    [Word("should", "any", "any", "any")],
    [Word("would", "any", "past", "any")],
    [Word("may", "any", "any", "any")],
    [Word("might", "any", "any", "any")],
    [Word("must", "any", "any", "any")]
]

# Present participles (VBG)
VBG = [
    [Word("playing", "any", "any", "present")],
    [Word("running", "any", "any", "present")],
    [Word("watching", "any", "any", "present")],
    [Word("painting", "any", "any", "present")],
    [Word("calling", "any", "any", "present")],
    [Word("helping", "any", "any", "present")],
    [Word("working", "any", "any", "present")],
    [Word("riding", "any", "any", "present")],
    [Word("moving", "any", "any", "present")],
    [Word("jumping", "any", "any", "present")],
    [Word("cooking", "any", "any", "present")],
    [Word("fighting", "any", "any", "present")],
    [Word("dreaming", "any", "any", "present")],
    [Word("dancing", "any", "any", "present")],
    [Word("kissing", "any", "any", "present")],
    [Word("planning", "any", "any", "present")],
    [Word("visiting", "any", "any", "present")],
    [Word("starting", "any", "any", "present")],
    [Word("ending", "any", "any", "present")],
    [Word("going", "any", "any", "present")],
    [Word("eating", "any", "any", "present")],
    [Word("spending", "any", "any", "present")],
    [Word("enjoying", "any", "any", "present")],
    [Word("taking", "any", "any", "present")],
    [Word("including", "any", "any", "present")],
    [Word("preferring", "any", "any", "present")]
]

# Possible wh-words
Wh_Word = [
    [Word("what", "any", "any", "any")],
    [Word("where", "any", "any", "any")],
    [Word("when", "any", "any", "any")],
    [Word("why", "any", "any", "any")],
    [Word("how", "any", "any", "any")]
]

# Adjectives (JJ)
JJ = [
    [Word("red", "any", "any", "any")],[Word("blue", "any", "any", "any")],
    [Word("big", "any", "any", "any")],[Word("small", "any", "any", "any")],
    [Word("delicious", "any", "any", "any")],[Word("beautiful", "any", "any", "any")],
    [Word("interesting", "any", "any", "any")],[Word("important", "any", "any", "any")],
    [Word("happy", "any", "any", "any")],[Word("sad", "any", "any", "any")],
    [Word("fast", "any", "any", "any")],[Word("slow", "any", "any", "any")],
    [Word("heavy", "any", "any", "any")],[Word("light", "any", "any", "any")],
    [Word("young", "any", "any", "any")],[Word("old", "any", "any", "any")],
    [Word("rich", "any", "any", "any")],[Word("poor", "any", "any", "any")],
    [Word("strong", "any", "any", "any")],[Word("weak", "any", "any", "any")],
    [Word("friendly", "any", "any", "any")],[Word("angry", "any", "any", "any")],
    [Word("quiet", "any", "any", "any")],[Word("loud", "any", "any", "any")],
    [Word("clean", "any", "any", "any")],[Word("dirty", "any", "any", "any")],
    [Word("long", "any", "any", "any")],[Word("short", "any", "any", "any")],
    [Word("thick", "any", "any", "any")],[Word("thin", "any", "any", "any")],
    [Word("hot", "any", "any", "any")],[Word("cold", "any", "any", "any")],
    [Word("warm", "any", "any", "any")],[Word("cool", "any", "any", "any")],
    [Word("soft", "any", "any", "any")],[Word("hard", "any", "any", "any")],
    [Word("sharp", "any", "any", "any")],[Word("smooth", "any", "any", "any")],
    [Word("rough", "any", "any", "any")],[Word("expensive", "any", "any", "any")],
    [Word("cheap", "any", "any", "any")],[Word("sweet", "any", "any", "any")],
    [Word("sour", "any", "any", "any")],[Word("bitter", "any", "any", "any")],
    [Word("spicy", "any", "any", "any")],[Word("tall", "any", "any", "any")],
    [Word("short", "any", "any", "any")],[Word("early", "any", "any", "any")],
    [Word("late", "any", "any", "any")],[Word("kind", "any", "any", "any")],
    [Word("generous", "any", "any", "any")],[Word("selfish", "any", "any", "any")],
    [Word("brave", "any", "any", "any")],[Word("breathtaking", "any", "any", "any")],
    [Word("gorgeous", "any", "any", "any")],[Word("active", "any", "any", "any")],
    [Word("funny", "any", "any", "any")],[Word("serious", "any", "any", "any")],
    [Word("polite", "any", "any", "any")],[Word("rude", "any", "any", "any")],
    [Word("creative", "any", "any", "any")],[Word("boring", "any", "any", "any")],
    [Word("beautiful", "any", "any", "any")],[Word("ugly", "any", "any", "any")],
    [Word("pleasant", "any", "any", "any")],[Word("unpleasant", "any", "any", "any")],
    [Word("calm", "any", "any", "any")],[Word("nervous", "any", "any", "any")]
]

# Comparative adjectives (JJR)
JJR = [
    [Word("bigger", "any", "any", "any")],[Word("smaller", "any", "any", "any")],
    [Word("more delicious", "any", "any", "any")],[Word("more beautiful", "any", "any", "any")],
    [Word("more interesting", "any", "any", "any")],[Word("happier", "any", "any", "any")],
    [Word("sadder", "any", "any", "any")],[Word("faster", "any", "any", "any")],
    [Word("slower", "any", "any", "any")],[Word("heavier", "any", "any", "any")],
    [Word("lighter", "any", "any", "any")],[Word("younger", "any", "any", "any")],
    [Word("older", "any", "any", "any")],[Word("richer", "any", "any", "any")],
    [Word("poorer", "any", "any", "any")],[Word("stronger", "any", "any", "any")],
    [Word("weaker", "any", "any", "any")],[Word("friendlier", "any", "any", "any")],
    [Word("angrier", "any", "any", "any")],[Word("quieter", "any", "any", "any")],
    [Word("louder", "any", "any", "any")],[Word("cleaner", "any", "any", "any")],
    [Word("dirtier", "any", "any", "any")],[Word("longer", "any", "any", "any")],
    [Word("shorter", "any", "any", "any")],[Word("thicker", "any", "any", "any")],
    [Word("thinner", "any", "any", "any")],[Word("hotter", "any", "any", "any")],
    [Word("colder", "any", "any", "any")],[Word("warmer", "any", "any", "any")],
    [Word("cooler", "any", "any", "any")],[Word("softer", "any", "any", "any")],
    [Word("harder", "any", "any", "any")],[Word("sharper", "any", "any", "any")],
    [Word("smoother", "any", "any", "any")],[Word("rougher", "any", "any", "any")],
    [Word("more expensive", "any", "any", "any")],[Word("cheaper", "any", "any", "any")],
    [Word("sweeter", "any", "any", "any")],[Word("sourer", "any", "any", "any")],
    [Word("more bitter", "any", "any", "any")],[Word("spicier", "any", "any", "any")],
    [Word("taller", "any", "any", "any")],[Word("shorter", "any", "any", "any")],
    [Word("earlier", "any", "any", "any")],[Word("later", "any", "any", "any")],
    [Word("kinder", "any", "any", "any")],[Word("more generous", "any", "any", "any")],
    [Word("more selfish", "any", "any", "any")],[Word("braver", "any", "any", "any")],
    [Word("lazier", "any", "any", "any")],[Word("more active", "any", "any", "any")],
    [Word("funnier", "any", "any", "any")],[Word("more serious", "any", "any", "any")],
    [Word("more polite", "any", "any", "any")],[Word("ruder", "any", "any", "any")],
    [Word("more creative", "any", "any", "any")],[Word("more boring", "any", "any", "any")],
    [Word("more beautiful", "any", "any", "any")],[Word("uglier", "any", "any", "any")],
    [Word("more pleasant", "any", "any", "any")],[Word("more unpleasant", "any", "any", "any")],
    [Word("calmer", "any", "any", "any")],[Word("more nervous", "any", "any", "any")]
]

# Superlative adjectives (JJS)
JJS = [
    [Word("biggest", "any", "any", "any")],[Word("smallest", "any", "any", "any")],
    [Word("fastest", "any", "any", "any")],[Word("slowest", "any", "any", "any")],
    [Word("youngest", "any", "any", "any")],[Word("oldest", "any", "any", "any")],
    [Word("happiest", "any", "any", "any")],[Word("saddest", "any", "any", "any")],
    [Word("strongest", "any", "any", "any")],[Word("weakest", "any", "any", "any")],
    [Word("brightest", "any", "any", "any")],[Word("darkest", "any", "any", "any")],
    [Word("smartest", "any", "any", "any")],[Word("most delicious", "any", "any", "any")],
    [Word("most beautiful", "any", "any", "any")],[Word("most interesting", "any", "any", "any")],
    [Word("most important", "any", "any", "any")]
]

# Auxiliary Verbs (AUX)
AUX = [
    [Word("does", "any", "any", "present")],
    [Word("did", "any", "any", "past")],
    [Word("do", "any", "any", "any")],
    [Word("am", "any", "any", "present")],
    [Word("is", "any", "any", "present")],
    [Word("are", "any", "any", "present")]
]

# Negation (Neg)
Neg = [
    [Word("not", "any", "any", "any")]
]

# Do (DO)
DO = [
    [Word("do", "any", "any", "any")]
]

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
