
import pymysql
create_table_sql = """\
    CREATE TABLE trending
    (
        id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(255) NOT NULL ,
        abstract VARCHAR(255) NOT NULL ,
        nickname VARCHAR(255) NOT NULL,
        comments VARCHAR(255) NOT NULL,
        likes VARCHAR(255) NOT NULL,
        money VARCHAR(255) NOT NULL
    )
    """

con = pymysql.connect("localhost", "root", "op90--", "test", charset='utf8')
with con:
    cur = con.cursor()
    cur.execute(create_table_sql)
    rows = cur.fetchall()
    for row in rows:
        print(row)

