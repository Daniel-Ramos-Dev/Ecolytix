import hashlib
import json

def generate_hash(data):

    payload = json.dumps(data).encode()

    return hashlib.sha256(payload).hexdigest()