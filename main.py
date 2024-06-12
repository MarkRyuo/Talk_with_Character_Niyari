# Import 


# Todo Create a Log
# Todo Ilagay ang class dito 

class Character_ :

    def __init__(self,Name, Codename, Age, Location) :
        self.Name = Name
        self.Codename = Codename 
        self.Age = Age 
        self.Location = Location
    
    def speak1(self) :
        print(f"Hi user: {self.Name}")



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
                else : # * Break if greater than 10 
                    break
            else : 
                attempt -= 1 # * Attempt Decrement by 1 
                if attempt > 0 :  # * If attempt is greater than to 0 
                    print(f"{your_age} is not a number") # * If your age is string
                else :
                    print("Locked you have 2 attempt already🔒")
                    break
                

        return your_age
    Age_()
    return your_name


def main() :

    LOG = log()
    Char = Character_(LOG, None, None, None)
    Char.speak1

main()
