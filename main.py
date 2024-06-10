# Import 


# Todo Create a Log



def log() :

    #* ENTER your name 
    your_name = input("Enter your name: ")
    your_age = input("Enter your age: ")

    def Age_() :

        if your_age.isdigit() :
            if your_age <= 10 : # * if your age is less than or equal to 10, age is not allowed
                print("Age is not allowed")
                exit()
            else :
                print()
        else : 
            print(f"{your_age} is not a number") # * If your age is string 
    
    Age_()


def main() :

    log()
 



main()
