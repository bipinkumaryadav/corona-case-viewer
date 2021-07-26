import sqlite3


# This is data sending function
def data_send(name):
    conn = sqlite3.connect('database.db')   # change database name from 'database.db' to 'your_database_name.db'
    cnc = conn.cursor()
    try:
        print("Table is going to create")
        cnc.execute(f"""CREATE TABLE Scan(number, name)""")
        cnc.execute(f"""INSERT INTO Scan(number, name) VALUES (?, ?)""", (0, name))
        conn.commit()
        print("created")

    except:
        print("process aborted")

    print("Insertion is done")


    cnc.execute("SELECT * FROM Scan")
    row = cnc.fetchall()
    for val in row:
        if val[1] == name:
            flag = 1
            index =
    if len(row) == 1:
        num = 1
        print("ok")
        cnc.execute(f'CREATE TABLE {name}{num}(number, domain)')
        cnc.execute(f"""INSERT INTO Scan(number, name) VALUES (?, ?)""", (num, name))
        conn.commit()


    elif flag == 1:
        num = row[-1][0]
        print(num)
        try:
            cnc.execute(f'CREATE TABLE {name}{num}(number, domain)')
        except:
            pass
        cnc.execute(f"""INSERT INTO Scan(number, name) VALUES (?, ?)""", ((num + 1), name))
        conn.commit()



    # for i in range(len(data)):
    #     cnc.execute(f"""INSERT INTO Scans{num} (number, domain) VALUES (?, ?)""", (i + 1, data[i]))
    # conn.commit()

# domains = ['abc.com', 'cde.com']
# data_send(12, domains)
con = sqlite3.connect('database.db')

c = con.cursor()

data_send('zomato')

# This is used to fetch data from the database just change the table name
c.execute("SELECT * FROM Scan")
row = c.fetchall()
print(row)
for i in row:
    print("okay")

