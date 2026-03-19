# Complete Fixed Billing System

class BillingSystem:
    def __init__(self):
        self.customers = []
        self.stock = {}
        self.sales_data = []

    def add_customer(self, customer_name):
        self.customers.append(customer_name)

    def update_stock(self, item, quantity):
        if item in self.stock:
            self.stock[item] += quantity
        else:
            self.stock[item] = quantity

    def generate_invoice(self, customer_name, item, quantity):
        if item not in self.stock or self.stock[item] < quantity:
            raise Exception("Insufficient stock")
        self.stock[item] -= quantity
        invoice = f"Invoice for {customer_name}:\nItem: {item}\nQuantity: {quantity}\nTotal: ${self.calculate_total(item, quantity)}"
        self.sales_data.append(invoice)
        return invoice

    def calculate_total(self, item, quantity):
        # Placeholder for item price lookup
        item_price = 10  # Example item price
        return item_price * quantity

    def display_dashboard(self):
        print(f"Total Customers: {len(self.customers)}")
        print("Stock Details:")
        for item, quantity in self.stock.items():
            print(f"{item}: {quantity}")
        print("Sales Data:")
        for sale in self.sales_data:
            print(sale)

# Example usage:

billing_system = BillingSystem()
billing_system.add_customer("John Doe")
billing_system.update_stock("Product A", 100)

try:
    print(billing_system.generate_invoice("John Doe", "Product A", 2))
except Exception as e:
    print(e)

billing_system.display_dashboard()