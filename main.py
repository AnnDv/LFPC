grammar = [
    'S->aS',
    'S->bS',
    'S->cD',
    'D->dD',
    'D->bF',
    'D->a',
    'F->bS',
    'F->a'
]

def parseGrammar(grammar):

    finiteAutomaton = {}

    for grammarRules in grammar:
        rule = grammarRules.split('->')

        subGrammar = {
            0: list(rule[0])[0],
            1: list(rule[1])
        }

        if not subGrammar[0] in finiteAutomaton:
            finiteAutomaton[subGrammar[0]] = {}

        if len(subGrammar[1]) == 1:
            subGrammar[1].append('$')

        finiteAutomaton[subGrammar[0]][subGrammar[1][0]] = subGrammar[1][1]

    return finiteAutomaton


def testGrammar(fa, initial, final, inputWord):

    state = initial

    currword = ""
    print(state + "->")

    for character in inputWord:
        if state in fa and character in fa[state]:
            state = fa[state][character]
            currword += character
        else:
            return 'Is not matching the grammar'
    return state in final

finiteAutomaton = parseGrammar(grammar)
print('Non-Terminal: ' + ', '.join(finiteAutomaton) + '\n', 'Terminal: ' + ', '.join(grammar))

while True:
    print('Write a combination: ')
    inputWord = input()
    if inputWord == '':
        break
    print(testGrammar(finiteAutomaton, 'S', {'$'}, inputWord))
    break