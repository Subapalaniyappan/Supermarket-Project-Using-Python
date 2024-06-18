available_items = {
    "vegetables": {
        "carrot": 120,
        "onion": 55,
        "bitter_gourd": 30,
        "potato": 30
    },
    "dairy_products": {
        "milk": 52,
        "curd": 25,
        "cheese": 70,
        "butter": 45
    },
    "snacks": {
        "popcorn": 75,
        "nuts": 150,
        "ice_cream": 50,
        "juice": 30
    },
    "fruits": {
        "apple": 250,
        "papaya": 40,
        "banana": 25,
        "watermelon": 65
    },
    "foods": {
        "pasta": 60,
        "noodles": 100,
        "chicken_rice": 120,
        "cake": 70
    }
}

def print_available_items():
    print("Available items:")
    for category, items in available_items.items():
        print(f"{category.capitalize()}:")
        for item, price in items.items():
            print(f"{item}: Rs.{price}")

def calculate_total_cost(orders):
    total_cost = 0
    for item, quantity in orders:
        category = get_item_category(item)
        if category:
            price = available_items[category][item]
            total_cost += price * quantity
            gst_rate=18
            gst_price=total_cost*18/100
            net_amount=total_cost+gst_price
            print(f"GST price is {gst_price}at GST Rate {gst_rate}% ")
            print(f"Total cost of the product after appling GST = {net_amount} ")
            f=open("bill.txt","w")
            f.write(f" Total cost of the product after appling GST = {net_amount} ")
            print("Bill Generated Successfully")
    return total_cost

def get_item_category(item):
    for category, items in available_items.items():
        if item in items:
            return category
    return None

def main():
    orders = []

    print("Welcome to Kannan SuperMarket")
    print_available_items()

    while True:
        your_order = input("Enter your order (or 'done' to finish): ").strip().lower()
        
        if your_order == 'done':
            break
        
        # Check if the item is available
        category = get_item_category(your_order)
        if category:
            print(f"Yes, {your_order} is available in {category.capitalize()}.")
        else:
            print(f"Sorry, {your_order} is not available.")
            continue
        
        try:
            how_many = int(input(f"How many {your_order} do you want: "))
            if how_many <= 0:
                print("Please enter a valid quantity.")
                continue
        except :
            print("Invalid input. Please enter a number.")
            continue
        
        # Add the current order to the list
        orders.append((your_order, how_many))
        
        # Ask if the customer wants to continue shopping
        customer_input = input("If you want to continue shopping, enter 'yes', otherwise 'no': ").strip().lower()
        if customer_input != 'yes':
            break

    # Print the final order and total cost
    print("\nYour order summary:")
    for order in orders:
        item, quantity = order
        print(f"{item}: {quantity}")
    
    total_cost = calculate_total_cost(orders)
    print(f"Total cost: Rs.{total_cost}")

# Call the main function to start the program
if __name__ == "__main__":
    main()
import smtplib
import random
def email_sending():
    try:
        receiver_mail=["19uma063@ksrcas.edu"]
        for i in receiver_mail:
            print(i,"Thank you for Shopping Us \n Have a Nice Day :) ")
            s=smtplib.SMTP('smtp.gmail.com',587)
            s.starttls()
            s.login("subadurai2001@gmail.com","wapg swso ilri")
            message="Thanks for Visiting"
            s.sendmail("subadurai2001@gmail.com",i,message)
            s.quit
            print("Mail Sent Successfully")
    except:
        print("Mail Not Sent")
email_sending()