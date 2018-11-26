import json
from passlib.hash import sha256_crypt

def check_passwords(password, password_hash):
    return sha256_crypt.verify(password, password_hash)

def generate_hash(password):
    return sha256_crypt.hash(password)

def get_config(filename):
    with open(filename, 'r') as file:
        return json.load(file)
