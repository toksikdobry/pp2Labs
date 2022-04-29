Yelaman, [29.04.2022 22:44]
import psycopg2 
def create(): 
    conn = psycopg2.connect(database = 'pp2', user = 'postgres', password = '12345') 
    cur = conn.cursor() 
    cur.execute( 
        ''' 
        CREATE TABLE phonebook ( 
            id INTEGER PRIMARY KEY, 
            name VARCHAR(50), 
            last_name VARCHAR(50), 
            phone_number VARCHAR(50) 
        ); 
        ''') 
    conn.commit() 
    cur.close() 
 
 
def show(): 
    conn = psycopg2.connect(database = 'pp2', user = 'postgres', password = '12345') 
    cur = conn.cursor() 
    cur.execute( 
        ''' 
        SELECT * FROM phonebook;  
        ''') 
    conn.commit() 
    cur.close() 
 
      
 
def insert(name, phoneNumber): 
    conn = psycopg2.connect(database = 'pp2', user = 'postgres', password = '12345') 
    cur = conn.cursor() 
    cur.execute( 
        ''' 
        INSERT INTO phonebook ( 
            name, 
            last_name, 
            phone_number 
        ) 
        VALUES (%s, %s) 
        ''', (name, phoneNumber)) 
    conn.commit() 
    cur.close() 
 
 
def main(): 
    print('Your name:') 
    name = input() 
    print('Your phone number:') 
    phoneNumber = input() 
    insert(name, phoneNumber)