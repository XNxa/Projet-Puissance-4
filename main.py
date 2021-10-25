# -*- coding: utf-8 -*-

import outilsp4 as f

taille=f.dim_grille()
N=f.nbr_pion(taille)
grille = f.newG(taille)
print("Joueur 1, ton pion est X.\nJoueur 2, le tiens sera 0, bon jeu !")
if f.choixAdv()==False:
  while(True):
      f.affiche(grille, taille)
      f.joue(1, f.quelleCol(1, grille,taille), grille,taille)
      if (f.victoire(grille,taille,N)[0]):
          break
      f.affiche(grille, taille)
      f.joue(2, f.quelleCol(2,grille,taille), grille,taille)
      if (f.victoire(grille,taille,N)[0]):
          break
      
else:
  while(True):
      f.affiche(grille, taille)
      f.joue(1, f.quelleCol(1, grille,taille), grille,taille)
      if (f.victoire(grille,taille,N)[0]):
          break
      vic1=f.testVictoire(grille,taille,N,1)
      vic2=f.testVictoire(grille,taille,N,2)
      if vic2!=-1:
        f.joue(2,f.nToCol(vic2),grille,taille)
        if (f.victoire(grille,taille,N)[0]):
              break
      elif vic1!=-1:
        f.joue(2,f.nToCol(vic1),grille,taille)
        if (f.victoire(grille,taille,N)[0]):
              break
      else:
        f.joue(2, f.quelleColIA(grille,taille), grille,taille)
        if (f.victoire(grille,taille,N)[0]):
              break

f.affiche(grille, taille)
a = f.victoire(grille,taille,N)[1]
print("Fin du jeu :")
if (a == 0):
    print("Match Nul")
else:
    print("Victoire du joueur {} ! Félicitations".format(a))