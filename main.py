student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")
print(data_frame)
new_dictionary = {row.letter:row.code for (index, row) in data_frame.iterrows()}
# for key in new_dictionary:
#     print(new_dictionary[key])

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user = input("enter a word:")
# user_list = []
# for word in user:
#     user_list.append(word.upper())
# user_list = [letter for letter in user]
user_list = [new_dictionary[letter] for letter in user]
print(user_list)