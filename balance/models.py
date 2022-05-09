import sqlite3

coin_list = ['BTC', 'ETH', 'BNB', 'BCH', 'LINK', 'LUNA', 'ATOM', 'SOL', 'USDT']


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

    def graba_datos(self, params):
        con = sqlite3.connect("data/datos.db")
        cur = con.cursor()

        cur.execute("""
        INSERT INTO movements (fecha, hora, origen, Qfrom, destino, Qto)
                        values (?, ?, ?, ?, ?, ?)""", params)

        con.commit()
        con.close()





