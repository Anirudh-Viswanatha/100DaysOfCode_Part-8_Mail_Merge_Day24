PLACEHOLDER = "[name]"

with open("/Users/<Fill_the_path>/Desktop/Mail Merge/Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()


with open("/Users/<Fill_the_path>/Desktop/Mail Merge/Input/Letters/starting_letter.txt") as letter_file:
    letter = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter.replace(PLACEHOLDER, stripped_name)
        with open(f"/Users/<Fill_the_path>/Desktop/Mail Merge/Output/ReadyToSend/Letter_to_{name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)








