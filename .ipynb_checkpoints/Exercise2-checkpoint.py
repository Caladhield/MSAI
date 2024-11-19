import random 
while True:
    number = random.randint(1, 100) 
    number_of_guesses = 0 
    name = input("Hej! vad heter du?")
    print("Okej " + name.capitalize() + "! Gissa ett tal mellan 1 och 100")
    while number_of_guesses < 10: 
        guess = int(input())
        number_of_guesses += 1 
        if guess == number: 
            print('Bra jobbat! Du gissade rätt efter ' + str(number_of_guesses) + ' gånger!')
            break
        elif guess < number: 
            if number - guess < 5: 
                print("Varmt! Gissa på ett större tal.")
            else: 
                print("Kallt! Gissa på ett större tal.")
        else: 
            if guess - number < 5:
                print("Varmt! Gissa på ett mindre tal.")
            else: 
                print("Kallt! Gissa på ett mindre tal.")
    else: 
        print("Tyvärr! du förlorade. Rätt siffra var", str(number))
    
    play_again = input("Vill du spela igen? y/n ").lower() 
    if play_again == "n" :
        print("Tack för att du spelade.")
    break