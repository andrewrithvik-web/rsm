import datetime

class RS_Mobiles:
    def __init__(self):
        self.stock = {}
        self.sales = []

    def add_stock(self, item_name, quantity, price):
        self.stock[item_name] = {"quantity": quantity, "price": price}

    def update_stock(self, item_name, quantity):
        if item_name in self.stock:
            self.stock[item_name]["quantity"] += quantity

    def remove_stock(self, item_name):
        if item_name in self.stock:
            del self.stock[item_name]

    def record_sale(self, item_name, quantity):
        if item_name in self.stock and self.stock[item_name]["quantity"] >= quantity:
            self.stock[item_name]["quantity"] -= quantity
            total_price = quantity * self.stock[item_name]["price"]
            self.sales.append({"item": item_name, "quantity": quantity, "total_price": total_price, "date": datetime.datetime.now()})
            return total_price
        else:
            raise ValueError("Not enough stock available.")

    def generate_invoice(self, sale):
        invoice = f"Invoice Date: {sale['date']}\nItem: {sale['item']}\nQuantity: {sale['quantity']}\nTotal Price: ${sale['total_price']:.2f}"
        return invoice

    def dashboard_statistics(self):
        total_sales = sum(sale['total_price'] for sale in self.sales)
        total_customers = len(self.sales)  # Assuming each sale is a customer for simplicity
        return {
            "Total Sales": total_sales,
            "Total Customers": total_customers,
            "Current Stock": self.stock,
        }

# Example usage
if __name__ == "__main__":
    system = RS_Mobiles()
    # Add, update, remove stock and record sales as needed
