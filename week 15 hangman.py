import random

s=""
word = random.choice(["melon", "banjo", "dwarves","orange","rhythmic"])
guess_string=[]
for x in range(len(word)):
    guess_string.append('_')
print guess_string 
wrong_letter = []
print "Time to play hangman!"
number_of_letters = len(word)
#print word
print "the number of letters in the word is " + str(number_of_letters)
while len(wrong_letter)<6:
    print "Enter a letter"
    guess = raw_input()
    if guess in word:
        print "correct" #how to display and what to do when there are 2 
        res = word.index(guess) 
        print ("Character {} in string {} is present at {}".format( guess, word, str(res + 1)))
        guess_string.insert(res, guess) 
        guess_string.pop(res+1)
        #list(map(lambda b: b.replace(guess,'_'), guess_string))
        print guess_string
        print s.join(guess_string)
    else: #if guess not in word:
        wrong_letter.append(guess)
        print "The following are wrong guesses:"
        print wrong_letter
        print "Guess again"
        if len(wrong_letter)== 1:
            print "i'm drawing a head"
        if len(wrong_letter)== 2 or len(wrong_letter)==3:
            print "i'm drawing an arm"
        if len(wrong_letter)== 4:
            print "i'm drawing a body"
        if len(wrong_letter)== 5:
            print "i'm drawing a leg"
        if len(wrong_letter)==6:
            print "i'm drawing the last leg"   
    if s.join(guess_string) == word:
        break
if len(wrong_letter) == 6:
    print "you loose the word was " + word
else:
    print "you win"
        