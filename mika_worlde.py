import random

# woordenlijst
woordlijst = ["appel", "besje", "kersen", "druif", "citroen", "mango", "meloen", "perzik"]

def kies_willekeurig_woord(woordlijst):
    return random.choice(woordlijst).lower()

def geef_feedback(gok, doelwoord):
    feedback = ["_"] * 5
    gok_letter_telling = {}
    doelwoord_letter_telling = {}
    
    # Eerste ronde: Vind correcte letters op de juiste positie
    for i in range(5):
        if gok[i] == doelwoord[i]:
            feedback[i] = 'G'  # Groen
        else:
            gok_letter_telling[gok[i]] = gok_letter_telling.get(gok[i], 0) + 1
            doelwoord_letter_telling[doelwoord[i]] = doelwoord_letter_telling.get(doelwoord[i], 0) + 1
    
    # Tweede ronde: Vind correcte letters op de verkeerde positie
    for i in range(5):
        if feedback[i] == '_':  # Alleen letters controleren die nog niet groen zijn
            if gok[i] in doelwoord and gok_letter_telling[gok[i]] <= doelwoord_letter_telling.get(gok[i], 0):
                feedback[i] = 'G'  # Geel
                doelwoord_letter_telling[gok[i]] -= 1  # Een van de beschikbare letters gebruiken
            else:
                feedback[i] = 'Z'  # Grijs (Zwart)
    
    return ''.join(feedback)

def toon_ascii_kunst():
    ascii_kunst = """
#     #                         #     #                                    
##   ## # #    #   ##           #  #  #  ####  #####  #      #####  ###### 
# # # # # #   #   #  #          #  #  # #    # #    # #      #    # #      
#  #  # # ####   #    #         #  #  # #    # #    # #      #    # #####  
#     # # #  #   ######         #  #  # #    # #####  #      #    # #      
#     # # #   #  #    #         #  #  # #    # #   #  #      #    # #      
#     # # #    # #    #          ## ##   ####  #    # ###### #####  ###### 
                        #######                                            
    """
    print(ascii_kunst)

def mika_wordle(woordlijst):
    toon_ascii_kunst()
    doelwoord = kies_willekeurig_woord(woordlijst)
    pogingen = 6
    print("Welkom bij Wordle! Raad het 5-letter woord.")
    
    for poging in range(pogingen):
        while True:
            gok = input(f"Poging {poging + 1}/{pogingen}: ").lower()
            if len(gok) == 5 and gok.isalpha():
                break
            else:
                print("Ongeldige invoer. Voer een 5-letter woord in.")
        
        feedback = geef_feedback(gok, doelwoord)
        print("Feedback:", feedback)
        
        if gok == doelwoord:
            print("Gefeliciteerd! Je hebt het woord geraden.")
            return
    
    print(f"Helaas, je hebt al je pogingen gebruikt. Het woord was: {doelwoord}")

# Start het spel
mika_wordle(woordlijst)
