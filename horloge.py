import time

heure_actuelle = time.localtime()[3:6]  # Obtenir l'heure actuelle
alarme = None  # Aucune alarme par défaut

def afficher_heure(heure):
    print("{:02d}:{:02d}:{:02d}".format(heure[0], heure[1], heure[2]), end='\r')

def regler_alarme():
    heures = int(input("Réglez l'heure de l'alarme (0-23): "))
    minutes = int(input("Réglez les minutes de l'alarme (0-59): "))
    secondes = int(input("Réglez les secondes de l'alarme (0-59): "))
    return heures, minutes, secondes

def verifier_alarme(heure_actuelle, heure_alarme):
    return heure_actuelle == heure_alarme

try:
    # Régler l'alarme au début
    alarme = regler_alarme()

    while True:
        heure_actuelle = time.localtime()[3:6]  # Actualiser l'heure actuelle
        afficher_heure(heure_actuelle)
        
        # Vérifier l'alarme
        if verifier_alarme(heure_actuelle, alarme):
            print("\nDING DONG l'arlame sonne")
            break  # Sortir de la boucle lorsque l'alarme se déclenche

        time.sleep(1)  # Attendre une seconde

except KeyboardInterrupt:
    print("\nArrêt du programme.")
