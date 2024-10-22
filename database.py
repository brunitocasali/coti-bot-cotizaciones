import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
connection = sqlite3.connect('cotizaciones.db')

# Create a cursor object
cursor = connection.cursor()

# Create the COTI_USD table
create_table_query = """
CREATE TABLE IF NOT EXISTS COTI_USD
(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    PORTAL TEXT NOT NULL,
    FECHA DATETIME NOT NULL,
    COMPRA FLOAT NULL,   -- Allow NULL values for COMPRA
    VENTA FLOAT NOT NULL,
    VARIACION FLOAT NOT NULL
);
"""

# Execute the create table query
cursor.execute(create_table_query)

# Commit the changes and close the connection
connection.commit()

print("COTI_USD table created successfully.")
