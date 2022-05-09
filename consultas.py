import sqlite3

con = sqlite3.connect("data/datos.db")
cur = con.cursor()

cur.execute("""
            SELECT fecha, hora, from, Qfrom, to, Qto
            FROM movements
            ORDER BY fecha
            """
            )
l = cur.fetchall()
con.close()


