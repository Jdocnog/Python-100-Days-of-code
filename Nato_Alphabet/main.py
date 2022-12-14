# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass


# student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    # pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas
#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter:row.code for (index, row) in nato_data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
users_name = list(input("What is your name? ").upper())
print(users_name)
users_nato_name = [nato_dict[letter] for letter in users_name]
print(users_nato_name)
# for letter in users_name:
#         print(nato_dict[letter.values]) ##Turned this into the dict comprehension above

