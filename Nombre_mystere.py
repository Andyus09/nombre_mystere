import random



def nombre_mystere(nom):

    nbre_mystere = random.randrange(101)
    nbre_d_essaie = 5

    print()
    print("********** Jeu du nombre mystère **********")
    print()
    print(f"Bonjour {tonNom}! Vous avez droit a 5 essaies pour ce jeu.")

    while nbre_d_essaie >= 1 :
        
        choix_str = input("Entrez un nombre entre 0 et 100: ")
        
        # Input validation for a number between 0 and 100, inclusive
        if choix_str.isdigit():
            
            if int(choix_str) in range(101):
            
                choix = int(choix_str)
                print(choix)

                if choix < nbre_mystere:
                    print("Votre nombre est inferieur au nombre mystere")
                    nbre_d_essaie -=1
                    print(f"il vous reste {nbre_d_essaie} tentatives.")     
                    continue

                elif choix > nbre_mystere:
                    print("Votre nombre est superieur au nombre mystere")
                    nbre_d_essaie -=1
                    print(f"il vous reste {nbre_d_essaie} tentatives.")
                    continue

                else :
                    print(f"Bravo! Vous avez trouvé le nombre mystere qui est {nbre_mystere}.")
                    break
                    
            else:
                print("Entrez un nombre entre 0 et 100!")
                
        else:
            print("Entrez un nombre ! ")
            
        
            
    if nbre_d_essaie == 0:
        print("Vous avez perdu!!!")
        print(f"Le nombre mystère était {nbre_mystere}.")
        print("Voulez-vous recommencez?")
        recommencer = input("Oui où Non? ").capitalize()
        if recommencer == "Oui":
            print("Nouvelle partie...")
            nombre_mystere(tonNom)
            choix_str
        else: print("À bientot!")


tonNom = input("Entrée votre Nom: ").capitalize()
nombre_mystere(tonNom)
