# sets blueprint
from flask import Blueprint


# create blueprint instance
main = Blueprint('main', __name__)


from . import views