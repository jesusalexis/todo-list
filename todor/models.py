from todor import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), unique = True, nullable = False)
    password = db.Column(db.Text, nullable = False)
    email = db.Column(db.String(120), unique=True, nullable=False)  # Nuevo campo email
    name = db.Column(db.Text)
    lastname = db.Column(db.Text)
    address = db.Column(db.Text)

    def __init__(self, username, password, email, name, lastname, address):
        self.username = username
        self.password = password
        self.email = email  # Asigna el correo electrónico
        self.name = name
        self.lastname = lastname
        self.address = address

    def __repr__(self):
        return f'<User: {self.username} >'
    
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    created_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    title = db.Column(db.String(100), nullable = False)
    desc = db.Column(db.Text)
    state = db.Column(db.Boolean, default = False)

    def __init__(self, created_by, title, desc, state = False):
        self.created_by = created_by
        self.title = title
        self.desc = desc
        self.state = state
    
    def __repr__(self):
        return f'<Todo: {self.title} >'