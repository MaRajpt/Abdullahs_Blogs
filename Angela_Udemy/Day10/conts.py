##################### FUNCTIONS WITH OUTPUT #############

# def my_function():
#     result  = 2*3
#     return result


# output = my_function() # BECAUSE function has 'return result' hence 'output' will have 6 value otherwise it wont.

# print(output)

#######################  FUNC to captilize first letter ##########

# def format_name(f_name , l_name):
#     formulated_f_name = f_name.title()
#     formulated_l_name = l_name.title()
#     return f"{formulated_f_name} {formulated_l_name }"


# formated_string = format_name("mUhaMMad", "abDULlaH")

# print(formated_string)


##########################  MULTIPLE RETURNS OF A FUNCTION  ##########################


def format_name(f_name , l_name):
    if f_name == "" or l_name == "":
        return "you didnt provide valid inputs"
    formulated_f_name = f_name.title()
    formulated_l_name = l_name.title()
    return f"{formulated_f_name} {formulated_l_name }"


formated_string = format_name(input("Enter your first name: "), input("Enter your last name: "))

print(formated_string)
