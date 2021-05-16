################################################################################
#
#   Lab #8
#
#   Purpose: This program has the option to convert a given sentence to either
#               Pig-latin if english or to English if Pig-latin.
#   Author: Tigris Mendez
#   Date Written: April 28th, 2021
#   Version: 2.9
#
################################################################################

#print prompt for user to "input a sentence and select options of translation."
print("\nThis program is meant to either translate English to Pig Latin, or Pig Latin to English.\n")
sentence = input("input a sentence:\n")

#ask user for input of sentence (piglatin/ english as " type p2e or e2p")
process = input("If you would like to translate from Pig Latin to English, enter 'p2e'\n"
                "If you would like to translate from English to Pig latin, enter 'e2p'\n:")

#convert sentence to a list of strings
input_list = sentence.split()

#new sentence to append onto
new_sentence = []

#global variables
pyg = 'ay'
yay = 'yay'


#for each item in the sentence, send through for-loop if/else-statement then concantenate to new_sentence
# identify if word starts with a consonant (word[0] != a,e,i,o,u)
def english_to_piglatin():

    for i in input_list:
        if len(i) > 0 and i.isalpha() and (str(i[0])=='a' or str(i[0])=='e' or str(i[0])=='i' or str(i[0])=='o' or str(i[0])=='u'):
            # convert sentence to lowercase.
            word = i.lower()
            # create a new_word that is made from concantenating word + 'yay'
            new_word = word + yay
            new_sentence.append(new_word)
        elif len(i) > 0 and i.isalpha() and (str(i[0])!='a' or str(i[0])!='e' or str(i[0])!='i' or str(i[0])!='o' or str(i[0])!='u'):
            # convert sentence to lowercase.
            word = i.lower()
            first = i[0]
            # create a new_word that is made from concantenating word + [0] + 'ay'
            new_word = word + first + pyg
            new_word = new_word[1:]
            new_sentence.append(new_word)
    else:
        print("empty")

    print (new_sentence)


#Piglatin_to_english
def piglatin_to_english():

    for i in input_list:
        # determine if the last three letters are 'yay'.
        if len(i) > 0 and i.isalpha() and (str(i[-3:])=='yay'):
            # if so, remove last three letters.
            # convert sentence to lowercase.
            piglatin_word = i.lower()
            #remove 'yay' from piglatin_word
            new_word = piglatin_word.replace('yay', '')
            new_sentence.append(new_word)
        # determine if the last 3 letters are something other than 'yay'.
        elif len(i) > 0 and i.isalpha() and (str(i[-3:])!='yay'):
            # convert sentence to lowercase.
            piglatin_word = i.lower()
            pl_minus_last_two = piglatin_word[:-2]
            #remove the last two letters and move the remaining letter to the front.
            new_word = pl_minus_last_two[-1] + pl_minus_last_two[:-1]
            new_sentence.append(new_word)

    else:
        print("empty")

    print (new_sentence)

#Mainline logic of the program

if process == 'p2e':
    piglatin_to_english()
elif process == 'e2p':
    english_to_piglatin()
else:
    print('invalid process plz try again')
    exit()




