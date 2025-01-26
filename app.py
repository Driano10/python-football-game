import random

# Welcome the user to the game
print("Welcome to the football game!")
print("Which football team has the most Premier Leagues?")
score = 0

# First Question
question1 = input()

if question1.lower() in ["manchester united", "man utd"]:
    print("Correct! They have won 13 times, and the last time they won was in the 12/13 Premier League season.")
    score += 1
else:
    print("Incorrect! The answer is Manchester United.")
    score -= 1
print("Your points:", score)

# Second Question
print("Who scored the most goals in the 2022 World Cup?")
question2 = input()

if question2.lower() in ["kylian mbappe", "mbappe"]:
    print("Correct! Kylian Mbappe scored 8 goals for France.")
    score += 1
else:
    print("Incorrect! It was Kylian Mbappe. He managed to get 8 goals in that campaign.")
    score -= 1
print("Your points:", score)

# Third Question
print("Name a former or current English footballer who has played for Real Madrid.")
user_answer = input()

correct_answers = [
    "jude bellingham", "bellingham", "michael owen", "owen",
    "david beckham", "beckham", "jonathan woodgate", "woodgate",
    "steve mcmanaman", "mcmanaman", "laurie cunningham", "cunningham"
]

if user_answer.lower() in correct_answers:
    print("Well Done! Jude Bellingham, Michael Owen, David Beckham, Steve McManaman, Jonathan Woodgate, and Laurie Cunningham played for Los Blancos as Englishmen.")
    score += 1
else:
    print("Wrong! Jude Bellingham, Michael Owen, David Beckham, Steve McManaman, Jonathan Woodgate, and Laurie Cunningham played for Los Blancos as Englishmen.")
    score -= 1
print("Your points:", score)

# Fourth Question
print("How many teams has Mohamed Salah played for in his senior career?")
question4 = input()

if question4 == "6":
    print("Spot on! He has played for 1. Al Mokawloon, 2. Basel, 3. Chelsea, 4. Fiorentina, 5. Roma, and his current team, 6. Liverpool.")
    score += 1
else:
    print("That is wrong. He has played for 1. Al Mokawloon, 2. Basel, 3. Chelsea, 4. Fiorentina, 5. Roma, and his current team, 6. Liverpool.")
    score -= 1
print("Your points:", score)

# Fifth Question
print("How many goals did Neymar score for PSG?")
correct_answer = "118"

for attempt in range(3):
    user_guess = input()
    if user_guess == correct_answer:
        print("Correct! Neymar scored 118 goals in 173 appearances for Paris Saint-Germain.")
        score += 1
        break
    else:
        print(f"Incorrect. You have {2 - attempt} more guesses.")
        print("Hint: It's between 100 and 120.")
else:
    print("That's wrong again, and you have no more guesses. The answer was 118.")
    score -= 1
print("Your points:", score)

# Sixth Question
print("Which footballer was on the FIFA 19 cover?")
question6 = input().lower()

correct_answers3 = ["neymar jr", "neymar", "kevin de bruyne", "de bruyne", "paulo dybala", "dybala", "cristiano ronaldo", "ronaldo", "cr7"]

if question6 in correct_answers3:
    print("Correct. Ronaldo was originally on the cover before he got replaced by Dybala, Neymar, and De Bruyne.")
    score += 1
else:
    print("Nope. The correct answers were Ronaldo, De Bruyne, Neymar, or Dybala.")
    score -= 1
print("Your points:", score)

# Seventh Question
print("Which academy did Garnacho play for before he joined Manchester United's academy?")
correct_answer = "atletico madrid"

for attempt in range(3):
    user_guess = input().lower()
    if user_guess == correct_answer:
        print("Correct! That was a tough question, so you get a bonus point.")
        score += 2
        break
    else:
        print(f"No, that is wrong. You have {2 - attempt} more guesses.")
        print("Hint: The team is in Spain.")
else:
    print("Wrong. The answer is Atletico Madrid.")
    score -= 1
print("Your points:", score)

# Eighth Question
print("How many European trophies did César Azpilicueta win in his club career?")
correct_answer = "4"

for attempt in range(3):
    user_guess = input()
    if user_guess == correct_answer:
        print("Correct! He won 2 Europa Leagues, 1 Champions League, and 1 UEFA Super Cup.")
        score += 1
        break
    else:
        print(f"Incorrect. You have {2 - attempt} more guesses.")
        print("Hint: The last one he won was 2 seasons ago.")
else:
    print("That's wrong again, and you have no more guesses. The answer was 4.")
    score -= 1
print("Your points:", score)

# Ninth Question
print("Which player has the highest market value in the Premier League?")
correct_answers = ["bukayo saka", "saka"]

for attempt in range(3):
    user_guess = input().lower()
    if user_guess in correct_answers:
        print("Correct!")
        score += 1
        break
    else:
        print(f"No, that is wrong. You have {2 - attempt} more guesses.")
        print("Hint: He is English.")
else:
    print("Wrong. The answer is Bukayo Saka.")
    score -= 1
print("Your points:", score)

# Final Score
print(f"Game over! Your final score is {score}.")
