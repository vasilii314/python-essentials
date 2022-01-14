PLACEHOLDER = "[name]"


with open("Names/invited_names.txt") as names_file:
    names = map(lambda item: item.strip(), names_file.readlines())
with open("Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        new_letter = letter_contents.replace(PLACEHOLDER, name)
        with open(f"Output/ReadyToSend/letter_for_{name}.txt", "w") as completed_letter:
            completed_letter.write(new_letter)
