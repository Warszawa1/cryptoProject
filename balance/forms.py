from datetime import date

from flask_wtf import FlaskForm
from wtforms import StringField, DateField, TimeField, SelectField, FloatField, SubmitField, HiddenField
from wtforms.validators import DataRequired, NumberRange, ValidationError
from datetime import date, datetime

# def today(formulario, field):
#     hoy = date.today()
#     if field.data > hoy or field.data < hoy:
#         raise ValidationError("La fecha tiene que ser hoy.")
fecha_now = date.today()
date_time_now = datetime.now()


class MovimientosForm(FlaskForm):
    fecha = fecha_now.strftime("%d-%m-%Y")
    # fecha = HiddenField()
    hora = date_time_now.strftime("%H:%M:%S")
    origen = SelectField("Origen:", choices=[('EUR', 'EUR'), ('BTC', 'BTC'), ('ETH', 'ETH'), ('BNB', 'BNB'), ('BCH', 'BCH'),
                                          ('LINK', 'LINK'), ('LUNA', 'LUNA'), ('ATOM', 'ATOM'), ('SOL', 'SOL'),
                                            ('USDT', 'USDT')],
                         validators=[DataRequired()])
    Qfrom = FloatField("Qfrom:", validators=[DataRequired(), NumberRange(message="Debe ser un número positivo",
                                                                    min=0.00000001)])
    destino = SelectField("Destino:", choices=[('EUR', 'EUR'), ('BTC', 'BTC'), ('ETH', 'ETH'), ('BNB', 'BNB'), ('BCH', 'BCH'),
                                            ('LINK', 'LINK'), ('LUNA', 'LUNA'), ('ATOM', 'ATOM'), ('SOL', 'SOL'),
                                            ('USDT', 'USDT')],
                          validators=[DataRequired()])
    Qto = FloatField("Qto:")

    aceptar = SubmitField("ACEPTAR")
    calcular = SubmitField("CALCULAR")
