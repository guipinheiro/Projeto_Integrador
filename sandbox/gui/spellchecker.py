!pip install spellchecker


import pandas as pd
from spellchecker import SpellChecker


verbos = pd.read_csv('verbo_tempo.csv', sep=';')


spell = SpellChecker(language='pt')


lista_verbos_arrumados = []
for word in verbos['Verbo_test']:
    try:
        lista_verbos_arrumados.append(spell.correction(word))
    except:
        lista_verbos_arrumados.append(word)


dic_verbos_arrumados = dict(zip(verbos['Verbo_test'], lista_verbos_arrumados))