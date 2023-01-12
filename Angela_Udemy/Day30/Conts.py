#####  TRY   EXCEPT  ELSE  FINALLY

try:
    file = open("a_file.txt")       # this file didnt exist hence in except block it will create it
    dict = {"key": "value"}
    print(dict["asdf"])             # key doesent exist

except FileNotFoundError:                 # can have multiple exceptions
    file = open("a_file.txt", "w")
    file.write("something")

except KeyError as error_message:
    print(f"the key {error_message} does not exist")

# if there are no exceptions
else:
    content = file.read()
    print(content)

# Always runs no matter what
finally:
    raise KeyError("this is a error i made up")

