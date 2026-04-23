# 5. Shopping Cart / Billing System
# Students build a store billing project.
# Requirements
# • Add products and prices in a dictionary
# • Let user buy multiple items
# • Quantity support
# • Generate total bill
# • Apply discount if total exceeds some amount
# • Print final invoice
# • Handle invalid product names

products = {
    "apple": 1.5,
    "banana": 0.5,
    "orange": 0.8,
    "milk": 2.0,
    "bread": 1.0
}


print("="*50)
print("     WELCOME TO THE SHOPPING CART SYSTEM")
print("="*50)
print("\nAvailable Products:")
for product, price in products.items():
    print(f"  - {product.capitalize()}: ${price:.2f}")
print("\n👉🏻Enter product name and quantity (e.g., 'apple 3')👈🏻")
print("Type 'done' when finished shopping\n")
print("="*50)
print("Note: If your total exceeds $20, you will receive a 10% discount!")
print("="*50)


class shopping_cart:
    
    def __init__(self,products):
        self.products=products
        self.cart={}
        
    def add_to_cart(self):
        while True:
            user_input = input("Enter product name and quantity: ").strip()
        
            if user_input.lower() == "done":
                break
        
            try:
            # FIX 1: Split input into product name and quantity
                product_name, quantity = user_input.split()
                quantity = int(quantity)
            
            # FIX 2: Convert product name to lowercase for comparison
                product_name = product_name.lower()
            
            # FIX 3: Validate quantity is positive
                if quantity <= 0:
                    print("Quantity must be greater than 0.")
                    continue
            
                if product_name in self.products:
                    if product_name in self.cart:
                        self.cart[product_name]=self.cart.get[product_name,0] + quantity
                    else:
                        self.cart[product_name] = quantity
                    print(f" Added {quantity} {product_name}(s) to cart")
                else:
                    print(f" Invalid product name: '{product_name}'. Please try again.")
        
            except ValueError:
            
                print(" Invalid input format. Please enter: product_name quantity (e.g., 'apple 3')")
        
    def generating_invoice(self):
        # FIX 4: This code should be OUTSIDE the while loop (indentation fixed)
        print("\n" + "="*50)
        print(f"{'INVOICE':^50}")
        print("="*50)

        total_bill = 0

        # Check if cart is empty
        if not cart.cart:
            print("Your cart is empty. No purchase made.")
        else:
            print(f"{'Product':<15} {'Qty':<5} {'Price':<10} {'Total':<10}")
            print("-"*50)
            
            for product, quantity in cart.cart.items():
                price = products[product]
                product_total = price * quantity
                total_bill += product_total
                print(f"{product.capitalize():<15} {quantity:<5} ${price:<9.2f} ${product_total:.2f}")
            
            print("-"*50)
            print(f"Subtotal: ${total_bill:.2f}")
            
            # FIX 5: Apply discount logic
            if total_bill > 20:
                discount = total_bill * 0.1
                total_bill -= discount
                print(f"Discount (10%): -${discount:.2f}")
            
            print("="*50)
            print(f"FINAL BILL: ${total_bill:.2f}")
            print("="*50)
            print("\n Thank you for shopping with us!\n")

    
cart = shopping_cart(products)
cart.add_to_cart() 
cart.generating_invoice()



