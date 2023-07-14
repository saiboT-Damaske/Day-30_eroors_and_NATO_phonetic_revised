import pandas


student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# # Looping through dictionaries:
# for (key, value) in student_dict.items():
#     # Access key and value
#     print(key)


student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
nato_data = pandas.read_csv("./nato_phonetic_alphabet.csv")
# for (index, row) in nato_data.iterrows():
#     print(nato_data.iloc[index].code)

nato_dict = {row.letter:row.code for (index, row) in nato_data.iterrows()}
print(nato_dict)
# TODO 2. Create a list of the phonetic code words from a word that the user inputs. UPDATE: catch key errors


def generate_phonetic():
    user_word = input("Type a word: ").upper()
    try:
        result = [nato_dict[letter] for letter in user_word]
    except KeyError:
        print("Sorry, only letters of the alphabet allowed.")
        generate_phonetic()
    else:
        print(result)


generate_phonetic()


