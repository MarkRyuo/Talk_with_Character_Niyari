# Import
import main 

your_name = main.log()


# Todo Create a Dict about character Niyari 

Character_Description = { 
    "Name" : "Niyari",
    "Codename" : "Light Princess",
    "Age" : 19,
    "Location" : "Oriental Dart " 
}


class Character_ :

    def __init__(self,Name, Codename, Age, Location) :
        self.Name = Name
        self.Codename = Codename 
        self.Age = Age 
        self.Location = Location
    
    def speak1(self) :
        print(f"Hi user: {self,Name}")



char = Character(your_name)
char.speak1