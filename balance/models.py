import sqlite3


class ProcesaDatos:

    def recupera_datos(self):
        con = sqlite3.connect("data/datos.db")
        cur = con.cursor()

        cur.execute("""
                           SELECT fecha, hora, origen, Qfrom, destino, Qto
                               FROM movements
                           ORDER BY fecha;
                       """
        )

        return cur.fetchall()

    def investment(self):
        con = sqlite3.connect("data/datos.db")
        cur = con. cursor()

        cur.execute("""
                    SELECT Qfrom;
                    FROM movements;
                    WHERE origen="EUR"
                    """
                    )

        amount = cur.fetchall()
        return amount


    def graba_datos(self, params):
        con = sqlite3.connect("data/datos.db")
        cur = con.cursor()

        cur.execute("""
        INSERT INTO movements (fecha, hora, origen, Qfrom, destino, Qto)
                        values (?, ?, ?, ?, ?, ?)""", params)

        con.commit()
        con.close()








