import mysql.connector as mysql


def connect(db_name):
    try:
        return mysql.connect(
            host="localhost",
            user="root",
            password="numlock29032416",
            database=db_name
        )
    except Exception as e:
        print(e)


db = connect("user")
cursor = db.cursor()
# cursor.execute("select * from products")
# emp_record = cursor.fetchall()
# print(emp_record)
# my_pro = ("led", "sdf", "10", "drf", "dg")
# cursor.execute(
#     '''insert into products(name,imageurl,price,category,brand) values (%s,%s,%s,%s,%s)''', my_pro)
my_task = [("1", "dfv", 20, "srdfv", "rdfgv"), ("2", "dfv", 30,
                                                "egt", "wer"), ("3", "dfv", 15, "tyh", "yfth")]
cursor.executemany(
    '''insert into products(name,imageurl,price,category,brand) values (%s,%s,%s,%s,%s)''', my_task)
db.commit()
db.close()
