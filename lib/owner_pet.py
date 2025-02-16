class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet type: {pet_type}. Must be one of {Pet.PET_TYPES}")

        self.name = name
        self.pet_type = pet_type
        self.owner = None  

        Pet.all.append(self)
        
        if owner:  
            self.set_owner(owner)  

    def set_owner(self, owner):
        if not isinstance(owner, Owner):
            raise Exception("Owner must be an instance of Owner")
        
        self.owner = owner
        owner._pets.append(self)  

    def __repr__(self):
        return f"{self.name} ({self.pet_type})"


class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []  

    @property
    def pets(self):
        return self._pets  

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Invalid pet instance. Must be of type Pet.")

        pet.set_owner(self)  

    def get_sorted_pets(self):
        return sorted(self._pets, key=lambda pet: pet.name)

    def __repr__(self):
        return f"Owner: {self.name}"
