import psycopg2 as pg

conn = pg.connect(host="localhost", dbname="postgres", user="postgres",
                  password="awesome password", port=5432)

cur = conn.cursor()

cur.execute("""DROP TABLE PhoneBook""")

cur.execute("""CREATE TABLE IF NOT EXISTS PhoneBook(
    id INT PRIMARY KEY,
    name VARCHAR(255),
    phone VARCHAR(255)
);
""")

current_id = 1
while 1 == 1:
    print("-------------")
    should_we = input("What would you like to do?\n commands: 'ADD', 'CHANGE', 'QUERY', 'DELETE', 'STOP'\n")
    if should_we == "ADD":
        adding_name = input("Please input the person's name (no spaces!): ")
        adding_num = input("Please input their phone number: ")
        cur.execute(f'''INSERT INTO PhoneBook (id, name, phone) VALUES
                ({current_id}, '{adding_name}', '{adding_num}')
        ''')
        current_id += 1
    elif should_we == "CHANGE":
        whose = input("Whose values are changed?: ")
        what = input("What are we changing? NAME or NUMBER?: ")
        if what == "NAME" or what == "name":
            into = input("Write a new name: ")
            cur.execute(f'''UPDATE PhoneBook
                        SET name = "{into}"
                        WHERE name = "{whose}";''')
        elif what == "NUMBER" or what == "number":
            into = input("Write a new number: ")
            cur.execute(f'''UPDATE PhoneBook
                        SET phone = "{into}"
                        WHERE name = "{whose}";''')
        else:
            print("Canceled due to confusion")
    elif should_we == "STOP":
        break
    else:
        print("???")

conn.commit()
cur.close()
conn.close()