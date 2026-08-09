# write a class train which has methods to book a ticket ,get status (no of seats) and get fare information of train running under indian railways.

class Train:
    Total_seats=100
    def __init__(self,name,age,source,destination,contact,payment_method):
        self.name=name
        self.age=age
        self.source=source
        self.destination=destination 
        self.contact=contact
        self.payment_method=payment_method

    def book_ticket(self):
        if Train.Total_seats>0:
            Train.Total_seats-=1
            print(f'Ticked booked for {self.name} from {self.source} to {self.destination}')
        else:
            print(f'Seats not available ')

    def status(self):
        print(f'Total no of seats {Train.Total_seats}')

    def get_fare(self):
        # simple logic just right now
        fare= 1000
        print(f'Fare from {self.source} to {self.destination} is  ₹{fare}')               


# creating object 

p1 = Train("Anvi", 21, "Delhi", "Mumbai", "9999999999", "UPI")
p2 = Train("Rahul", 25, "Delhi", "Mumbai", "8888888888", "Card")

# using methods
p1.status()
p1.book_ticket()
p1.get_fare()

print()

p2.status()
p2.book_ticket()