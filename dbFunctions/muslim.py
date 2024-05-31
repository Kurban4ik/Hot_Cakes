import sqlite3

db_absolyte_way = r"C:\Users\03\PycharmProjects\hot_cakes\main_database.sqlite"


def add_last_ip(id, ip, datetime):
    con = sqlite3.connect(db_absolyte_way)
    cur = con.cursor()

    cur.execute(f'''UPDATE All_workers SET Last_Ip = "{ip}", Last_Ip_Time = "{datetime}" WHERE ID = {id}''')
    con.commit()
    con.close()
    print("\n", id, ip, datetime, "\n")


def add_worker(name, slug, company):
    con = sqlite3.connect(db_absolyte_way)
    cur = con.cursor()
    cur.execute(f'''INSERT INTO All_Workers(Name, Link, Company) VALUES("{name}", "{slug}", "{company}")''')
    con.commit()
    con.close()


def worker_checker(id, company):
    con = sqlite3.connect(db_absolyte_way)
    cur = con.cursor()
    cur.execute(f'''SELECT Name FROM All_Workers WHERE Name={id} AND Company="{company}")''')
    if cur.fetchall():
        con.close()
        return True
    else:
        return False


def save_data(ip, slug, company, time):
    con = sqlite3.connect(db_absolyte_way)
    cur = con.cursor()
    acc1 = [i[0] for i in cur.execute(f'''SELECT IP FROM Requests WHERE
     IP = "{ip}" AND COMPANY = "{company}"''').fetchall()]
    user = [i[0] for i in cur.execute(f'''SELECT ID FROM All_Workers WHERE link = "{slug}"''').fetchall()]
    id = user[0]
    add_last_ip(id, ip, time)
    print(acc1)
    print('1')
    if not acc1:
        print('2')
        print(slug)
        user = [i[0] for i in cur.execute(f'''SELECT ID FROM All_Workers WHERE link = "{slug}"''').fetchall()]
        id = user[0]
        cur.execute(f'''INSERT INTO Requests(IP, Workers_ID, COMPANY, time) VALUES("{ip}", {id}, "{company}", "{time}")''')
        con.commit()
    con.close()


def get_company(name):
    con = sqlite3.connect(db_absolyte_way)
    cur = con.cursor()
    res = list(set(cur.execute(f'''
    SELECT ID FROM All_Workers WHERE Name = {name}
    ''').fetchall()))
    all_1 = list(set(cur.execute(f'''
    SELECT * FROM requests''').fetchall()))
    out = {'lays': 0, 'pinterest': 0}
    for i in res:
        out[cur.execute(f'''SELECT COMPANY FROM Requests WHERE Workers_ID = {i[0]}''').fetchall()[0][0]] += \
            len(cur.execute(f'''SELECT COMPANY FROM Requests WHERE Workers_ID = {i[0]}''').fetchall())
    return out

def get_amount(name):
    con = sqlite3.connect(db_absolyte_way)
    cur = con.cursor()
    res = cur.execute(f'''
SELECT r.IP FROM requests AS r
JOIN All_workers AS a ON r.Workers_ID = a.ID
''').fetchall()
    res = list(set([i[0] for i in res]))
    return len(res)