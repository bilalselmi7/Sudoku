# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 16:19:02 2020

@author: Cheick KANOUTE et Bilal SELMI : TDO
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from ortools.sat.python import cp_model
import random 


#Selection du niveau
def Niveau ():
    print("1 : Très difficile")
    print("2 : Difficile")
    print("3 : Moyen")
    print("4 : Facile")
    print("5 : Débutant")
    entier = eval(input("Veuillez saisir un nombre entre 1 et 5 : "))
    print(entier)
    print("")
    print("Voici la grille avant l'ajout des valeurs en fonction du niveau souhaité")
    #while(entier!=1,2,3,4,5) <- ne fonctionne pas et ne sors jamais de la boucle           
    count=0 # count correspond au nombre de cases manquantes
    if(entier==1):
        count=64 
    if(entier==2):
        count = 55
    if(entier==3):
        count = 48
    if(entier==4):
        count=41
    if(entier==5):
        count=31
    return count

def SolutionSudoku(grille_preremplie):
    """Minimal CP-SAT example to showcase calling the solver."""
#Créer le modèle 
    modele=cp_model.CpModel()
# Creation des variables


    sudoku= [[modele.NewIntVar(1,9,'column: %i' %i) for i in range(9)] for j in range(9)]
    #sudoku=remplissage(modele,sudoku,sudoku)
    # Creation de contraintes

    #Contraintes sur les lignes

    for i in range(9):
        ligne=[]
        for j in range(9):
            ligne.append(sudoku[i][j])
            modele.AddAllDifferent(ligne)
    #Contraintes sur les colonnes
    
    for i in range(9):
        colonne=[]
        for j in range(9):
            colonne.append(sudoku[j][i])
            modele.AddAllDifferent(colonne)
        
    #Contraintes sur les carrés
    carre1=[]
    for k in range(3):
        for l in range(3):
            carre1.append(sudoku[k][l])
            modele.AddAllDifferent(carre1)
    carre2=[]
    for m in range(3,6):
        for n in range(3):
            carre2.append(sudoku[m][n])
            modele.AddAllDifferent(carre2)
    carre3=[]
    for o in range(6,9):
        for p in range(3):
            carre3.append(sudoku[o][p])
            modele.AddAllDifferent(carre3)
    carre4=[]
    for q in range(3):
        for r in range(3,6):
            carre4.append(sudoku[q][r])
            modele.AddAllDifferent(carre4)
    carre5=[]
    for s in range(3,6):
        for t in range(3,6):
            carre5.append(sudoku[s][t])
            modele.AddAllDifferent(carre5)
    carre6=[]
    for u in range(6,9):
        for v in range(3,6):
            carre6.append(sudoku[u][v])
            modele.AddAllDifferent(carre6)
    carre7=[]
    for w in range(3):
        for x in range(6,9):
            carre7.append(sudoku[w][x])
            modele.AddAllDifferent(carre7)
    carre8=[]
    for y in range(3,6):
        for z in range(6,9):
            carre8.append(sudoku[y][z])
            modele.AddAllDifferent(carre8)
    carre9=[]
    for a in range(6,9):
        for b in range(6,9):
            carre9.append(sudoku[a][b])
            modele.AddAllDifferent(carre9)
    
    #Contrainte sur la grille fournie
    for i in range(9):
        for j in range(9):
            if(grille_preremplie[i][j]!=0):
                modele.Add(grille_preremplie[i][j]==sudoku[i][j])




 # Creation du solver et solution.
    solver = cp_model.CpSolver()
    status = solver.Solve(modele)

    if status == cp_model.FEASIBLE:
        print("Faisable")
        for i in range(9):
            print("\n")
            for j in range(9):
                print(solver.Value(sudoku[i][j]), end = " | ")
          
    if status == cp_model.INFEASIBLE:
        print("Infeasible")
    
def Jeu(unegrille=None):
#Créer le modèle 
    modele=cp_model.CpModel()
