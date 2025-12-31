# Import required libraries
import sqlite3

# Define a function to create a database
def create_database():
    # Connect to the SQLite database
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    # Create a table
    cursor.execute('CREATE TABLE IF NOT EXISTS data (id INTEGER PRIMARY KEY, value REAL)')
    
    # Close the connection
    conn.close()
