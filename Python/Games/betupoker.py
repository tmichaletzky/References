import random

def getName():
    return input()

def getSecret(words):
    return random.choice(words)

def getWord(giveup, helpword):
    while True:
        word = input().lower()
        if word == giveup:
            return giveup
        elif word == helpword:
            return helpword
        elif len(word) == 5:
            return word
        print("Ötbetűs szavakat adj meg!")
        
def getMatches(guess, secret):
    return sum([1 for g, s in zip(guess, secret) if g == s])


words = ['bálna', 'csiga', 'faorr', 'tégla', 'szűrő', 'mobil', 'tükör', 'kölni', 'isten']

score = rounds = 0

giveup = 'giveup'
helpword = 'help'

print('''Betűpókert fogunk játszani.\nA játék során minden körben egy ötbetűs szóra fogok gondolni.\nA te feladatod, hogy kitaláld ezt a szót.\n
      Segítségképpen minden egyes tippedre meg fogom mondani, hogy hány betű (karakter) áll jó helyen.\n
      Például ha a "málna" szóra gondoltam, akkor a "bálna" tippre 4-et fogok mondani, míg a "pohár" tippre 0-t.\n''')

print("Hogyan szólíthatlak?")
name = getName()
print('Szervusz %s!\n' %(name))

wantToPlay = True

print('Segítség: ha beütöd a "giveup" szót, automatikusan feladod az adott kört,\na "help" szó beírásával pedig háromszor megadok neked segítségként egy betűt és a pozícióját.\n')
print('Kezdődjön a játék!\n')

while wantToPlay:

    secret = getSecret(words)
    rounds += 1
    
    guesses = helps = 0
    helpList = list(range(1,6))
    dontKnow = True
    won = False
    
    print('Gondoltam!\n')
    
    while dontKnow:
        print("Kérlek adj meg egy ötbetűs szót:")
        guess = getWord(giveup, helpword)
        if guess == giveup:
            dontKnow = False
        elif guess == helpword:
            if helps < 3:
                helps += 1
                ind = random.choice(helpList)
                helpList.remove(ind)
                print('A(z) %s-edik betű %s.' %(ind, secret[ind-1]))
            else:
                print("Elhasználtál négy segítséget, az utolsó betűt neked kell kitalálni!")
        else:
            guesses += 1
            matches = getMatches(guess, secret)
            if matches == 5:
                score += 1
                dontKnow = False
                won = True
            else:
                print("%s betű van jó helyen." %(matches))
       
    if won:
        print('Gratulálok, %s tipp után és %s segítséggel kitaláltad a szót, %s!' %(guesses, helps, name))
    print('A(z) %s szóra gondoltam.' %(secret))
    
    print("Szeretnél még egyet játszani, %s?" %(name))
    if not input().lower().startswith('i'):
        wantToPlay = False
    else:
        print('Kiváló ötlet, játszunk még egyet!\n')

print('%s körből %s-ször kitaláltad. Gratulálok!\n' %(rounds, score))
print('Köszönöm, hogy velem játszottál, %s, legyen szép napod!' %(name))
       
    
        
           


