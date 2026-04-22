import random
#This is the list of words that are randomly picked by the program for the specified length of words whether 3,4 or 5
WORD_LISTS = {
    3: ["cat", "dog", "run", "sun", "hat", "map", "cup", "fog", "big", "jam"],
    4: ["game", "love", "fire", "wind", "rain", "moon", "star", "gold", "lamp"],
    5: ["brave", "flame", "crisp", "globe", "index", "juice", "kneel", "large"]
}
# This is a function to display the output based on the user's guess and how correct they are
def get_feedback(secret, guess):
    feedback = []
    for i, letter in enumerate(guess):
        if letter == secret[i]:
            feedback.append(letter.upper())
        elif letter in secret:
            feedback.append(letter.lower())
        else:
            feedback.append("$")
    return "".join(feedback)
    
#this is a function to print a key for easy understanding    
def print_legend():
    print("KEY: \n")
    print("UPPERCASE means correct letter in correct psoition")
    print("lowercase means correct letter in wrong position")
    print("$ means letter does not exist in word")
#This is the function showing the logic of the game
def play_word_guess_game():
    print("---------ITS TIME TO GUESS A WORD---------")
#Checking if the user has entered a correct length
    while True:
        try:
            length = int(input("Choose a number between 3,4, and 5: ").strip())
            if length in (3, 4, 5):
                break
            else:
                print("Invalid number! Choose among 3,4, or 5")
        except ValueError:
            print("Input should be a number among 3,4,or 5 ")
#The random_word is from the particular length of words in the words list    
    random_word = random.choice(WORD_LISTS[length])
    max_attempts = length + 1
    print(f"Nice! Now guess a {length}-letter word.")
    print(f"You have {max_attempts} attempts to guess the correct word")
    print_legend()
#The for loop to count the number of attempts used for the guesses    
    for attempt in range(1, max_attempts+1):
        while True:
            user_guess = input(f"Attempt {attempt}/{max_attempts} → ").strip().lower()
            if len(user_guess)!= length:
                print(f"Your guess must have only {length}letters")
            elif not user_guess.isalpha():
                print("The guess should consist of only letters")
            else:
                break
        
        feedback = get_feedback(random_word,user_guess)
        print("Feedback: "+feedback+"\n")
        
        if feedback==random_word.upper():
                print(f"Congra congra! You guessed right in {attempt} attempt(s)!")
                break
    else:
        print(f"You have finished your attempts! Correct word : '{random_word.upper()}'")
#If the user wants to repeat the game        
    again = input("Do you want to play again? (yes/no): ").strip().lower()
    if again in ("yes","y"):
        play_word_guess_game()
    else: 
        print("Come again next time")
#Calling the game function to begin            
play_word_guess_game()