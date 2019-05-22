string = input("Please enter a string: ")

print(string[0].upper()+string[1:(len(string)-1)].lower()+string[len(string)-1].upper())

