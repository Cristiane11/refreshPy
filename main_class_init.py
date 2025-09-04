class officeBuilding:
    def __init__(self, name, address, num_floors):
        self.name = name
        self.address = address
        self.num_floors = num_floors        
    def __str__(self):
        return f"{self.name}, located at {self.address}, has {self.num_floors} floors."
    
building1 = officeBuilding("Tech Hub", "456 Innovation Drive", 10)
print(building1)
building2 = officeBuilding("Business Center", "789 Enterprise Ave", 15)
print(building2)
building3 = officeBuilding("Corporate Plaza", "101 Commerce St", 20)
print(building3)
class House:
    def __init__(self, address, num_bedrooms, num_bathrooms):
        self.address = address
        self.num_bedrooms = num_bedrooms
        self.num_bathrooms = num_bathrooms
        
    def __str__(self):
        return f"House at {self.address} with {self.num_bedrooms} bedrooms and {self.num_bathrooms} bathrooms."
building1.__str__