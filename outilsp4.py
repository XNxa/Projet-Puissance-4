# -*- coding: utf-8 -*-
from random import randint
from copy import deepcopy

def testVictoire(grille, taille, N, joueur):
    """Test si le joueur peut gagner au tour suivant et renvoi le numéro de la colonne si jamais c'est le cas"""
    for i in range(taille[0]):
      if hauteur(nToCol(i),grille,taille)<taille[1]:
        grilleTemp=deepcopy(grille)
        joue(joueur,nToCol(i),grilleTemp,taille)
        if victoire(grilleTemp,taille,N)==(True,joueur):
          return i
    return -1

def choixAdv():
    """Permet de demander a l'utilisateur si il veut jouer seul ou a deux"""
    rep=input("Souhaitez vous jouer contre l'ordinateur?(o/n)")
    while rep!='o' and rep!='n':
      rep=input("Souhaitez vous jouer contre l'ordinateur?(o/n)")
    if rep=='o':
      return True
    return False

def affiche(grille, taille):
    """affiche la grille de jeu"""
    print("\n ", end="")
    for i in range(taille[0]):
        print(" -", end="")
    print("")
    for i in range(taille[1]-1, -1, -1 ):
        ligne = ""
        for k in range(taille[0]):
            ligne += " " +grille[k + i*taille[0]]
        print("|" + ligne + " |")
    print(" ", end="")
    for i in range(taille[0]):
        print(" -", end="")
    print("\n ", end="")
    for i in range(taille[0]):
        print(" {}".format(nToCol(i)), end="")
    print("")

def dim_grille():
    """Demande a l'utilisateur la taille de la grille de Jeu"""
    x=input("Donnez le nombre de colonnes de la grille : ")

    while x not in [str(i) for i in range(3, 27)]:
        x=input("Donnez le nombre de colonnes de la grille (entre 3 et 26): ")
    
    y=input("Donnez le nombre de lignes de la grille : ")
    while y not in [str(i) for i in range(3, 27)]:
        y=input("Donnez le nombre de lignes de la grille (entre 3 et 26): ")
    
    return [int(x),int(y)]
  
def nbr_pion(taille):
    """Demande a l'utilisateur le nombre N de pions a aligner pour gagner """
    N=input("Donnez le nombre de pions à aligner pour gagner : ")

    while N.isnumeric()==False:
        N=input("Donnez le nombre de pions à aligner pour gagner (entre 2 et {}): ".format(min(taille[0],taille[1])))
        
    while int(N)<=1 or int(N)>min(taille[0],taille[1]):
      N=input("Donnez le nombre de pions à aligner pour gagner (entre 2 et {}): ".format(min(taille[0],taille[1])))
      
      while N.isnumeric()==False:
        N=input("Donnez le nombre de pions à aligner pour gagner (entre 2 et {}): ".format(min(taille[0],taille[1])))

    return (int(N))
  
def pion(joueur):
    """prend le numéro du joueur et renvoi son pion (str)"""
    return {1: "X", 2: "O"}[joueur]

def nToCol(colonne):
    """prend le numéro de la colonne et renvoi son char"""
    return list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")[colonne]

def var(colonne):
    """prend le char de la colonne et renvoi le numéro"""
    return (list("ABCDEFGHIJKLMNOPQRSTUVWXYZ").index(colonne))

