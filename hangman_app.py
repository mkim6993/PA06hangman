"""
   hangman_app.py is an app for playing hangman in the terminal
   it is also used as a module in the hangman_webapp flask app
"""
from random import randint
import math
wordList = [
"euouae","exodus","faking","fishhook","fixable","fjord","flapjack","flopping","fluffiness",
"flyby","foxglove","frazzled","frizzled","fuchsia","funny","gabby","galaxy","galvanize",
"gazebo","giaour","gizmo","glowworm","glyph","gnarly","gnostic","gossip","grogginess",
"haiku","haphazard","hyphen","iatrogenic","icebox","injury","ivory","ivy","jackpot"
    ]
wordListLength = len(wordList)


def generate_random_word():
   """ read a list of words from a file and pick a random one to return """
   return "unimplemented"

def play_hangman():
    while True:
        gameList = []
        word = wordList[randint(0,wordListLength-1)]
        wordLength = len(word)
        wordinList = list(word)
        choicesLeft = wordLength
        wordListCopy = []

        for i in word:
            wordListCopy.append(i)

        for i in word:
            gameList.append("-")

        while True:
            if choicesLeft == 0:
                print("you lose...")
                break

            print("----------------")
            print(gameList)
            print(str(choicesLeft)+" choices left")
            answer = input("pick a letter: ")
            if answer in word:
                for i in wordinList:
                    if i == answer:
                        posInList = wordinList.index(answer)
                        gameList[posInList] = answer
                        wordinList[posInList] = "/"
    
                    if gameList == wordListCopy:
                        print("great you won...")
                        break
            else:
                choicesLeft -= 1
        again = input("play again? (y or n) ")
        if again == "y":
            continue
        else:
            break






if __name__ == '__main__':
    play_hangman()
