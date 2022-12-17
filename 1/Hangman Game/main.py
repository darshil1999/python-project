import random
import time

print("Welcome to the Game")
name = input("Enter your name: ")
print("Hello " + name + "! Good luck with your game!")
time.sleep(3)
print("The game is about to start...")
time.sleep(2)


def main():
    global count
    global display
    global word
    global already_guess
    global length
    global play_game
    
    words_to_guess = ['october','border','day','image','whatsapp','instagram','facebook','google','kids','twitter','human','doll','panda']
    word = random.choice(words_to_guess)
    length = len(word)
    count= 0
    display = '_' * length
    already_guess = []
    play_game = ""
    
def play_loop():
    global play_game
    play_game = input("Do you want to play this game again? y = yes, n = no \n")
    while play_game not in ['Y','N','y','n']:
        play_game = input("Do you want to play this game again? y = yes, n = no \n")
    if play_game == 'y':
        main()
    elif play_game == 'n':
        print("Thank you for playing Hangman game. Visit again.")
        exit()
        
def hangman():
    global count
    global display
    global word
    global already_guess
    global play_game
    limit = 5
    guess = input("This is a hangman word: " + display + " Enter your guess: \n")
    guess = guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <='9':
        print('Invalid Input\n')
        hangman()
        
    elif guess in word:
        already_guess.extend([guess])
        index = word.find(guess)
        word = word[:index] + "_" + word[index + 1:]
        display = display[:index]  + guess + display[index + 1:]
        print(display + '\n')
    
    elif guess in already_guess:
        print('Try another letter\n')
        
    else:
        count+=1
        
        if count ==1:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guess remaining\n")
        elif count == 2:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     | \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guess remaining\n")
        elif count ==3:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     | \n"
                  "  |     | \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guess remaining\n")
        elif count == 4:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     | \n"
                  "  |     | \n"
                  "  |     o \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guess remaining\n")
        elif count == 5:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     | \n"
                  "  |     | \n"
                  "  |     o \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")
            print("Wrong guess. Game over. You died.")
            print('The word was: ', already_guess)
            play_loop()
            
    if word == '_' * length:
        print('Wow! You save a life. Guessed word is correct!')
        play_loop()
        
    elif count != limit:
        hangman()
        
        
main()
hangman()
                
            