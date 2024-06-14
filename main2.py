# Import 


class Log :

    def __init__(self, Name, Age) : 
        self.Name = Name
        self.Age = Age 

    def Log_user(self) :

        #* Input Credentials 
        userName = input("Input your name: ")

        userAge = input("Input your age: ") 
        
        if int(userAge) <= 10 :
            print("Your too young to talk in Niyari")
            exit
        else: 
            print()
        return userName, userAge