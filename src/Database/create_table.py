import sqlite3

def create_brothers_table(db_file):
    """Creates the 'brothers' table in the specified SQLite database file."""
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # Create the table
    cursor.execute('''
        CREATE TABLE members (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            pledge_class TEXT, 
            major TEXT, 
            year_graduating INTEGER,
            linkedin_url TEXT,
            image_url TEXT, 
            email TEXT 
        )
    ''')

    conn.commit()  # Save the changes
    conn.close()  # Close the connection

# Example usage:
create_brothers_table('fraternity.db')  # Replace 'fraternity.db' with your actual database filename