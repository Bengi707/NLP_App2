grammar_rules = {
    "S": [
        ["NP", "VP"]    # Declarative
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
        ["prefer"], ["include"], ["eat"], ["take"], ["want"], ["watch"], ["spend"], ["enjoy"], ["book"], ["present"],  # Base form verb  ["VB"]
        ["bought"], ["helped"], ["watched"], ["ate"], ["took"], ["spent"], ["enjoyed"], ["booked"], ["presented"], ["went"], ["was"], ["were"],  # Past tense verb ["VBD"]
        ["VBZ", "NP"],  # 3rd person singular present verb + NP
        ["VBP", "NP"],  # Non-3rd person singular present verb + NP
        ["VBD", "NP"],  # Past tense verb + NP
        ["VB", "NP", "PP"],  # Base form verb + NP + PP !!!!!!!
        ["VP", "PP"]  # VP + PP
    ],

    "PP": [
        ["IN", "NP"]  # Preposition + NP
    ],

    "DT":[["that"], ["this"], ["a"], ["the"], ["an"]],
    "NN": [["book"], ["flight"], ["meal"], ["money"], ["present"], ["school"], ["music"], ["movie"], ["friend"]],
    "NNS": [["novels"], ["friends"], ["flights"], ["schools"], ["presents"], ["meals"], ["books"]],
    "VB": [["prefer"], ["include"], ["eat"], ["take"], ["want"], ["watch"], ["spend"], ["enjoy"], ["book"], ["present"]],
    "VBD": [["bought"], ["helped"], ["watched"], ["ate"], ["took"], ["spent"], ["enjoyed"], ["booked"], ["presented"], ["went"], ["was"], ["were"] ],  # Past tense verbs
    "VBZ": [["prefers"], ["includes"], ["buys"], ["eats"], ["takes"], ["spends"], ["watches"], ["enjoys"], ["books"], ["presents"], ["goes"]],  # 3rd person singular present verbs
    "VBP": [["enjoy"], ["listen"], ["go"], ["see"]],  # Non-3rd person singular present verbs
    "PRP": [["I"], ["she"], ["we"], ["you"], ["her"]],  # Personal pronouns
    "NNP": [["Houston"], ["NWA"]],  # Singular proper nouns
    "IN": [["from"], ["to"], ["on"], ["near"], ["through"], ["with"], ["under"]],  # Prepositions
    "RB": [["quickly"], ["slowly"], ["often"], ["always"], ["never"], ["here"], ["yesterday"]], #Adverbs
    "MD": [["will"], ["can"], ["should"], ["would"], ["may"], ["might"], ["must"]], #Modal verbs
    "VBG": [["enjoying"], ["reading"], ["helping"], ["attending"], ["working"], ["eating"], ["enjoying"], ["watching"], ["taking"]],

}


# Example test cases
test_sentences = [
    "I bought a book",
    "She enjoys the music",
    "We want a meal",
    "You watched a movie",
    "I was in the school"
]



