import random

word = ["Elephant","Computer","Python","Adventure","Butterfly","Happiness","Chocolate"]
replace = []
seperate_word = []
used = []
correct = []
def random_word():
    global target_word
    target_word = word[random.randint(0,6)]
    length_word = len(target_word)
    return target_word,length_word

rand,length = random_word()
def seperate():
    for letters in rand:
        for let in letters:
            low = str.lower(let)
            seperate_word.append(low)
    for num in range(len(target_word)):
        replace.append("_")


def guess():
    length = len(target_word)
    count_death = 6
    while True:
        print(f"You have used {used} that are not correct")
        print(f"These letters are in the word:{correct}")
        ask = str(input("Give a letter:"))
        if ask in seperate_word:
            index = seperate_word.index(ask)
            replace[index] = ask
            seperate_word[index] = "_"
            length -= 1
            correct.append(ask)
            print("==========================================================================")
            print(replace)
            if length <= 0:
                print(f"you Win, the word is {target_word} ")
                break
        elif ask not in seperate_word:
            count_death -= 1
            print(f"you got {count_death} life left before dying")
            print("==========================================================================")
            used.append(ask)
            print(replace)
            if count_death <= 0:
                print(f"you die, the word is {target_word} ")
                break


seperate()
guess()
