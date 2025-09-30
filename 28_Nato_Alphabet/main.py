import pandas

#TODO 1. Create a dictionary in this format:
data = pandas.read_csv("28_Nato_Alphabet/nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

def generate_phonetic():
    user_input = input("Enter your word: ").upper()
    try:
        word_list = [phonetic_dict[letter] for letter in user_input]
    except KeyError as e:
        print(f"Sorry, the character '{e.args[0]}' is not in the NATO alphabet. Please try again.")
        generate_phonetic()
    else:
        print(word_list)
        
        
generate_phonetic()
