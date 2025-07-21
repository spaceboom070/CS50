print("Welcome to Ed's diner!")
def greatworkservers() :
    bill = input("what is your meal cost")
    bill = bill.replace("$", "")
    bill = float(bill)
    tip = bill/100*20
    print(f"${tip:.2f}")
greatworkservers()
input()