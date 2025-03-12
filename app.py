from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mi_secreto_seguro'  # Necesario para formularios con CSRF

# Definir la clase de formulario
class NombreForm(FlaskForm):
    nombre = StringField('Ingresa tu nombre', validators=[DataRequired(), Length(min=2, max=50)])
    submit = SubmitField('Enviar')

# Ruta principal (Página de inicio)
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para el formulario
@app.route('/formulario', methods=['GET', 'POST'])
def formulario():
    form = NombreForm()
    if form.validate_on_submit():
        session['nombre'] = form.nombre.data  # Guardar en sesión
        flash('Formulario enviado con éxito!', 'success')
        return redirect(url_for('resultado'))
    return render_template('formulario.html', form=form)

# Ruta para mostrar el resultado
@app.route('/resultado')
def resultado():
    nombre = session.get('nombre', None)  # Obtener de sesión

    if nombre is None:  # Evita errores si no se ha llenado el formulario
        flash('No hay datos en la sesión. Ingresa tu nombre en el formulario.', 'warning')
        return redirect(url_for('formulario'))

    return render_template('resultado.html', nombre=nombre)
@app.route('/about')
def about():
    return render_template('about.html')
# Ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True)
