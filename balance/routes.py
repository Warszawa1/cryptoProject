import sqlite3
from balance import app
from flask import render_template, flash, request, redirect, url_for
from balance.models import ProcesaDatos
import sqlite3
from balance.forms import MovimientosForm

@app.route('/')
def inicio():
    data_manager = ProcesaDatos()
    try:
        datos = data_manager.recupera_datos()
        return render_template('movimientos.html', movimientos=datos)
    except sqlite3.Error as e:
        flash("Se ha producido un error en la base de datos. Inténtelo más tarde.")
        return render_template('movimientos.html', movimientos=[])



@app.route('/alta', methods=['GET', 'POST'])
def alta():
    form = MovimientosForm()
    if request.method == 'GET':
        return render_template('alta.html', formulario=form)
    else:
        if form.validate():
            fecha = str(form.fecha)
            hora = str(form.hora)
            origen = form.origen.data
            Qfrom = float(form.Qfrom.data)
            destino = form.destino.data
            Qto = float(form.Qto.data)

            data_manager = ProcesaDatos()
            data_manager.graba_datos((fecha, hora, origen, Qfrom, destino, Qto))

            return redirect(url_for("inicio"))
        else:
            return render_template("alta.html", formulario=form)

# def calcular():
#         form = MovimientosForm()
#         origen = 1
#         destino = 1.2
#         Qfrom = float(form.Qfrom.data)
#
#         resultado = origen * destino * Qfrom
#
#
#
#         return render_template(
#             'status.html',
#             formulario=form,
#             resultado=resultado
#         )


@app.route('/status')
def estado():
    return render_template('status.html')

@app.route('/calcular', methods=['GET'])
def calcular():
    form = MovimientosForm()

    if form.validate_on_submit():

        fecha = form.fecha.data
        hora = form.hora.data
        origen = form.origen.data
        Qfrom = form.Qfrom.data
        destino = form.destino.data
        Qto = form.Qto.data

        data_manager = ProcesaDatos()
        data_manager.graba_datos((fecha, hora, origen, Qfrom, destino, Qto))

        return render_template("calcular.html", formulario=form)
    else:
        return render_template("calcular.html", formulario=form)