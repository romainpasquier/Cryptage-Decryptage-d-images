# Pour pouvoir bouger dans la clef, je mets ma clef sous forme de liste de longueur 24
def transpo_clef(ecrit):
    for i in range(len(ecrit)):
        ecrit[i] = int(ecrit[i])
    return ecrit