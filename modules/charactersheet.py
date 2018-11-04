classes = []

class CharacterSheet:
    def __init__(self):
        # User Attributes
        self.server = "3453453453"
        self.userid = "3456356345"
        
        # Dnd Attributes
        self.stats = {
            "Strength": [0, 0],
            "Dexterity": [0, 0],
            "Constitution": [0, 0],
            "Intelligence": [0, 0],
            "Wisdom": [0, 0],
            "Charisma": [0, 0]
        }

        self.skills = {
            "Athletics": [0, 0],
            "Acrobatics": [0, 0],
            "Sleight of Hand": [0, 0],
            "Stealth": [0, 0],
            "Arcana": [0, 0],
            "History": [0, 0],
            "Investigation": [0, 0],
            "Nature": [0, 0],
            "Religion": [0, 0],
            "Animal Handling": [0, 0],
            "Insight": [0, 0],
            "Medicine": [0, 0],
            "Perception": [0, 0],
            "Survival": [0, 0],
            "Deception": [0, 0],
            "Intimidation": [0, 0],
            "Performance": [0, 0],
            "Persuasion": [0, 0]
        }

        self.equipment = { }


    def encode():
        print("encoding")

    def decode(object):
        print("decoding")

    def displaySheet():
        print("display the sheet and stuff")
        

x = CharacterSheet()
