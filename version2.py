DT = [["that"], ["this"], ["a"], ["the"], ["an"], ["these"], ["those"]],

NN=  [
    ["book"], ["flight"], ["meal"], ["money"], ["present"], ["school"], ["music"], ["movie"],
    ["friend"], ["apple"], ["face"], ["market"], ["dog"], ["cat"], ["house"], ["car"], ["teacher"],
    ["child"], ["idea"], ["story"], ["game"], ["photo"], ["river"], ["city"], ["garden"], ["song"],
    ["phone"], ["computer"], ["table"], ["bottle"], ["shirt"], ["painting"]],

NNS= [
    ["novels"], ["friends"], ["flights"], ["schools"], ["presents"], ["meals"], ["books"],
    ["apples"], ["faces"], ["dogs"], ["cats"], ["houses"], ["cars"], ["teachers"], ["children"],
    ["ideas"], ["stories"], ["games"], ["photos"], ["rivers"], ["cities"], ["gardens"], ["songs"],
    ["phones"], ["computers"], ["tables"], ["bottles"], ["shirts"]],

VB= [
    ["prefer"], ["include"], ["eat"], ["take"], ["want"], ["watch"], ["spend"], ["enjoy"], ["book"],
    ["present"], ["build"], ["sing"], ["dance"], ["paint"], ["write"], ["call"], ["drive"], ["buy"],
    ["sell"], ["read"], ["open"], ["close"], ["fix"], ["carry"], ["create"], ["explore"], ["face"], ["book"]
],
# Past tense verbs
VBD= [
    ["bought"], ["helped"], ["watched"], ["ate"], ["took"], ["spent"], ["enjoyed"], ["booked"],
    ["presented"], ["went"], ["was"], ["were"], ["built"], ["sang"], ["danced"], ["painted"],
    ["wrote"], ["called"], ["drove"], ["sold"], ["read"], ["opened"], ["closed"], ["fixed"],
    ["carried"], ["created"], ["explored"], ["faced"], ["booked"]
],
# 3rd person singular present verbs
VBZ= [
    ["prefers"], ["includes"], ["eats"], ["takes"], ["spends"], ["watches"], ["enjoys"], ["books"],
    ["presents"], ["goes"], ["builds"], ["sings"], ["dances"], ["paints"], ["writes"], ["calls"],
    ["drives"], ["buys"], ["sells"], ["reads"], ["opens"], ["closes"], ["fixes"], ["carries"],
    ["creates"], ["explores"], ["faces"], ["books"]
],
# Non-3rd person singular present verbs
VBP= [
    ["prefer"], ["include"], ["eat"], ["take"], ["spend"], ["watch"], ["enjoy"], ["book"],
    ["present"], ["build"], ["sing"], ["dance"], ["paint"], ["write"], ["call"], ["drive"],
    ["buy"], ["sell"], ["read"], ["open"], ["close"], ["fix"], ["carry"], ["create"], ["explore"], ["face"]
],
# Personal pronouns
PRP= [["I"], ["she"], ["we"], ["you"], ["her"], ["he"], ["it"], ["they"], ["them"]],
NNP= [["Houston"], ["NWA"]],  # Singular proper nouns
# Prepositions
IN= [
    ["from"], ["to"], ["on"], ["near"], ["through"], ["with"], ["under"], ["over"], ["beside"],
    ["between"], ["before"], ["after"], ["inside"], ["outside"], ["around"], ["above"], ["below"]
],
# Adverbs
RB= [
    ["quickly"], ["slowly"], ["often"], ["always"], ["never"], ["here"], ["yesterday"],
    ["today"], ["tomorrow"], ["carefully"], ["happily"], ["sadly"], ["silently"], ["loudly"],
    ["angrily"], ["eagerly"]
],
# Modal verbs
MD= [["will"], ["can"], ["should"], ["would"], ["may"], ["might"], ["must"]],
VBG= [
    ["playing"], ["running"], ["watching"], ["painting"], ["calling"], ["helping"], ["working"], ["riding"], ["moving"],
    ["jumping"], ["cooking"], ["fighting"], ["dreaming"], ["dancing"], ["kissing"], ["planning"], ["visiting"],
    ["starting"], ["ending"], ["going"], ["eating"], ["spending"], ["enjoying"], ["taking"], ["including"],
    ["preferring"]
],
# Possible wh-words
Wh_Word= [
    ["what"], ["where"], ["when"], ["why"], ["how"]
],
JJ= [
    ["red"], ["blue"], ["big"], ["small"], ["delicious"], ["beautiful"], ["interesting"], ["important"], ["happy"],
    ["sad"], ["fast"], ["slow"], ["heavy"], ["light"], ["young"], ["old"], ["rich"], ["poor"], ["strong"], ["weak"],
    ["friendly"], ["angry"], ["quiet"], ["loud"], ["clean"], ["dirty"], ["long"], ["short"], ["thick"], ["thin"],
    ["hot"], ["cold"], ["warm"], ["cool"], ["soft"], ["hard"], ["sharp"], ["smooth"], ["rough"], ["expensive"],
    ["cheap"], ["sweet"], ["sour"], ["bitter"], ["spicy"], ["tall"], ["short"], ["early"], ["late"], ["kind"],
    ["generous"], ["selfish"], ["brave"], ["breathtaking"], ["gorgeous"], ["active"], ["funny"], ["serious"],
    ["polite"],
    ["rude"], ["creative"], ["boring"], ["beautiful"], ["ugly"], ["pleasant"], ["unpleasant"], ["calm"], ["nervous"]
],

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
],

