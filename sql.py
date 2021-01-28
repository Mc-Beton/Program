import sqlite3
from sqlite3 import Error


# polączenie z bazą danych
def create_connection(db_file):
   conn = None
   try:
       conn = sqlite3.connect(db_file)
       return conn
   except Error as e:
       print(e)

   return conn

# stworzenie nowej tabeli
def execute_sql(conn, sql):
   try:
       c = conn.cursor()
       c.execute(sql)
   except Error as e:
       print(e)

# dodanie nowej pozycji do tabeli projekts
def add_projekt(conn, projekt):
   """
   Create a new projekt into the projects table
   :param conn:
   :param projekt:
   :return: projekt id
   """
   sql = '''INSERT INTO projects(nazwa, start_date, end_date)
             VALUES(?,?,?)'''
   cur = conn.cursor()
   cur.execute(sql, projekt)
   conn.commit()
   return cur.lastrowid

db_file="Baza.db"


create_client_sql = """
    -- client
    CREATE TABLE IF NOT EXISTS client (
        id integer PRIMARY KEY,
        name text NOT NULL,
        surname text NOT NULL,
        tel1 text NOT NULL,
        tel2 text,
        loc text,
        info text
    );
    """

create_order_sql = """
    -- orders
    CREATE TABLE IF NOT EXISTS orders (
        id integer PRIMARY KEY,
        client_id integer NOT NULL,
        product_id integer NOT NULL,
        adds_id integer NOT NULL,
        finish_id integer NOT NULL,
        head_id integer NOT NULL,
        writing_id integer NOT NULL,
        info text,
        FOREIGN KEY (client_id) REFERENCES client (id),
        FOREIGN KEY (product_id) REFERENCES product (id),
        FOREIGN KEY (adds_id) REFERENCES adds (id),
        FOREIGN KEY (finish_id) REFERENCES path (id),
        FOREIGN KEY (head_id) REFERENCES head (id),
        FOREIGN KEY (writing_id) REFERENCES writing (id)
    );
    """

create_product_sql = """
    -- product
    CREATE TABLE IF NOT EXISTS product (
        id integer PRIMARY KEY,
        kind text NOT NULL,
        finish text NOT NULL,
        parapet text NOT NULL,
        mat1 text NOT NULL,
        cokoly text NOT NULL,
        mat2 text NOT NULL,
        plyta text NOT NULL,
        thick text NOT NULL,
        mat3 text NOT NULL,
        info text
    );
    """
    
create_adds_sql = """
    -- adds
    CREATE TABLE IF NOT EXISTS adds (
        id integer PRIMARY KEY,
        wazon text NOT NULL,
        info1 text,
        podstawa text NOT NULL,
        info2 text,
        lampion text NOT NULL,
        info3 text,
        photo text NOT NULL,
        info4 text,
        cross text NOT NULL,
        info5 text
    );
    """

create_path_sql = """
    -- path
    CREATE TABLE IF NOT EXISTS path (
        id integer PRIMARY KEY,
        kind text NOT NULL,
        border text NOT NULL,
        info text
    );
    """

create_writing_sql = """
    -- writing
    CREATE TABLE IF NOT EXISTS writing (
        id integer PRIMARY KEY,
        content text NOT NULL,
        kind text NOT NULL,
        info text
    );
    """

create_head_sql = """
    -- head
    CREATE TABLE IF NOT EXISTS head (
        id integer PRIMARY KEY,
        name text NOT NULL,
        thick text NOT NULL,
        mat1 text NOT NULL,
        mat2 text,
        info text
    );
    """

create_material_sql = """
    -- material
    CREATE TABLE IF NOT EXISTS material (
        id integer PRIMARY KEY,
        name text NOT NULL,
        price text NOT NULL,
        info text,
        photo BLOB
    );
    """

create_heads_sql = """
    -- heads
    CREATE TABLE IF NOT EXISTS heads (
        id integer PRIMARY KEY,
        name text NOT NULL,
        photo text NOT NULL
    );
    """

create_cross_sql = """
    -- cross
    CREATE TABLE IF NOT EXISTS cross (
        id integer PRIMARY KEY,
        name text NOT NULL,
        price text NOT NULL
    );
    """

create_wazon_sql = """
    -- wazon
    CREATE TABLE IF NOT EXISTS wazon (
        id integer PRIMARY KEY,
        name text NOT NULL,
        price text NOT NULL
    );
    """

create_photo_sql = """
    -- photo
    CREATE TABLE IF NOT EXISTS photo (
        id integer PRIMARY KEY,
        name text NOT NULL,
        price text NOT NULL
    );
    """

create_podst_sql = """
    -- podst
    CREATE TABLE IF NOT EXISTS podst (
        id integer PRIMARY KEY,
        name text NOT NULL,
        price text NOT NULL
    );
    """

create_letters_sql = """
    -- letters
    CREATE TABLE IF NOT EXISTS letters (
        id integer PRIMARY KEY,
        name text NOT NULL,
        price text NOT NULL
    );
    """

create_lampion_sql = """
    -- lampion
    CREATE TABLE IF NOT EXISTS lampion (
        id integer PRIMARY KEY,
        name text NOT NULL,
        price text NOT NULL
    );
    """

def add_client(conn, client):
   """
   Create a new client into the client table
   :param conn:
   :param client:
   :return: client id
   """
   sql = '''INSERT INTO client(name, surname, tel1, tel2, loc, info)
             VALUES(?,?,?,?,?,?)'''
   cur = conn.cursor()
   cur.execute(sql, client)
   conn.commit()
   return cur.lastrowid


def add_material(connn, material):
    sql = '''INSERT INTO material(name, price, info, photo)
             VALUES(?,?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql, material)
    conn.commit()
    return cur.lastrowid



conn = create_connection(db_file)
if conn is not None:
    

    execute_sql(conn, create_order_sql)
    execute_sql(conn, create_client_sql)
    execute_sql(conn, create_product_sql)
    execute_sql(conn, create_adds_sql)
    execute_sql(conn, create_path_sql)
    execute_sql(conn, create_writing_sql)
    execute_sql(conn, create_head_sql)
    execute_sql(conn, create_material_sql)
    execute_sql(conn, create_heads_sql)
    execute_sql(conn, create_cross_sql)
    execute_sql(conn, create_wazon_sql)
    execute_sql(conn, create_photo_sql)
    execute_sql(conn, create_podst_sql)
    execute_sql(conn, create_letters_sql)
    execute_sql(conn, create_lampion_sql)
    
    conn.close()


