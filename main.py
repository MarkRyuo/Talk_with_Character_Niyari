# Import 


# Todo Create a Log

def log() :

    #* ENTER your name 
    your_name = input("Enter your name: ")

    def Age_() :

        while True :

            your_age = input("Enter your age: ")

            if your_age.isdigit() :
                if int(your_age) <= 10 : # * if your age is less than or equal to 10, age is not allowed
                    print("Age is not allowed")
                    break
                else :
                    break
            else : 
                print(f"{your_age} is not a number") # * If your age is string

        return your_age
    
    Age_()


def main() :

    log()


main()
