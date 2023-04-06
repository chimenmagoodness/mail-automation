PLACEHOLDER = '[name]'

with open('./Input/Names/invited_names.txt') as name_file:
    names = name_file.readlines()


letter_file = open('./Input/Letters/starting_letter.docx').read()
    # letter_content = letter_file.read()
for name in names:
    stripped_name = name.strip()
    new_letter = letter_file.replace(PLACEHOLDER, stripped_name)
    with open(f'./Output/ReadyToSend/letter_for_{stripped_name}.docx', mode="w") as completed_letter:
        completed_letter.write(new_letter)
