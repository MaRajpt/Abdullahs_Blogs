
# WORKING DIRECTORY MEANS THE FOLDER OD YOU R CURRENT PROJECT FILE

########  ABSOLUTE FILE PATH ( FULL PATH ) ########
# with open("/Users/sam_h/Desktop/MM.txt") as file:   # FILE ON DESKTOP
#     content = file.read()
#     print(content)

########  RELATIVE FILE PATH  ########
with open("../../days.txt") as file:   # ../ means one previous folder
    content = file.read()
    print(content)
