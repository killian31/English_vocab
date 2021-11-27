import os
import random

pwd = os.getcwd() #set the present working directory

#on récupère les mots à partir du fichier
file_name = "/words.txt"
with open(pwd + file_name, 'r') as f:
    text = f.readlines()

dico = {}

for trad in text:
    a = trad.split(':')
    dico[a[0].strip()] = a[1].strip()

def train(dico=dico):

    while len(dico) > 0:
        print('*'*35)
        print('Mots restants :', len(dico))
        traduction = random.choice(list(dico.items()))
        ans = input(f'Traduire : {traduction[0]}\nAppuyez sur Entrée pour voir la réponse : ')
        if a != '':
            print('Traduction :', traduction[1])
            del dico[traduction[0]]
        else:
            print('Bye')
            break
        print('*'*35)
    print('Entraînement terminé.')
    
train()