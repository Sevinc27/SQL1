import sqlite3
connection = sqlite3.connect("databaza1.db")
cursor = connection.cursor()

#task1

def create_products_sold_table():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products_sold (
            product_id INTEGER,
            quantity INTEGER,
            unit_price REAL
        )
    """)
    connection.commit()

def get_total_revenue():
    cursor.execute("""
        SELECT product_id, SUM(quantity * unit_price) AS total_revenue
        FROM products_sold
        GROUP BY product_id
        ORDER BY total_revenue DESC
    """)
    data = cursor.fetchall()
    for row in data:
        print(row)

create_products_sold_table()

get_total_revenue()


#task2

def create_employees_table():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            name TEXT,
            salary REAL,
            department TEXT
        )
    """)
    connection.commit()

def get_high_salary_sales_employees():
    cursor.execute("""
        SELECT name, salary
        FROM employees
        WHERE department='satış' AND salary > 600
        ORDER BY salary DESC
    """)
    data = cursor.fetchall()
    for row in data:
        print(row)

create_employees_table()

get_high_salary_sales_employees()



#task3

def create_books_table():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            title TEXT,
            genre TEXT,
            publication_year INTEGER
        )
    """)
    connection.commit()

def get_books_published_after_2015():
    cursor.execute("""
        SELECT title, genre, publication_year
        FROM books
        WHERE publication_year > 2015
        ORDER BY genre ASC
    """)
    data = cursor.fetchall()
    for row in data:
        print(row)

create_books_table()

get_books_published_after_2015()


#task4

def create_movies_table():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS movies (
            title TEXT,
            release_date INTEGER,
            rating REAL
        )
    """)
    connection.commit()

def get_movies_before_2000_and_high_rating():
    cursor.execute("""
        SELECT title, release_date, rating
        FROM movies
        WHERE release_date < 2000
        ORDER BY release_date ASC, rating DESC
    """)
    data = cursor.fetchall()
    for row in data:
        print(row)

create_movies_table()

get_movies_before_2000_and_high_rating()