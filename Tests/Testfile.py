
import string
import random

# create a list structure containing all the letters
letters = list(string.ascii_letters)
# sample without replacement (use random sample from the random library to shuffle letters)
codes = random.sample(letters, k=len(letters))

# create an encrypt and decrypt dictionary
encrypt_key = dict(zip(letters,codes))
decrypt_key = dict(zip(codes,letters))

# insert todays phrase (this could be changed to query a website, select from a supplied file with list
# of phrases. Note here that we randomly select a phrase from the plain_text_list. 
plain_text_list=["The secret of getting ahead is getting started", "For whom the bell tolls", "I can't get no satisfaction, but I try"]
plain_text = plain_text_list[random.randint(0,len(plain_text_list))-1]

# Here we scramble our phrase and create a new string called scrambled
cipher_text = ''
for i in plain_text:
    if i in string.ascii_letters:
        cipher_text += encrypt_key[i]
    else:
        cipher_text += i

# # Note, for those looking to understand more advanced techniques, we can accomplish the same things as the for loop
# # above using a single line "list comprehension"
# scrambled = ''.join([encrypt[x] if x in string.ascii_letters else x for x in phrase])


# Here we start our user interface, and let the player play the game
print("\nWelcome to word scramble!\n\n")

while True:
    print("Todays word is:")
    print(cipher_text)

    user_input = input("\nPlease enter your guess (or type exit to exit): \n")

    if user_input.lower() == "exit":
        break
    elif user_input == plain_text:
        print("\nThat is correct! Great work")
        break
    else:
        print("\nSorry, that is incorrect. Please try again.\n")

print("\n\nThanks for playing word scramble.\n\n")