# Creation des variables


    sudoku= [[modele.NewIntVar(1,9,'column: %i' %i) for i in range(9)] for j in range(9)]
    #sudoku=remplissage(modele,sudoku,sudoku)
    # Creation de contraintes

    #Contraintes sur les lignes

    for i in range(9):
        ligne=[]
        for j in range(9):
            ligne.append(sudoku[i][j])
            modele.AddAllDifferent(ligne)
    #Contraintes sur les colonnes
    
    for i in range(9):
        colonne=[]
        for j in range(9):
            colonne.append(sudoku[j][i])
            modele.AddAllDifferent(colonne)
        
    #Contraintes sur les carrés
    carre1=[]
    for k in range(3):
        for l in range(3):
            carre1.append(sudoku[k][l])
            modele.AddAllDifferent(carre1)
    carre2=[]
    for m in range(3,6):
        for n in range(3):
            carre2.append(sudoku[m][n])
            modele.AddAllDifferent(carre2)
    carre3=[]
    for o in range(6,9):
        for p in range(3):
            carre3.append(sudoku[o][p])
            modele.AddAllDifferent(carre3)
    carre4=[]
    for q in range(3):
        for r in range(3,6):
            carre4.append(sudoku[q][r])
            modele.AddAllDifferent(carre4)
    carre5=[]
    for s in range(3,6):
        for t in range(3,6):
            carre5.append(sudoku[s][t])
            modele.AddAllDifferent(carre5)
    carre6=[]
    for u in range(6,9):
        for v in range(3,6):
            carre6.append(sudoku[u][v])
            modele.AddAllDifferent(carre6)
    carre7=[]
    for w in range(3):
        for x in range(6,9):
            carre7.append(sudoku[w][x])
            modele.AddAllDifferent(carre7)
    carre8=[]
    for y in range(3,6):
        for z in range(6,9):
            carre8.append(sudoku[y][z])
            modele.AddAllDifferent(carre8)
    carre9=[]
    for a in range(6,9):
        for b in range(6,9):
            carre9.append(sudoku[a][b])
            modele.AddAllDifferent(carre9)
    
    #Contrainte sur la grille fournie
    if unegrille!=None:
        for i in range(9):
            for j in range(9):
                if(unegrille[i][j]!=0):
                    modele.Add(unegrille[i][j]==sudoku[i][j])


    
    
 # Creation du solver et solution.
    solver = cp_model.CpSolver()
    status = solver.Solve(modele)
    if unegrille!=None:
        if status == cp_model.FEASIBLE:
            count = Niveau()
            compteur = 0
            grilledebut = [[i for i in elm] for elm in sudoku] #grille qui prend les valeurs de la grille solution pour ne pas écraser les valeurs de la solution 
            while(compteur < count):
                ligne = random.randint(0,8)
                colonne = random.randint(0,8)
                if (grilledebut[ligne][colonne] != 0) : 
                    grilledebut[ligne][colonne] = 0
                    compteur += 1
                    
            print("Voici la grille de départ")
            for i in range (9):
                if i%3==0:
                    print("-------------------")
                for j in range (9): 
                    if j%3==0:
                        print("|",end="")
                    print(solver.Value(grilledebut[i][j]), end =" ") #il affiche les valeurs des variables avec les 0 qui répresentent les cases à compléter
                
                print("")
            solution=(input("Voulez vous une solution ? Si oui tapez 1.\nSi non tapez autre chose pour quitter le jeu.\n"))
            if solution=="1":
                print("")
                print("voici la grille résolue")
                for i in range (9):
                    if i%3==0:
                        print("-------------------")
                    for j in range (9): 
                        if j%3==0:
                            print("|",end="")
                        print(solver.Value(sudoku[i][j]), end =" ")
                    print("")
            else :
                print("Merci d'avoir joué, n'hésitez pas à revenir !")
                pass
                    
                        
         
    else:
        unegrille=[[0 for i in range(9)]for j in range(9)] #on crée un matrice 9X9 que de zéros 
        unegrille[0][0]=random.randint(0,9)  # On initialise 3 valeurs de la diagonale avec un random pour avoir de la diversité dans la géneration des grilles
        unegrille[4][4]=random.randint(0,9)
        unegrille[8][8]=random.randint(0,9)
        Jeu(unegrille) # On rappelle la méthode qui devrait à coup sûr être capable de résoudre la grille qui comportent 3 valeurs sur la diagonale et que des zéros sur les autres cases 
    
  

if __name__=='__main__':
    print("Vous allez jouer au Sudoku :\n")
    print("Choisissez un mode de difficulté\n")
    Jeu()
     