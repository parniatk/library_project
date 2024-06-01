import sqlite3
#ایجاد دیتابیس
def connect():
    conn = sqlite3.connect("book.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY,title text,author text,year INTEGER,Isbn INTEGER)")
    conn.commit()
    conn.close()
# فانکشن مربوط به افزودن اطلاعات
def insert (title , author, year, Isbn):
    conn = sqlite3.connect("book.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO book VALUES (null , ?,?,?,?)" ,(title, author, year, Isbn))
    conn.commit()
    conn.close()
#فانکشن برای دریافت ایتم های داخل دیتابیس
def view():
    conn = sqlite3.connect("book.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
#دریافت اطلاعات
    rows = cur.fetchall()
    conn.close()
    return rows

def search(title="", author ="", year ="", Isbn =""):
    conn = sqlite3.connect("book.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book WHERE title = ? OR author=? OR year =? OR Isbn=?",(title, author, year, Isbn))
    row = cur.fetchall()
    conn.close()
    return row
def delete(id):
    conn = sqlite3.connect("book.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM book WHERE id = ?",(id,))
    conn.commit()
    conn.close()

def update(id, title, author, year, Isbn) :
    conn = sqlite3.connect("book.db")
    cur = conn.cursor()
    cur.execute("UPDATE book SET title=?, author=?, year=?, Isbn=? WHERE id = ?" ,(title, author, year, Isbn, id))
    conn.commit()
    conn.close()

connect()
#update(1,"new book title", "new author", 2020, 25482)
#print(search())