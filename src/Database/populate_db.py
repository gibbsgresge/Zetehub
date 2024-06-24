import sqlite3
import csv

def populate_database(db_file, csv_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    with open('brothers.csv', 'r') as file:
        reader = csv.DictReader(file)  # Read as a dictionary

        for row in reader:
            cursor.execute(
                '''
                INSERT INTO members (name, pledge_class, major, year_graduating, linkedin_url, image_url, email)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                ''',
                (
                    row['name'], 
                    row['pledge_class'], 
                    row['major'], 
                    row['year_graduating'],
                    row['linkedin_url'],
                    row['image_url'],
                    row['email'] 
                    
                )
            )

    conn.commit()
    conn.close()

if __name__ == '__main__':
    populate_database('fraternity.db', 'brothers.csv')