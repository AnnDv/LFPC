import pandas as pd

rules = [
    'A a A',
    'B b B',
    'B b C',
    'A b B',
    'B a A',
    'C b B '
]


def getNFA(rules):
    nfa = {}
    for rule in rules:
        x = rule.split(' ')

        if not x[0] in nfa:
            nfa[x[0]] = {}

        if not x[1] in nfa[x[0]]:
            nfa[x[0]][x[1]] = ''

        nfa[x[0]][x[1]] += x[2]
    return nfa


def getStates(nfa):
    states = []
    for x in nfa:
        states.append(x)

    for x in nfa:
        for y in nfa[x]:
            if len(nfa[x][y]) > 1:
                if not nfa[x][y] in states:
                    states.append(nfa[x][y])
            else:
                if not nfa[x][y][0] in states:
                    states.append(nfa[x][y][0])
    return states


def getMethods(nfa):
    methods = []

    for x in nfa:
        for j in nfa[x]:
            if not j in methods:
                methods.append(j)

    return methods


def convertNFA2DFA(nfa, states, methods):
    dfa = nfa.copy()
    for s in states:
        if not s in dfa:
            separated = list(s)
            for m in methods:
                temp = []

                for sp in separated:
                    if m in dfa[sp]:
                        temp.append(dfa[sp][m])

                if not s in dfa:
                    dfa[s] = {}

                dfa[s][m] = ''.join(set(''.join(temp)))
                states.append(''.join(set(''.join(temp))))

    return dfa

print("NFA table")
nfa = getNFA(rules)
NFA = pd.DataFrame(nfa)
NFA = NFA.fillna("-")
print(NFA.transpose())

print("DFA table")
dfa = convertNFA2DFA(nfa, getStates(nfa), getMethods(nfa))
df = pd.DataFrame(dfa)
df = df.fillna("-")
print(df.transpose())