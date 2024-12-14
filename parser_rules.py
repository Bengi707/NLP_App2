# Non-terminal symbols (Penn Treebank tags)
non_terminals = ["S", "NP", "VP", "PP", "PRP", "VBP", "JJ", "NNS", "DT", "NN", "RB", "VB","EMP"]

# Terminals (words in our lexicon)
terminals = ["I", "enjoy", "historical", "novels", "the", "book", "a", "man", "will", "attend", "meeting", "tonight",
             "loud", "music", "do", "not"]

# Rules of the grammar (CFG in CNF)
R = {
    "S": [["NP", "VP"]],
    "NP": [["JJ", "NNS"], ["DT", "NN"], ["I"]],
    "VP": [["VBP", "NP"]],
    "PRP": [["I"]],
    "VBP": [["enjoy"]],
    "JJ": [["historical"]],
    "NNS": [["novels"]],
    "DT": [["the"], ["a"]],
    "NN": [["book"], ["man"]],
}


# Function to perform the CYK Algorithm
def cykParse(w):
    try:
        n = len(w)

        if n == 0:
            raise ValueError("Input sentence is empty.")

        # Validate that all words in the sentence are valid terminals
        for word in w:
            if word not in terminals:
                raise ValueError(f"Unexpected word in sentence: {word}")

        # Initialize the table
        T = [[set() for _ in range(n)] for _ in range(n)]

        # Fill in the table with terminals
        for j in range(n):
            for lhs, rule in R.items():
                for rhs in rule:
                    if len(rhs) == 1 and rhs[0] == w[j]:
                        T[j][j].add(lhs)

        # Fill in the table with non-terminals
        for i in range(j, -1, -1):
            for k in range(i, j):
                for lhs, rule in R.items():
                    for rhs in rule:
                        if len(rhs) == 2 and rhs[0] in T[i][k] and rhs[1] in T[k + 1][j]:
                            T[i][j].add(lhs)

        # Print the parse table
        print("\nCYK Parse Table:")
        for row in T:
            print(["{" + ", ".join(cell) + "}" if cell else "{}" for cell in row])

        # Check if 'S' is in the top-right cell
        if "S" in T[0][n - 1]:
            print("\nThe sentence is valid!")
        else:
            print("\nThe sentence is invalid!")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


# Driver Code
w = "I enjoy historical novels".split()
cykParse(w)
