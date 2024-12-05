from todor import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), unique = True, nullable = False)
    password = db.Column(db.Text, nullable = False)
    email = db.Column(db.String(254), unique=True, nullable=False)  # Nuevo campo email
    name = db.Column(db.String(80))
    lastname = db.Column(db.String(80))
    address = db.Column(db.String(80))
    gender = db.Column(db.String(10))  
    language = db.Column(db.String(50))  
    birthday = db.Column(db.Date)  

    def __init__(self, username, password, email, name, lastname, address, gender, language, birthday):
        self.username = username
        self.password = password
        self.email = email  # Asigna el correo electrónico
        self.name = name
        self.lastname = lastname
        self.address = address
        self.gender = gender
        self.language = language
        self.birthday = birthday

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