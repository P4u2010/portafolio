# Importa las clases necesarias desde Flask
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

# Configura la aplicación Flask
app = Flask(__name__)

# Configura la base de datos SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/Pau/Desktop/portafolio/diary.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializa la extensión SQLAlchemy
db = SQLAlchemy(app)

# Define el modelo de datos para la tabla User
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    comment = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<User {self.email}>'

# Crea todas las tablas definidas en los modelos
with app.app_context():
    db.create_all()

# Ruta para la página principal
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para procesar el formulario de feedback
@app.route('/feedback', methods=['POST'])
def feedback():
    if request.method == 'POST':
        email = request.form['email']
        comment = request.form['text']
        
        # Crea un nuevo objeto User y guarda en la base de datos
        new_comment = User(email=email, comment=comment)
        db.session.add(new_comment)
        db.session.commit()

        # Redirige al usuario a la página principal después de procesar el formulario
        return redirect('/')

# Corre la aplicación Flask en modo debug
if __name__ == "__main__":
    app.run(debug=True)

