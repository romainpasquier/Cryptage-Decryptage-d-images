def somme(liste):
    _somme = 0
    for i in liste:
        _somme = _somme + i
    return _somme


def moyenne(liste):
    return somme(liste)/len(liste)
