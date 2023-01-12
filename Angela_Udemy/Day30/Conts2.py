#
# height = float(input("height: "))
# weight = float(input("weight: "))
#
# if height > 3:
#     raise ValueError("height should not be above 3 meters")
#
#
# bmi = weight/ height ** 2
# print(bmi)


################################### INDEX ERROR EXERCISE

# fruits = ["Apple", "Pear", "Orange"]
#
# #TODO: Catch the exception and make sure the code runs without crashing.
#
# def make_pie(index):
#     try:
#         fruit = fruits[index]
#     except IndexError:        # except will take in account all error instead we want it to be specific
#         print("fruit pie")
#     else:
#         print(fruit + " pie")
#
# make_pie(3)
#

############################  KEY ERROR EXERCISE

# facebook_posts = [
#     {'Likes': 21, 'Comments': 2},
#     {'Likes': 13, 'Comments': 2, 'Shares': 1},
#     {'Likes': 33, 'Comments': 8, 'Shares': 3},
#     {'Comments': 4, 'Shares': 2},
#     {'Comments': 1, 'Shares': 1},
#     {'Likes': 19, 'Comments': 3}
# ]
# total_likes = 0
#
# for post in facebook_posts:
#     try:
#         total_likes = total_likes + post['Likes']
#     except KeyError:
#         pass            # basically its ignoring the dictionaries with NO likes  e.g total_likes += 0
#
# print(total_likes)


################# EXCEPTION HANDLING IN NATO PHONETIC ALPHABET
import pandas

data = pandas.read_csv("/Users/ma088/Desktop/PYTH/Angela_Udemy\Day26/nato_phonetic_alphabet.csv")
data_dict = {row.letter: row.code for (index, row) in data.iterrows()}

def nato():
    #TODO 2. Create a list of the phonetic code words from a word that the user inputs.
    word = input("Please enter the word: ").upper()
    try:
        output = [data_dict[letter] for letter in word]
    except KeyError:
        print("Please only enter alphabets !")
        nato()
    else:
        print(' '.join(output))

nato()




