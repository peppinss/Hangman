import random

def parolacorretta(scrambleword, lenword):
    test = ""
    for x in range(lenword):
        test += scrambleword[x]
    test = str(test)
    if test == word:
        return word
    else:
        return ""


def assegnazionelettere(lettera, scrambleword):
    test = 0
    while True:
        test = word.find(lettera, test)
        if test != -1:
            scrambleword[test] = lettera
        else:
            return scrambleword
        test += 1


def inserisci_lettera(anticheat):
    while True:
        checklettera = input("Inserisci una lettera oppure prova ad indovinare la parola\n")
        lenchecklettera = len(checklettera)
        if lenchecklettera <= 1 and lenchecklettera >= 0:
            return checklettera, anticheat
        if checklettera == word:
            return word
        if anticheat >= 5:
            return False
        if len(checklettera) > 2:
            print(f"La parola inserita non sembra essere corretta ti rimangono {5-anticheat} tentativi")
            anticheat += 1


def calcolo_lettere(lenword):
    scrableword = ""
    for x in range(lenword):
        scrableword += "_,"
    scrableword = scrableword.split(",")
    scrableword.pop(-1)
    return scrableword


#Script princiale

def main():
    global word
    word = random.choice(wordlist)
    x, y, z, anticheat = 0, 0, 0, 0
    lenword = len(word)
    debug = print(f"debug word = {word}")
    scrambleword = calcolo_lettere(lenword)
    while True:
        wipe
        print(f"Errori rimasti: {6 - x}\nPossibilita' di indovinare la parola rimaste {5 -anticheat}")
        print(f"{scrambleword} {lenword}")
        print(stage(x))
        lettera = inserisci_lettera(anticheat)
        if lettera is False:
            break
        anticheat = lettera[-1]
        lettera = str(lettera[-2])
        if lettera == word:
            return 1
        test2 = parolacorretta(scrambleword, lenword)
        if word.find(lettera) != -1 and test2.find(lettera) == -1:
            scrambleword = assegnazionelettere(lettera, scrambleword)
            if parolacorretta(scrambleword, lenword) == word:
                scrambleword = parolacorretta(scrambleword, lenword)
                break
        if x > 6 or anticheat > 5:
            break
        else:
            x += 1

    if scrambleword == word:
        return 1
    else:
        return 0






# parte 1
#inserisco un dizionario di parole


def genwordlist():
    inFile = open("wordlist.txt", mode="r", newline='\r\n')
    line = inFile.readline()
    wordlist = str.split(line)
    return wordlist
#Selezione ascii art


def stage(y):
    stages = ['''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    ''', '''
      +---+
      |   |
          |
          |
          |
          |
    =========
    ''']
    return stages[6 - y]
#Scegliere se il giocatore vuole continuare oppure no


def tryagain():
    while True:
        check = input("Vuoi giocare ancora Y N \n").lower()
        if check == "y":
            return 0
        if check == "n":
            return 1
        else:
            print("il valore inserito non sembra corretto riprova")


if __name__ == '__main__':
    wordlist = genwordlist()
    victory = 0
    lose = 0
    print("Benvenuto")
    while True:
        resoults = main()
        if resoults == 1:
            victory += 1
            print("Vittoria")
        else:
            lose += 1
            print("ritenta sarai piu' fortunato")
        print(f"Il tuo score attuale vittorie: {victory} sconfitte: {lose} partite giocate: {victory + lose}")
        tryagain1 = tryagain()
        if tryagain1 == 0:
            continue
        if tryagain1 == 1:
            print("Grazie per aver giocato")
            break

