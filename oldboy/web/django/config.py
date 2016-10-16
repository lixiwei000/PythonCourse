
def index():
    return 'index'

def login():
    return 'login'

def register():
    return 'register'


url = (
    ('index', index),
    ('/login', login),
    ('/register', register)
)
