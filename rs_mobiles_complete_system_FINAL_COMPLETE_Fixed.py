class DashboardWindow:
    def load_stats(self):
        try:
            # Assume some database connection and cursor
            # Example SQL using COALESCE
            query = "SELECT COALESCE(SUM(sales), 0) as today_sales, COALESCE(COUNT(bill_id), 0) as bills_count, COALESCE(SUM(monthly_sales), 0) as monthly_sales, COALESCE(COUNT(customer_id), 0) as total_customers FROM sales_data"
            cursor.execute(query)
            result = cursor.fetchone()

            # Set the statistics
            self.today_sales = result[0]
            self.bills_count = result[1]
            self.monthly_sales = result[2]
            self.total_customers = result[3]

            # Debug logging (this is just an example, replace with your logging implementation)
            print(f"Today's Sales: {self.today_sales}")
            print(f"Bills Count: {self.bills_count}")
            print(f"Monthly Sales: {self.monthly_sales}")
            print(f"Total Customers: {self.total_customers}")

        except Exception as e:
            # Handle any errors that occur during the loading of stats
            print(f"Error loading stats: {e}")
