from Temps.Temps_tab import moyenne_temps


def decrypte_tab(x, n):
    tab = []
    for i in range(1, x+1):
        tps = moyenne_temps(i, n)
        tab.append(tps)
    return tab

