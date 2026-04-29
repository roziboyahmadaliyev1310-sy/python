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



print("WELCOME TO THE SHOPPING CART SYSTEM")
def display_products(products):
    print("\nAvailable Products:")
    for product, price in products.items():
        print(f"  - {product.capitalize()}: ${price}")
        
print("\nEnter product name and quantity")
print("Type 'done' when finished shopping\n")

print("Note: If your total exceeds $20, you will receive a 10% discount!")



class shopping_cart:
    
    def __init__(self,products):
        self.products=products
        self.cart={}
        
    def add_to_cart(self):
        display_products(self.products)
        while True:
            user_input = input("Enter product name or 'done' to finish shopping: ").strip()
        
            if user_input.lower()=="done":
                break
            elif user_input.lower() not in self.products:
                print(f" Invalid product name: '{user_input}'. Please try again.")
                continue
            
            quantity_1 = input("Enter quantity: ").strip()
        
            try:
                quantity = int(quantity_1)
                product_name = user_input.lower()
            
                if quantity <= 0:
                    print("Quantity must be greater than 0.")
                    continue
            
                if product_name in self.products:
                    if product_name in self.cart:
                        self.cart[product_name] += quantity
                    else:
                        self.cart[product_name] = quantity
                    print(f" Added {quantity} {product_name}(s) to cart")
                    print("if you want to add more products, please enter the product name or type 'done' to finish shopping.")
                    display_products(self.products)
                    
                else:
                    print(f" Invalid product name: '{product_name}'. Please try again.")
        
            except ValueError:
            
                print(" Invalid input format. Please enter: product_name quantity")
        
    def generating_invoice(self):
        print("\n" + "*"*60)
        print(f"{'INVOICE':^40}")

        total_bill = 0
       
        if not self.cart:
            print("Your cart is empty. No purchase made.")
        else:
            print(f"{'Product':<15} {'Qty':<10} {'Price':<10} {'Total':<10}")
            
            for product, quantity in self.cart.items():
                price = self.products[product]
                product_total = price * quantity
                total_bill += product_total
                print(f"{product.capitalize():<15} {quantity:<10} ${price:<9} ${product_total:<9}")
            
            print(f"Subtotal: ${total_bill}")
            
            
            if total_bill > 20:
                discount = total_bill * 0.1
                total_bill -= discount
                print(f"Discount (10%): -${discount}")
            
            print(f"FINAL BILL: ${total_bill}")

    
cart = shopping_cart(products)
cart.add_to_cart() 
cart.generating_invoice()



