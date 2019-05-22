def Strcon(string):
    string = " "

    return (string[0:len(string):2].upper()+string[1:len(string):2])
        
print(Strcon("We have been the most powerful of civilization.")