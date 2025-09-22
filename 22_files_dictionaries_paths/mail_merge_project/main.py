#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


# Use the full path from the project root
with open("22_files_dictionaries_paths/mail_merge_project/Input/Letters/starting_letter.txt", "r") as f:
    letter_content = f.read()

# Read the invited names file
with open("22_files_dictionaries_paths/mail_merge_project/Input/Names/invited_names.txt", "r") as names_file:
    invited_names = names_file.readlines()

for name in invited_names:
    stripped_name = name.strip()
    new_letter = letter_content.replace("[name]", stripped_name)
    with open(f"22_files_dictionaries_paths/mail_merge_project/Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
        completed_letter.write(new_letter)
        