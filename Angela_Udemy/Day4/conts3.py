
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

index1 = int(position[0])-1
index2 = int(position[1])-1

map[index2][index1] = 'X'


print(f"{row1}\n{row2}\n{row3}")        # because in line 12 we assigning values directly to-
                                        # row1 row2 row2 hence no need to print map just print rows- 
                                        # becuase map = [row1, row2, row3] we only put together lists in-
                                        # var name map, however if we did map = row1 + row2 + row3
                                        # then that game wonk work as desired