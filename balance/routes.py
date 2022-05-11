import sqlite3
from balance import app
from flask import render_template, flash, request, redirect, url_for
from balance.models import ProcesaDatos
import sqlite3
from balance.forms import MovimientosForm
from datetime import date, datetime
import requests


@app.route('/')
def inicio():
    data_manager = ProcesaDatos()
    try:
        datos = data_manager.recupera_datos()
        return render_template('movimientos.html', movimientos=datos)
    except sqlite3.Error as e:
        flash("Se ha producido un error en la base de datos. Inténtelo más tarde.")
        return render_template('movimientos.html', movimientos=[])


@app.route('/calcular', methods=['POST'])
def resultado():
    """Route where we send calculator form input"""
    form = MovimientosForm()
    origen = request.form['origen']
    Qfrom = float(request.form['Qfrom'])
    destino = request.form['destino']
    fecha_now = date.today()
    date_time_now = datetime.now()
    fecha = fecha_now.strftime("%d-%m-%Y")
    hora = date_time_now.strftime("%H:%M:%S")

    endpoint = "https://rest.coinapi.io/v1/exchangerate/{}/{}?apikey=757C0581-641E-494C-8DCA-30C5274259BD"
    moneda_from = origen
    moneda_to = destino

    r = requests.get(endpoint.format(moneda_from, moneda_to))
    tasa = r.json()
    result = round(Qfrom * tasa['rate'], 10)

    return render_template('alta.html', origen=origen, Qfrom=Qfrom, destino=destino, result=result, hora=hora,
                           fecha=fecha)


@app.route('/calcular', methods=['GET'])
def calcular():
    form = MovimientosForm()
    if form.validate_on_submit():
        fecha = str(form.fecha.data)
        hora = str(form.hora.data)
        origen = request.form['origen']
        Qfrom = float(request.form['Qfrom'])
        destino = request.form['destino']
        Qto = request.form['Qto']

        return render_template("alta.html", formulario=form, fecha=fecha, hora=hora, origen=origen, Qfrom=Qfrom,
                               destino=destino, Qto=Qto)
    else:
        return render_template("calcular.html", formulario=form)


@app.route('/alta', methods=['GET', 'POST'])
def alta():
    form = MovimientosForm()
    if request.method == 'GET':
        return render_template('alta.html', form=form)
    else:
        if form.validate():
            fecha = str(form.fecha)
            hora = str(form.hora)
            origen = request.form['origen']
            Qfrom = float(request.form['Qfrom'])
            destino = request.form['destino']
            Qto = float(request.form['Qto'])

            data_manager = ProcesaDatos()
            data_manager.graba_datos((fecha, hora, origen, Qfrom, destino, Qto))

            return redirect(url_for("inicio"))
        else:
            return render_template("alta.html", form=form)


@app.route('/status')
def estado():
    con = sqlite3.connect("data/datos.db")
    cur = con.cursor()

    cur.execute("""
                SELECT 
                    SUM(Qfrom)
                FROM movements
                    WHERE origen="EUR";
                """
                )

    amount = cur.fetchall()

    amount0 = (lambda x: x)(*amount)
    amount1 = str(amount0)[1:-2]


    con = sqlite3.connect("data/datos.db")
    cur = con.cursor()

    cur.execute("""
                SELECT 
                    SUM(Qto)
                FROM movements
                    WHERE destino="BTC";
                """
                )

    amount = cur.fetchall()

    amounta = (lambda x: x)(*amount)
    amount2 = str(amounta)[1:-2]





    return render_template('status.html', amount=amount1, amount2=amount2)
