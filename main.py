import psycopg2

def create_table():
    # Establish a connection to the database
    conn = psycopg2.connect(
    
        host="localhost",
        database="mydatabase",
        user="postgres",
        password="root"
    )
    
    try:
        # Create a cursor to execute SQL commands
        cursor = conn.cursor()

        # SQL command to create the table
        create_table_query = '''
            CREATE TABLE food (
                id serial PRIMARY KEY,
                name VARCHAR(50),
                kg VARCHAR(100)
            )
        '''

        # Execute the SQL command to create the table
        cursor.execute(create_table_query)

        # Commit the transaction
        conn.commit()

        # Close the cursor
        cursor.close()

    except psycopg2.OperationalError as e:
        print("Error:", e)

