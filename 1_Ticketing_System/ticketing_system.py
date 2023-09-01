SERVICE_CHARGE = 2
TICKET_PRICE = 10

tickets_remaining = 100  

# Create the calculate_price function. it ttake number of tickets and returns 
# number_of_ticket * TICKET_PRICE

def calculate_price(num_tickets):
    return (num_tickets * TICKET_PRICE) + SERVICE_CHARGE


while tickets_remaining >= 1:
    print("There are {} tickets remaining.".format(tickets_remaining))     
    name = input("Hi, what's your name? ")         

    try:
        number_of_tickets = int(input("Hi {}, how many tickets would you like to purchase? ".format(name)))
        if number_of_tickets > tickets_remaining:
            raise ValueError("There are only {} tickets left".format(tickets_remaining))
    except ValueError as err:
        print("Invalid entry. {}. Please enter a number.".format(err))
    else:
         total = calculate_price(number_of_tickets)
         print("The total cost for {} tickets will cost £{}.".format(number_of_tickets,total))
         customer_decision = str(input(f"Would you like to proceed with your purchase {name}? \nEnter Y/N "))
         while customer_decision != "y" or "n":
            if customer_decision.upper() == "Y":
                #card error handling on todo list
                card_num = str(input(f"{name}, Please enter your credit card number: "))
                # while len(card_num) < 16 or len(card_num) > 16:
                #     print("Card number is 16 digits long. Please enter 16 digits only.")
                #     break
                card_expiry = str(input("Please enter the expiry date:"))
                card_cvv = str(input("Now, enter the cvv(last 3 digits on back of card): "))
                print("Please wait whilst we process the payment ...")
                print("Sold, enjoy the show!")
                tickets_remaining -= number_of_tickets
                break
            elif customer_decision.upper() == "N":
                print("Ok, thank you for visiting {}.".format(name))
                break
            else:
                print("That is an invalid entry. Please enter Y or N")
                customer_decision = str(input(f"Would you like to proceed with your purchase {name}? \nEnter Y/N "))
            
print("Sorry, tickets are all sold out!")
    