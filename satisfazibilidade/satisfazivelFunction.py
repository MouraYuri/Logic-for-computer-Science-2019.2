from consequencia import consequencia

formula = [['p'], ['&'], [['~'], ['p']]]

def satisfazivel(formula):
    aux = [['~']]
    aux.append(formula)
    return (consequencia([], aux) == False)

print(satisfazivel(formula))