class Train:
    # => Class
    def __init__(self, train_no, name, source, destination, seats): # constructor..
        self.train_no = train_no
        self.name = name
        self.source = source
        self.destination = destination
        self.seats = seats
    def display_train(self):
        print("\n Train_no :", self.train_no)
        print("\n Name :", self.name)
        print("\n Source :", self.source)
        print("\n Destination :", self.destination)
        print("\n seats", self.seats)

    def book_ticket(self):
        if self.seats > 0:
            self.seats -+ 1
            print("Ticket booked successful!")
            print("Reamaining seats", self.seats)
        else:
            print("Sorry! no Seat Available!")
    def cancel_ticket(self):
        self.seats +=1
        print("Ticket cancel succesfully!")
        print("Available seats", self.seats)

# => creating Object

train1 = Train(101,"express","Hyderabad","satna",5)
train2 = Train(102,"Superfast","Delhi","Mumbai",3)

# display train Details
train1.display_train()
train2.display_train()


# Book ticket
print("\n Cancelling Ticket")
train1.cancel_ticket()


# Displey updates Details
print("\n Updates train Details")
train1.display_train()




    