############ DICTIONARY #################

bio = {
    "name": "Abdullah",
    "age" : 30,
    "city": "Islamabad",
    69    : "prefered"
    
}

print(bio["age"])  # printing

bio["gender"] = "Male" # assigning key and value

print(bio)

gg = {}   # ASSIGNING empty dictionary

# bio = {}  # WIPE THE DICTIONARY

print(bio)

bio[69] = "definetly preferd"

print(bio)

for key in bio:
    print(key)          # NOTICE IT ONLY SHOWS KEYS ( NOT THEIR RESPECTED VALUES)
    print(bio[key])     # DISPLASY THE VALUES OF KEYS
    

########## USING DATA TYPES WITHIN DICTIONARIES ############

tavel_log = {
    "Pakistan": ["Islamabad", "Peshawar", "Karachi"],   # KEY CAN HAVE ONE VALUE OTHERWISE USE LIST OR OTHER DATA TYPE
    "India"  : "Delhi"
}

# NESTED DICTIONARY
likes= {
    "food" : {"desi": ["biryani", "daal" , "halwa"]}
}


############# TO GET MAXIMUM VALUE IN THE DICTIONARY ############


# max(dictionaryt_name, key=dictionaryt_name.get)




#  NESTED LISTS

["a", "b", ["c", "d"]]

#   DICTIONARIES CAN BE PUT INSIDE LIST

[
    {
    "desi": ["biryani", "daal" , "halwa"]
    },
 {
     "Pakistan": ["Islamabad", "Peshawar", "Karachi"]
     }
 ]