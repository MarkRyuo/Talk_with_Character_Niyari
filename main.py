# Import 


# Todo Create a Log

def log() :

    #* ENTER your name 
    your_name = input("Enter your name: ")

    def Age_() : # * Define a function to age verification 

        attempt = 2 # * Declare a variable for attempt  

        while True : # * While loop 

            your_age = input("Enter your age: ")

            if your_age.isdigit() :
                if int(your_age) <= 10 : # * if your age is less than or equal to 10, age is not allowed
                    print("Age is not allowed")
                    break
                else :
                   break
            else : 
                 attempt -= 1 # * Attempt Decreament by 1 
                if attempt > 0 :  # * If attempt is greater than to 0 
                    print("Try again")
                else :
                    print("Locked")
                        break
                print(f"{your_age} is not a number") # * If your age is string

        return your_age
    
    Age_()


def main() :

    log()


main()