def coord1to2(N, taille):
    return (N % taille[0], N//taille[0])

def coord2to1(x, y, taille):
    return y*taille[0]+x

def newG(taille):
    """crée une grille d'une taille donnée [c,l]"""
    return [" " for i in range(taille[0]*taille[1])]

def hauteur(c, grille,taille):
    """prend en param la colonne (char) la grille et sa taille et renvoi la hauteur de la colonne precisée """
    c = var(c)
    h = 0
    for i in range(taille[1]):
        if grille[coord2to1(c, i,taille)] == " ":
            break
        else:
            h += 1
    return h

def quelleCol(joueur, grille,taille):
    """Demande a l'utilisateur dans quelle colonne il veut jouer"""
    while True:
        rep = str(input("Joueur {} : Quelle Colonne voulez vous poser pion ?".format(str(joueur))))
        rep = rep.upper()

        if rep in list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")[:taille[0]]:
            if hauteur(rep, grille,taille) < taille[1]:
                return rep
            else:
               print("Cette colonne est deja pleine ...")
        else:
            print("Merci d'utiliser une lettre correspondant a une colonne")

def quelleColIA(grille,taille):
    """Donne une valeur aleatoire de colonne dans laquelle il est possible de placer un pion"""
    while True:
      rep=randint(0,taille[0]-1)
      if hauteur(nToCol(rep), grille,taille) < taille[1]:
          return nToCol(rep)

def posepion(j, N, grille):
    """Place un pion du joueur j a la position N dans la grille"""
    grille[N] = pion(j)

def joue(j, c, grille,taille):
    """Pose un pion du joueur j """
    posepion(j, coord2to1(var(c), hauteur(c, grille,taille),taille), grille)

def row(grille,N,taille):
    """Renvoi une liste de toutes les combinaisions de N pions en ligne possible"""
    liste = []
    for i in range(taille[0]-N+1):
        for j in range(taille[1]):
            coef = coord2to1(i, j,taille)
            liste.append("".join(grille[coef: coef+N]))
    return liste

def col(grille,N,taille):
    """Renvoi une liste de toutes les combinaisions de N pions en colonne possible"""
    liste = []
    for i in range(taille[0]):
        for j in range(taille[1]-N+1):
            coef = coord2to1(i, j,taille)
            liste.append("".join(grille[coef: coef+((N-1)*taille[0]+1): taille[0]]))
    return liste

def diag(grille,N,taille):
    """Renvoi une liste de toutes les combinaisions de N pions en diagonal possible"""
    liste = []
    for i in range(taille[0]-N+1):
        for j in range(N-1):
            coef = coord2to1(i, j,taille)
            liste.append("".join(grille[coef: coef+((N-1)*(taille[0]+1)+1): taille[0]+1]))
    for i in range(taille[1]-N+1, taille[0]):
        for j in range(N-1):
            coef = coord2to1(i, j,taille)
            liste.append("".join(grille[coef: coef+((N-1)*(taille[0]-1)+1): taille[0]-1]))
    return liste

def victoire(grille,taille,N):
    """Verifie si il y a un alignment de N pion dans la grille et pour quel joueur"""
    combinaison = []
    for i in col(grille,N,taille)+row(grille,N,taille)+diag(grille,N,taille):
        
      if ' ' not in i and "X" not in i:
          combinaison.append(i[0])
        
      elif ' ' not in i and "O" not in i:
          combinaison.append(i[0])


    if "O" in combinaison and "X" in combinaison:
            print("ERREUR : Fonction Victoire")
            return(True, 0)

    elif "X" in combinaison :
        return(True, 1)
    
    elif "O" in combinaison :
        return(True, 2)
    
    if " " not in grille:
        return(True, 0)
        
    return(False, 0)

if __name__== "__main__":
    import random
    print("Test des fonctions :\n_______________\n")

    #1
    print("Test de la fonction affiche(grille, taille) : ")
    grille = ["X", " ", "X", " ", " ", " ", "O", " ", "O"]
    print("Attendu : grille de 3x3 avec deux croix dans les coins inferieurs\net deux cercles dans les coins superieurs\nResultat :")
    affiche(grille, [3,3])

    #2
    print("\nTest de la fonction pion avec le joueur 1 : attendu 'X':")
    test = pion(1)
    print("pion(1) = '{}'".format(test))
    if test == 'X' :
        print("OK")
    else :
        print("NOK")
    
    #3
    print("\nTest de la fonction var avec la colonne Z : attendu 25:")
    test = var('Z')
    print("var('Z') = {}".format(test))
    if test == 25 :
        print("OK")
    else :
        print("NOK")
    
    #3
    print("\nTest de la fonction coord1to2 avec une grille [7,6] avec N=0 , N=29 et N=41 : \nattendu (0,0); (1, 4); (6,5):")
    test = coord1to2(0,[7,6])
    test2 = coord1to2(29,[7,6])
    test3 = coord1to2(41,[7,6])
    print("coord1to2(0,[7,6]) = {}\ncoord1to2(29,[7,6]) = {}\ncoord1to2(41,[7,6]) = {}".format(test, test2, test3))
    if test == (0,0) and test2 == (1, 4) and test3 == (6,5):
        print("OK")
    else :
        print("NOK")
    
    #4
    print("\nTest de la fonction coord2to1 avec une grille [7,6] avec (0,0); (1, 4); (6,5) :\nattendu 0 , 29 et 41 : ")
    test = coord2to1(0, 0,[7,6])
    test2 = coord2to1(1, 4,[7,6])
    test3 = coord2to1(6, 5,[7,6])
    print("coord2to1(0, 0,[7,6]) = {}\ncoord2to1(1, 4,[7,6]) = {}\ncoord2to1(6, 5,[7,6]) = {}".format(test, test2, test3))
    if test == 0 and test2 == 29 and test3 == 41:
        print("OK")
    else :
        print("NOK")
    
    #5
    print("\nTest de la fonction newG avec une grille [26,26] : \nattendu : liste de 676 element :' ' ")
    g = newG([26,26])
    s = len(g)
    print("Grille de {} élements '{}'".format(s, g[random.randint(0, 600)]))
    if s == 676 and g[random.randint(0, 600)] == ' ':
        print("OK")
    else :
        print("NOK")
    
    #6
    print("\nTest de la fonction hauteur avec une grille 3x3 colonne C: attendu 2:")
    grille =["X", "X", "O", "X", "X", "X", " ", " ", " "]
    test = hauteur('C', grille,[3,3])
    print("hauteur('C', grille,[3,3]) = {}".format(test))
    if test == 2 :
        print("OK")
    else :
        print("NOK")
    
    #7
    print("\nTest de la fonction quelleCol directement lors de l'execution du programe")
    print("Protocole : \nAppuyer sur la touche m : \nAttendu : demande de retaper sur une touche")
    print("Appuyer sur la touche A jusqu'a remplir la colonne puis reappuyer sur A : \nAttendu : Erreur : colonne pleine demande de rejouer")
    print("OK")
    
    #8
    print("\nTest de la fonction posepion a la 29e place avec le joueur2:\nAttendu : pion Rond a la colonne B en 5e ligne")
    grille = newG([7,10])
    posepion(2, 29, grille)
    print("posepion(2, 29, grille) => grille[29] = '{}'".format(grille[29]))
    affiche(grille,[7,10])
    if grille[29]=="O" :
        print("OK")
    else :
        print("NOK")
    
    #9
    print("\nTest de la fonction joue 2 fois en colonne B avec joueur2 sur une grille 10x10:\nAttendu : pion Rond a la colonne B 1ere et 2e lignes")
    grille = newG([10,10])
    joue(2, 'B', grille,[10,10])
    joue(2, 'B', grille,[10,10])
    print("joue(2, 'B', grille) => grille[1] = '{}'".format(grille[1]))
    affiche(grille,[10,10])
    if grille[1]=="O" and grille[11]=="O":
        print("OK")
    else :
        print("NOK")
    
    #10
    print("\nTest de la fonction row avec la grille de l'exemple 3 du sujet:\nAttendu : Liste de 24 chaines dont : 'XOOO', 'OOOX', 'OOXX'")
    grille =["X","O","O","O","X","X"," "," ","O","X","X","O"," "," "," "," ","X","O","X"," "," "," "," ","O"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]
    print("row(grille) --> {}".format(row(grille,4,[7,6])))
    if len(row(grille,4,[7,6]))==24:
        print("OK")
    else :
        print("NOK")
    
    #11
    print("\nTest de la fonction col avec la grille de l'exemple 3 du sujet:\nAttendu : Liste de 21 chaines dont : 'X   ', 'OXXO' ")
    grille =["X","O","O","O","X","X"," "," ","O","X","X","O"," "," "," "," ","X","O","X"," "," "," "," ","O"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]
    print("col(grille) --> {}".format(col(grille,4,[7,6])))
    if len(col(grille,4,[7,6]))==21:
        print("OK")
    else :
        print("NOK")
        
    #12
    print("\nTest de la fonction diag avec la grille de l'exemple 3 du sujet:\nAttendu : Liste de 24 chaines dont : 'XOX ', 'OXO ', 'OXX '")
    grille =["X","O","O","O","X","X"," "," ","O","X","X","O"," "," "," "," ","X","O","X"," "," "," "," ","O"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]
    print("diag(grille) --> {}".format(diag(grille,4,[7,6],)))
    if len(diag(grille,4,[7,6]))==24:
        print("OK")
    else :
        print("NOK")

    #13
    print("\nTest de la fonction Victoire avec 3 grilles differentes: \nattendu : grille 1 : joueur1 gagne(True, 1) avec 5 pions alignés, grille 2: la partie continue(False, 0), grille 3 match nul(True, 0)")
    grille1 = ['X', 'X', 'X', 'X', 'X', ' ', ' ', 'O', 'O', 'O', ' ', ' ', ' ', ' ', 'X', 'X', 'X', ' ', ' ', ' ', ' ', 'O', 'O', 'O', ' ', ' ', ' ', ' ', 'X', 'X', 'X', ' ', ' ', ' ', ' ', 'O', 'O', 'O', ' ', ' ', ' ', ' ']
    grille2 = ['X', 'X', ' ', 'X', ' ', ' ', ' ', 'O', 'O', 'O', ' ', ' ', ' ', ' ', 'X', 'X', 'X', ' ', ' ', ' ', ' ', 'O', 'O', 'O', ' ', ' ', ' ', ' ', 'X', 'X', 'X', ' ', ' ', ' ', ' ', 'O', 'O', 'O', ' ', ' ', ' ', ' ']
    grille3 = ['X', 'X', 'X', 'O', 'O', 'O', 'X', 'O', 'O', 'O', 'X', 'X', 'X', 'O', 'X', 'X', 'X', 'O', 'O', 'O', 'X', 'O', 'O', 'O', 'X', 'X', 'X', 'O', 'X', 'X', 'X', 'O', 'O', 'O', 'X', 'O', 'O', 'O', 'X', 'X', 'X', 'O']
    print("victoire(grille1) = {}\nvictoire(grille2) = {}\nvictoire(grille3) = {}".format(victoire(grille1,[7,6],5),victoire(grille2,[7,6],4),victoire(grille3,[7,6],4)))
    if victoire(grille1,[7,6],5) == (True, 1) and victoire(grille2,[7,6],4) == (False, 0) and victoire(grille3,[7,6],4) == (True, 0) :
        print("OK")
    else :
        print("NOK")
    
    #14
    print("\nTest des fonction dim_grille et nbr_pion directement lors de l'éxecution du programme")
    print("Protocole: \nEntrez: \n-n'importe quel str ou nombre non entier \n-pour dim_grille un entier inférieur à 3 ou supérieur à 26 \n-pour nbr_pion un entier supérieur à la dimension minimal de la grille ou inférieur à 2\n Attendu: Demande de retaper une touche")
    print('OK')

    #15
    print("Test de la fonction testVictoire avec 2 grilles\nAttendus grille 1:\n  -Joueur 1 peut gagner en jouant dans la colonne d\n  -Joueur 2 peut gagner en jouant dans le colonne a\nAttendus grille 2:\n  -Aucun joueur ne peut gagner")
    grilletest1=['X', 'X', 'X', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'O', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'O', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'O', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    grilletest2=['X', 'O', 'X', 'O', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    print("Grille 1", end="")
    affiche(grilletest1, [10, 10])
    print("Grille 2", end="")
    affiche(grilletest2, [4,4])

    if testVictoire(grilletest1,[10,10],4,1)==3:
      if testVictoire(grilletest1,[10,10],4,2)==0:
        if testVictoire(grilletest2,[4,4],3,2)==testVictoire(grilletest2,[4,4],3,1)==-1:
          print('OK')

    print("\n__________________\nFin des Tests !")