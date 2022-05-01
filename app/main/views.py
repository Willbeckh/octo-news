from . import main

# first default route
@main.route('/')
def index():
    """
    Landing page route
    """
    return "Yoow Blueprints!"