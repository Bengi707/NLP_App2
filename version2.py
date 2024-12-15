grammar_rules = {
    "S": [
        ["NP", "VP"],    # Declarative

        # VP : Imperative
        ["prefer"], ["include"], ["eat"], ["take"], ["want"], ["watch"], ["spend"], ["enjoy"], ["book"], ["present"],
        # Base form verb  ["VB"]
        ["bought"], ["helped"], ["watched"], ["ate"], ["took"], ["spent"], ["enjoyed"], ["booked"], ["presented"],
        ["went"], ["was"], ["were"],  # Past tense verb ["VBD"]
        ["VBZ", "NP"],  # 3rd person singular present verb + NP
        ["VBP", "NP"],  # Non-3rd person singular present verb + NP
        ["VBD", "NP"],  # Past tense verb + NP
        ["X1", "PP"],  # Base form verb + NP + PP
        ["VP", "PP"],  # VP + PP
        ["VB", "NP"],

        # Questions
        ["X4", "VP"],  # Yes/No Question: Modal verb + NP + VP
        ["X3", "X2"]  # Wh-Question: Wh-word + Modal verb + NP + VP

    ],

    "NP": [
        ["I"], ["she"], ["we"], ["you"], ["her"],  # Pronoun  ["PRP"]
        ["Houston"], ["NWA"],  # Singular Proper Noun ["NNP"]
        ["DT", "Nominal"]  # Determiner + Nominal
    ],

    "Nominal": [
        ["book"], ["flight"], ["meal"], ["money"], ["present"], ["school"], ["music"], ["movie"],  # Singular Noun ["NN"]
        ["novels"], ["friends"], ["flights"], ["schools"], ["presents"], ["meals"], ["books"],  # Plural Noun   ["NNS"]
        ["Nominal", "NN"],  # Nominal + Singular Noun
        ["Nominal", "PP"]  # Nominal + Prepositional Phrase
    ],

    "VP": [
        # Declarative sentence rule:
        ["prefer"], ["include"], ["eat"], ["take"], ["want"], ["watch"], ["spend"], ["enjoy"], ["book"], ["present"],  # Base form verb  ["VB"]
        ["bought"], ["helped"], ["watched"], ["ate"], ["took"], ["spent"], ["enjoyed"], ["booked"], ["presented"], ["went"], ["was"], ["were"],  # Past tense verb ["VBD"]
        ["VBZ", "NP"],  # 3rd person singular present verb + NP
        ["VBP", "NP"],  # Non-3rd person singular present verb + NP
        ["VBD", "NP"],  # Past tense verb + NP
        ["X1", "PP"],  # Base form verb + NP + PP
        ["VP", "PP"],  # VP + PP
        # Imperative sentence rule:
        ["VB", "NP"],
    ],

    "X1":[
        ["VB", "NP"],
    ],

    "X2":[
        ["NP", "VP"],
    ],

    "X3":[
        ["Wh-Word", "MD"],
    ],

    "X4":[
        ["MD", "NP"],
    ],

    "PP": [
        ["IN", "NP"]  # Preposition + NP
    ],

    "DT":[["that"], ["this"], ["a"], ["the"], ["an"]],
    "NN": [["book"], ["flight"], ["meal"], ["money"], ["present"], ["school"], ["music"], ["movie"], ["friend"], ["apple"], ["face"]],
    "NNS": [["novels"], ["friends"], ["flights"], ["schools"], ["presents"], ["meals"], ["books"], ["apples"], ["faces"]],
    "VB": [["prefer"], ["include"], ["eat"], ["take"], ["want"], ["watch"], ["spend"], ["enjoy"], ["book"], ["present"]],
    "VBD": [["bought"], ["helped"], ["watched"], ["ate"], ["took"], ["spent"], ["enjoyed"], ["booked"], ["presented"], ["went"], ["was"], ["were"] ],  # Past tense verbs
    "VBZ": [["prefers"], ["includes"], ["buys"], ["eats"], ["takes"], ["spends"], ["watches"], ["enjoys"], ["books"], ["presents"], ["goes"], ["faces"]],  # 3rd person singular present verbs
    "VBP": [["enjoy"], ["listen"], ["go"], ["see"]],  # Non-3rd person singular present verbs
    "PRP": [["I"], ["she"], ["we"], ["you"], ["her"]],  # Personal pronouns
    "NNP": [["Houston"], ["NWA"]],  # Singular proper nouns
    "IN": [["from"], ["to"], ["on"], ["near"], ["through"], ["with"], ["under"]],  # Prepositions
    "RB": [["quickly"], ["slowly"], ["often"], ["always"], ["never"], ["here"], ["yesterday"]], #Adverbs
    "MD": [["will"], ["can"], ["should"], ["would"], ["may"], ["might"], ["must"]], #Modal verbs
    "VBG": [["enjoying"], ["reading"], ["helping"], ["attending"], ["working"], ["eating"], ["enjoying"], ["watching"], ["taking"]],
    "Wh-Word": [
        ["what"], ["where"], ["when"], ["why"], ["how"]  # Possible wh-words
    ],
}


# Example test cases
test_sentences = [
    "I bought a book",
    "She enjoys the music",
    "We want a meal",
    "You watched a movie",
    "I was in the school"
]



