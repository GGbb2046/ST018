def Strcon(string):
    Astring = " "
    for count, ch in enumerate(string):
        if count%2 == 0:
            Astring +=ch.upper()
        else:
            Astring +=ch.lower()

    return Astring
    
        
print(Strcon("We have been the most powerful of civilization. When our successor look back they are going to see that hope has always led us to move ahead in the realm of existence."))