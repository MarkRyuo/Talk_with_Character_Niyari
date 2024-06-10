from Character_module import Person

# Character Niyari

# Create Object about Character Niyari 
character_Discription_Niyari = {
    "_name" : "Niyari",
    "codename": "Twilight Niyari",
    "age" : 20,
    "Location" : "Shadow of the Orient Seas"
}


class Character_niyari(Person) :

    def __init__(self, _name, codename, age, location):
        super().__init__(_name, codename, age)
        self.place = place
    
    def speech_1(self) :
        print(f"Hi i'm {self.name}, I'm sorry I suspected you as a monster")
    
    def speech_2(self) :
        print("")

