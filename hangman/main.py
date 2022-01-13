import random
import hangman_art
import wordlist

print(hangman_art.logo)

word_list = wordlist.word_list

stages = hangman_art.stages

chosen_word = random.choice(word_list)

print(f"Pssst, the solution is {chosen_word}")

display = []

health = 6

for letter in chosen_word:
    display.append("_")

while ("_" in display) and health > -1:
    guess = input("Guess a letter: ").lower()

    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = chosen_word[i]

    if guess not in chosen_word:
        health -= 1
        print(stages[health])
        if health == 0:
            print("You lose")
            break
    print(" ".join(display))

if ("_" not in display) and (health > -1):
    print("You win!")