JJS= [
    ["biggest"], ["smallest"], ["fastest"], ["slowest"], ["youngest"], ["oldest"], ["happiest"],
    ["saddest"], ["strongest"], ["weakest"], ["brightest"], ["darkest"], ["smartest"],
    ["most delicious"], ["most beautiful"], ["most interesting"], ["most important"]
],

AUX= [["does"], ["did"], ["do"], ["am"], ["is"], ["are"]],
Neg= [["not"]],
DO= [["do"]]



grammar_rules = {
    "S": [
        ["NP", "VP"],    # Declarative

        # Declarative Negation Rules
        ["X7", "VP"],    # Declarative with negation

        # VP : Imperative
        VB,  # Base form verb  ["VB"]
        VBD,  # Past tense verb ["VBD"]
        [VBZ[0], "NP"],  # 3rd person singular present verb + NP
        [VBP[0], "NP"],  # Non-3rd person singular present verb + NP
        [VBD[0], "NP"],  # Past tense verb + NP
        ["X1", "PP"],  # Base form verb + NP + PP
        ["VP", "PP"],  # VP + PP
        # Imperative sentence rule:
        [VB[0], "NP"],
        [AUX[0], VBG[0]],
        
        # Imperative Negation Rules
        ["X8",VB[0]],

        # Questions
        ["X4", "VP"],  # Yes/No Question: Modal verb + NP + VP
        ["X3", "X2"]  # Wh-Question: Wh-word + Modal verb + NP + VP

    ],

    "NP": [
        PRP[0],  # Pronoun  ["PRP"]
        NNP[0],  # Singular Proper Noun ["NNP"]
        [DT[0], "Nominal"]  # Determiner + Nominal
    ],

    "Nominal": [
        NN[0],  # Singular Noun ["NN"]
        NNS[0],  # Plural Noun   ["NNS"]
        ["Nominal", NN[0]],  # Nominal + Singular Noun
        ["Nominal", "PP"],  # Nominal + Prepositional Phrase
        [JJ[0], "Nominal"],  # Base Adjective + Nominal
        [JJR[0], "Nominal"],  # Comparative Adjective + Nominal
        [JJS[0], "Nominal"],  # Superlative Adjective + Nominal
        VBG[0] # Gerund as Nominal
    ],

    "VP": [
        # Declarative sentence rule:
        VB,  # Base form verb  ["VB"]
        VBD,  # Past tense verb ["VBD"]
        [VBZ[0], "NP"],  # 3rd person singular present verb + NP
        [VBP[0], "NP"],  # Non-3rd person singular present verb + NP
        [VBD[0], "NP"],  # Past tense verb + NP
        ["X1", "PP"],  # Base form verb + NP + PP
        ["VP", "PP"],  # VP + PP
        # Imperative sentence rule:
        [VB[0], "NP"],
        [AUX[0], VBG[0]],
    ],

    "X1":[
        [VB[0], "NP"],
    ],

    "X2":[
        ["NP", "VP"],
    ],

    "X3":[
        [Wh_Word[0], MD[0]],
    ],

    "X4":[
        [MD[0], "NP"],
    ],

    "X5": [
        [AUX[0],Neg[0]]
    ],

    "X6": [
        [MD[0],Neg[0]]
    ],

    "X7": [

        ["NP","X5"],
        ["NP","X6"],

    ],
    "X8": [
        [DO[0], Neg[0]]
    ],


    "PP": [
        [IN[0], "NP"]  # Preposition + NP
    ]

}


# Example test cases
test_sentences = [
    "I bought a book",
    "She enjoys the music",
    "We want a meal",
    "You watched a movie",
    "I was in the school"
]
