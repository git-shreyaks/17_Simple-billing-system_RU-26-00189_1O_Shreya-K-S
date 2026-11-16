#simple billing system 
# Product  dictionary
products = {
    "Rice": 50,
    "Sugar": 40,
    "Oil": 120
}

def add_item(bill_items):
    print("\n-----------------------------------")
    item = input("Add item (Rice/Sugar/Oil): ").capitalize()
    
    # Check if item exists in dictionary
    if item not in products:
        print("(a) Invalid product. Available: Rice, Sugar, Oil")
        return
        
    # Check quantity input
    try:
        qty = int(input("Quantity: "))
    except ValueError:
        print("(b) Quantity must be at least 1.")
        return
        
    if qty < 1:
        print("(b) Quantity must be at least 1.")
        return
        
    # Append item and quantity as a tuple to the list
    bill_items.append((item, qty))
    
    # Show  expected output format
    amount = products[item] * qty
    print(f"-> {item} x{qty} added successfully | Amount: {amount}")

def generate_bill(bill_items):
    if len(bill_items) == 0:
        print("\nNo items in the bill yet!")
        return
        
    subtotal = 0
    bill_content = "\n=== CUSTOMER BILL ===\n"
    
    # Loop of list of items
    for item, qty in bill_items:
        price = products[item]
        cost = price * qty
        subtotal += cost
        bill_content += f"{item} x{qty} = {cost}\n"
        
    # Calculate 5% GST and Grand Total
    gst = subtotal * 0.05
    grand_total = subtotal + gst
    
    # Add totals and thank you message to the bill content string
    bill_content += f"---------------------\n"
    bill_content += f"Subtotal: {subtotal}\n"
    bill_content += f"GST (5%): {gst:.2f}\n"
    bill_content += f"Grand Total: {grand_total:.2f}\n"
    bill_content += f"---------------------\n"
    bill_content += "Thank you for shopping with us!\n"
    
    # Print bill 
    print(bill_content)
    
    # Save bill to text file with error handling for online compilers
    try:
        f = open("bill.txt", "w")
        f.write(bill_content + "Bill saved to bill.txt")
        f.close()
        print("Bill saved to bill.txt successfully!")
    except PermissionError:
        print("Note: File saving is restricted in this online environment, but the bill calculation above is correct.")

def main():
    bill_items = []
  # list to store bill items
    
    print("=" * 35)
    print("      SIMPLE BILLING SYSTEM      ")
    print("=" * 35)
    print("Products available:")
    print(" • Rice : Rs. 50")
    print(" • Sugar: Rs. 40")
    print(" • Oil  : Rs. 120")
    print("=" * 35)
    
    while True:
        print("\n[ Menu ]")
        print("1. Add item")
        print("2. Generate bill")
        choice = input("Enter your choice (1 or 2): ")
        
        if choice == '1':
            add_item(bill_items)
        elif choice == '2':
            generate_bill(bill_items)
            break
        else:
            print("Invalid choice! Please enter 1 or 2.")

if __name__ == "__main__":
    main()