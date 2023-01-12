### letter.readlines will read all the lines whereas letter,readline will read one line (first)



names = open("invited_names.txt", 'r')
name_list = names.readlines()

letter = open("starting_letter.txt",'r')
lines = letter.read()

for i in name_list:
    stripped_name = i.strip()
    update_names = lines.replace("[name]", stripped_name)
    letters = open(f"Letter for {stripped_name}.txt", 'w')
    make_letters = letters.write(update_names)





######### LOND NON EFFCIENT METHOD ############

    # letter = open("starting_letter.txt",'r')
    # lines = letter.readlines()
    # striped_name = i.strip()
    # update = lines[0].replace("[name]", striped_name)
    # lines[0] = update
    # lines.append("---------------------------------\n")
    # new_letter = ''.join(lines)
    # all_letters = open("all_letters.txt", "a")
    # write_letters = all_letters.write(new_letter)
    # print(new_letter)
