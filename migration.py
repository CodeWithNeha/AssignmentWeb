import mysql.connector

# # Database Connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="todotask"
)

# Create tasks table if it doesn't exist
cursor = db.cursor()
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS tasks (
        id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(255) NOT NULL,
        description VARCHAR(255)
    )
    """
)
db.commit()