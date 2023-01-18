import random
import hanelukner
def game():
    my_words=hanelukner.my_words
    the_word=random.choice(my_words)
    print(hanelukner.hanelukner[my_words.index(the_word)])
    proces=len(the_word)*"_"
    y=list(proces)
    p=list(the_word)
    print("\nTry to guess this word ;)\nYou have 2 chances to be wrong(armenian letter in low case)")
    a=0
    class chikareli(Exception):
        pass    
    while a<3:
        print(proces)
        try_=0
        while try_==0:
            try:
                letter=str(input("enter a letter-> "))
                if letter not in hanelukner.tarer:
                    raise chikareli
                else:
                    try_=1
            except chikareli:
                print("We need one letter in a low case!\n"+proces)        
        if letter in proces:
            print("You have already entered that letter :/ Be carefull.")
        if letter in the_word and letter not in proces:
            k=0
            while k<the_word.count(letter):
                if the_word.count(letter)>1:
                    y[the_word.find(letter)]=letter
                    proces="".join(y)
                    p[the_word.find(letter)]="*"
                    the_word="".join(p)
                    if letter in the_word:
                        y[the_word.find(letter)]=letter
                        proces="".join(y)                                        
                elif the_word.count(letter)==1:
                    y[the_word.find(letter)]=letter
                    proces="".join(y)
                    k+=1
                    a=a
            if  proces in my_words:
                print("\""+proces+"\" You Win!!!")
                break
            print("Yes, \""+letter+"\" is in the word.")
        elif letter not in the_word:
            print("No, \""+letter+"\" is not in the word")
            a+=1
            if a==1:
                print("One chance left")
            if a==2:
                print("It is your last chance!")
            elif a==3:
                print("You loose :(\nThe word was \""+hanelukner.my_words[my_words.index(the_word)]+"\"")
game()

    