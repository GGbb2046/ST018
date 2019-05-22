astring = "I am learning to become a good programmer. I now program some basic stuff."

print(astring.find("learning"))    # this returns the index to the start of the word found

print(astring.find("good"))     # find the first occurrence 

print(astring.find("I", 5))  # to find any other occurrences, I need to start the search after the first one found

print(astring.find("xray")) # returns -1 if the string was not found