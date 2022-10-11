from flask_wtf import FlaskForm
from wtforms.fields import *
from wtforms.validators import DataRequired, Length

class form_basico(FlaskForm):
    nombre = StringField(name='nombre',render_kw={"placeholder": "Ingresa tu nombre", 'onclick':'click()'},
    validators=[DataRequired(), Length(1,50)])
    correo = EmailField(name='correo',render_kw={"placeholder": "Ingresa tu correo electronico",'onclick':'click()'},
    validators=[DataRequired(), Length(1,50)])
    telefono = IntegerField(name='telefono', render_kw={"placeholder": "Ingresa tu numero telefonico" 
    ,'onclick':'click()'},
    validators=[DataRequired(), Length(1,10)])

    enviar = SubmitField('Enviar',render_kw={'onclick':'click()'})

class form_descargas(FlaskForm):
    nombre = StringField(name='nombre',render_kw={"placeholder": "Ingresa tu nombre" ,'onclick':'click()'},
    validators=[DataRequired(), Length(1,50)])
    correo = EmailField(name='correo',render_kw={"placeholder": "Ingresa tu correo electronico" ,'onclick':'click()'},
    validators=[DataRequired(), Length(1,50)])

    descargar = SubmitField('Descargar',render_kw={'onclick':'click()'})

class form_cita(FlaskForm):
    nombre = StringField(name='nombre',render_kw={"placeholder": "Ingresa tu nombre",'onclick':'click()'},
    validators=[DataRequired(), Length(1,50)])
    correo = EmailField(name='correo',render_kw={"placeholder": "Ingresa tu correo electronico",'onclick':'click()'},
    validators=[DataRequired(), Length(1,50)])
    telefono = IntegerField(name='telefono', render_kw={"placeholder": "Ingresa tu numero telefonico",'onclick':'click()'},
    validators=[DataRequired(), Length(1,10)])
    horario = SelectField('Horario de preferencia', choices=[('mañana', 'Por la mañana'), 
    ('tarde', 'Por la tarde')],render_kw={'onclick':'click()'})

    fecha = DateField(name='fecha', validators=[DataRequired()],render_kw={'onclick':'click()'})

    enviar = SubmitField('Descargar ahora',render_kw={'onclick':'click()'})

class form_reservacion(FlaskForm):
    nombre = StringField(name='nombre',render_kw={"placeholder": "Ingresa tu nombre",'onclick':'click()'},
    validators=[DataRequired(), Length(1,50)])
    correo = EmailField(name='correo',render_kw={"placeholder": "Ingresa tu correo electronico",'onclick':'click()'},
    validators=[DataRequired(), Length(1,50)])
    destino = StringField(name='destino',render_kw={"placeholder": "destino",'onclick':'click()'},
    validators=[DataRequired(), Length(1,50)])
    fecha_llegada = DateField(name='fechaLlegada', validators=[DataRequired()],render_kw={'onclick':'click()'})
    fecha_salida = DateField(name='fechaSalida', validators=[DataRequired()],render_kw={'onclick':'click()'})
    num_dias = DateField(name='numDias', validators=[DataRequired()],render_kw={'onclick':'click()'})
    num_ninios = IntegerField(name='numNinios', render_kw={"placeholder": "Ingresa tu numero telefonico",'onclick':'click()'},
    validators=[DataRequired(), Length(1,2)])
    num_adultos = IntegerField(name='numAdultos', render_kw={"placeholder": "Ingresa tu numero telefonico",'onclick':'click()'},
    validators=[DataRequired(), Length(1,2)])

    reservar = SubmitField('Reservar', render_kw={'onclick':'click()'})