class vehicle:
    def __init__(self,reg_no,capacity_kg):
        self.reg_no = reg_no
        self.capacity_kg = capacity_kg

class DeleveryVan(vehicle):
    def __init__(self, reg_no,capacity_kg, route):
        super().__init__(reg_no, capacity_kg)
        self.route = route
van = DeleveryVan("MH 12 BB 1234", 100000,"REWA - MUMBAI")
print(f"{van.reg_no} | carries {van.capacity_kg}, {van.route}")

