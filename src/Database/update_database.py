import sqlite3

conn = sqlite3.connect('fraternity.db')
cursor = conn.cursor()

# Update the image URL for a specific brother
cursor.execute("UPDATE members SET image_url = 'ZachLandow.JPEG' WHERE id = 5")
cursor.execute("UPDATE members SET image_url = 'Kuzi2.JPEG' WHERE id = 3")
cursor.execute("UPDATE members SET image_url = 'JoshMontovano.JPEG' WHERE id = 10")
cursor.execute("UPDATE members SET image_url = 'NicolasCorica.JPEG' WHERE id = 21")
cursor.execute("UPDATE members SET image_url = 'AustinBorrotto.JPG' WHERE id = 11")

conn.commit()  # Commit all the changes
conn.close()