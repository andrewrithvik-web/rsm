# rs_mobiles_complete_system_FINAL_FIXED.py

# This Python script is a complete corrected version that fixes the bill_items insert statement to include all 7 columns.

import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('rsm.db')
cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS bill_items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    bill_no TEXT,
    product_code TEXT,
    product_name TEXT,
    quantity INTEGER,
    unit_price REAL,
    cost_price REAL
)
''')

# Insert statement with all columns accounted for (NULL for id)
insert_statement = '''
INSERT INTO bill_items (id, bill_no, product_code, product_name, quantity, unit_price, cost_price)
VALUES (NULL, ?, ?, ?, ?, ?, ?)
'''

# Sample data to insert
sample_data = (
    'B001', 'P001', 'Product Name 1', 5, 10.5, 7.0
)

# Execute the insert statement
cursor.execute(insert_statement, sample_data)
conn.commit()

# Close the database connection
conn.close()