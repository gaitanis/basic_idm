import jwt
from flask_jwt_extended import create_access_token
import datetime

from config import *

def encode_auth_token(user_id):
    """
    Generates the Auth Token
    :return: string
    """
    try:
        return create_access_token(identity = user_id)
    except Exception as e:
        return e
