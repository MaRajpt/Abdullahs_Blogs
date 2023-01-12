# ### READ FILE ###
#
# with open("my_file.txt") as file:         # By default mode = "r"  (write)
#     contents = file.read()
#     print(contents)
#
# #### WRITE FILE ### OVER WRITES
# # IF WE OPEN A FILE IN WRITE MODE BUT I DOSENT EXIST THE SYSTEM WILL CREATE IT FOR YOU
# # e.g:
# with open("my_new_file.txt", mode="w") as file:         # "w" stands for write
#     file.write("New text.")
#
# with open("my_file.txt", mode="w") as file:         # "w" stands for write
#     file.write("New text.")
#
# ### APPEND FILE #######
#
# with open("my_file.txt", mode="a") as file:         # "a" stands for append
#     file.write("\nNew text.")

























