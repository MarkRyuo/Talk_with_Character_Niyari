# Import 
from Character import Character_Description

# Todo Create a Log for Entering details 
# Todo Ilagay ang class dito 

CHAR_NAME = Character_Description.get("Name")

class Character_ :

    def __init__(self,Name, Codename, Age, Location) :
        self.Name = Name
        self.Codename = Codename 
        self.Age = Age 
        self.Location = Location
    
    def Qualify(self) :
        print(
            f"Welcome to Talk With {CHAR_NAME}"
            )
        print(
            f"Age Detected: {self.Age} \nName Detected: {self.Name} "
        )
    
    def speak1(self) :
        print(f"Welcome! I'm {CHAR_NAME} ")
        speak_1 = input("What is your name: ")

        if speak_1 :
            print(f"Thank you to answer {self.name}")
        else :
            print() 



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
                    exit()
                else : # * Break if greater than 10 
                    break
            else : 
                attempt -= 1 # * Attempt Decrement by 1 
                if attempt > 0 :  # * If attempt is greater than to 0 
                    print(f"{your_age} is not a number") # * If your age is string
                else :
                    print("Locked you have 2 attempt already🔒")
                    exit()
                
        return your_age 
    
    your_age = Age_()
    return your_name, your_age


def main() :

    your_name, your_age = log() 
    Char = Character_(your_name, None,your_age, None) # * None for no value 
    Char.Qualify()
    Char.speak1(your_name)

main()
