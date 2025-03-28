# Beginning: create variables
Basketball_points = 0
Soccer_points = 0


# Middle: Ask questions
answer = input ("Would you rather A) Score and game winning 3pt shot, B) Score a game winning goal?")
if answer == "A":
    Basketball_points += 1
elif answer == "B":
    Soccer_points += 1


answer = input ("Would you rather A) Play with Michael Jordan, B) Play with Cristiano Ronaldo?")
if answer == "A":
    Basketball_points += 1
elif answer == "B":
    Soccer_points += 1


answer = input ("Would you rather A) Play on hardwood, B) Play on grass?")
if answer == "A":
        Basketball_points += 1
elif answer == "B":
    Soccer_points += 1


answer = input ("Would you rather A) Play in game 7 of the NBA finals, B) Play in the World Cup final?")
if answer == "A":
    Basketball_points += 1
elif answer == "B":
    Soccer_points += 1


answer = input ("Would you rather A) Play in meduim size socks, B) Play in long socks?")
if answer == "A":
    Basketball_points += 1
elif answer == "B":
    Soccer_points += 1


# End: Determine results
if Basketball_points > Soccer_points:
    print("You are a Baksetball person")
elif Soccer_points > Basketball_points:
    print("You are a Soccer person")