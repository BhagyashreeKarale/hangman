import string
from word import choose_word
from images import IMAGES

# End of helper code
# -----------------------------------

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: ek string word jo ki user ko guess karna hai
    letters_guessed: ek list hai, jisme wo letters hai jo ki user nai abhi tak guess kare hai
    returns: return True kare agar saare letters jo ki user ne guess kiye hai wo secret_word mai hai, warna no
      False otherwise
    '''
    for i in letters_guessed:
        if i in secret_word:
            return True
    return False
# Iss function ko test karne ke liye aap get_guessed_word("kindness", [k, n, d]) call kar sakte hai
def display_hangman(tries):
    return IMAGES[tries]
def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: ek string word jo ki user ko guess kar raha hai
    letters_guessed: ek list hai, jisme wo letters hai jo ki user nai abhi tak guess kare hai
    returns: ek string return karni hai jisme wo letters ho jo sahi guess huye ho and baki jagah underscore ho.
    eg agar secret_word = "kindness", letters_guessed = [k,n, s]
    to hum return karenge "k_n_n_ss"
    '''
    index = 0
    guessed_word = ""
    while (index < len(secret_word)):
        if secret_word[index] in letters_guessed:
            guessed_word += secret_word[index]
        else:
            guessed_word += "_"
        index += 1
    
    return guessed_word

def get_available_letters(letters_guessed):
    '''
    letters_guessed: ek list hai, jisme wo letters hai jo ki user nai abhi tak guess kare hai
    returns: string, hame ye return karna hai ki kaun kaun se letters aapne nahi guess kare abhi tak
    eg agar letters_guessed = ['e', 'a'] hai to humme baki charecters return karne hai
    jo ki `bcdfghijklmnopqrstuvwxyz' ye hoga
    '''
    import string
    all_letters= list(string.ascii_lowercase)
    letters_left=""
    for i in all_letters:
        if i in letters_guessed:
            continue 
        else:
            letters_left+=i
    return letters_left
def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    Hangman game yeh start karta hai:
    * Game ki shuruaat mei hi, user ko bata dete hai ki
      secret_word mei kitne letters hai
    * Har round mei user se ek letter guess karne ko bolte hai
    * Har guess ke baad user ko feedback do ki woh guess uss
      word mei hai ya nahi
    * Har round ke baar, user ko uska guess kiya hua partial word
      display karo, aur underscore use kar kar woh letters bhi dikhao
      jo user ne abhi tak guess nahi kiye hai
    '''
    letters_guessed = []
    available_letters = get_available_letters(letters_guessed)
    tries=0
    print ("Welcome to the game, Hangman!")
    print ("I am thinking of a word that is " + str(len(secret_word)) + " letters long.")
    print ("")
    print(display_hangman(tries))
    print ("Available letters: " + available_letters)
    tries=1
    while tries<8:
        if tries == 7:
            if get_guessed_word(secret_word, letters_guessed)==secret_word:
                print (" * * Congratulations, you won! * * ")
                print ("")
            else:
                print(display_hangman(tries))
                print("Oops!You ran out of chances.\nThe secret word is:",secret_word,"\nBetter luck next time")
            tries+=1
            
        else:
            guess = input("Please guess a letter: ")
            letter = guess.lower()            
            if letter in secret_word:
                letters_guessed.append(letter)
                if get_guessed_word(secret_word, letters_guessed)==secret_word:
                    print (" * * Congratulations, you won! * * ")
                    print ("")
                    break
                else:
                    print ("Good guess: " + get_guessed_word(secret_word, letters_guessed))
                    print ("")
                    print(display_hangman(tries-1))
            else:
                print ("Oops! That letter is not in my word: " + get_guessed_word(secret_word, letters_guessed))
                print(display_hangman(tries))
                print ("")
                tries+=1
def play():
    secret_word = choose_word()
    hangman(secret_word)
    while input("Do you want to play again?(Y/N)")=="Y":
        secret_word = choose_word()
        hangman(secret_word)
play()
