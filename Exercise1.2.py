import random

def get_level():
    """Låter användaren välja svårighetsnivå och returnerar intervallet."""
    print("Välj svårighetsnivå:")
    print("1. Lätt (1-10)")
    print("2. Medel (1-50)")
    print("3. Svår (1-100)")
    level = input("Ange nivå (1, 2 eller 3): ")
    if level == "1":
        return 1, 10
    elif level == "2":
        return 1, 50
    elif level == "3":
        return 1, 100
    else:
        print("Ogiltigt val, standardnivå: Medel (1-50)")
        return 1, 50

def play_round(start, end):
    """Spela en omgång och returnera poängen."""
    secret_number = random.randint(start, end)
    attempts = 0
    max_score = 100  # Startpoäng
    print(f"Jag har valt ett nummer mellan {start} och {end}. Kan du gissa vilket?")
    
    while True:
        try:
            guess = int(input("Din gissning: "))
            attempts += 1
            if guess < secret_number:
                print("För lågt!")
            elif guess > secret_number:
                print("För högt!")
            else:
                print(f"Rätt gissat! Du behövde {attempts} försök.")
                break
        except ValueError:
            print("Ange ett giltigt nummer!")
    
    # Beräkna poängen (fler försök ger lägre poäng)
    score = max(max_score - (attempts - 1) * 10, 0)  # Poängen minskar med 10 per extra försök
    print(f"Din poäng för denna omgång är: {score}")
    return score

def main():
    """Huvudprogrammet."""
    print("Välkommen till nummergissningsspelet!")
    total_score = 0
    rounds = 0
    
    while True:
        start, end = get_level()
        score = play_round(start, end)
        total_score += score
        rounds += 1
        
        # Fråga om användaren vill spela igen
        play_again = input("Vill du spela en omgång till? (ja/nej): ").lower()
        if play_again != "ja":
            break
    
    # Visa genomsnittlig poäng
    if rounds > 0:
        avg_score = total_score / rounds
        print(f"Tack för att du spelade! Du spelade {rounds} omgångar.")
        print(f"Din genomsnittliga poäng är: {avg_score:.2f}")
    else:
        print("Du spelade inga omgångar.")

if __name__ == "__main__":
    main()
