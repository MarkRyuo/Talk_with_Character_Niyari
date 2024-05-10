# Character Niyari

# Create Object about Character Niyari 
character_Discription = {
    "_name" : "Niyari",
    "codename": "Twilight Niyari",
    "age" : 20
}



class Person: # Parent 

    def __init__(self, _name, codename, age) :
        self._name = _name 
        self.codename = codename
        self.age = age 

class Character(Person) :

    def __init__(self, _name, codename, age):
        super().__init__(_name, codename, age)

    
    def speech_1(self) :
        print(f"Hi i'm {self._name} ")

