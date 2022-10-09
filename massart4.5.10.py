import random

Pierre = 0
Feuille = 1
Ciseaux = 2
MANCHE = 5

COUP = ('Pierre', 'Feuille', 'Ciseaux')


def bat(coup_1, coup_2):
    return coup_1 % 3 == (coup_2 + 1) % 3


def manche(pt):
    coup_j, coup_o = int(input()), random.randint(0 , 2)
    if bat(coup_j, coup_o):
        pt, message = pt + 1, "est battu par"
    elif coup_j == coup_o:
        message = "annule"
    else:
        pt, message = pt - 1, "bat"
    print(COUP[coup_o], message, COUP[coup_j], ':', pt)
    return pt

def jeu():
    pt = 0
    for i in range(MANCHE):
        pt = manche(pt)
    if pt > 0:
        message_final = "Gagné"
    elif pt == 0:
        message_final = "Nul"
    else:
        message_final = "Perdu"
    print(message_final)

s = int(input())
random.seed(s)

jeu()