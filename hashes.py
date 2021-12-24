import hashlib
import pickle
from typing import Any

def sha1_any(object:Any) -> str:
    #Ter cuidado com a ordem dos objetos dentro do dict
    encoded = pickle.dumps(object)
    sha1 = hashlib.sha1(encoded)
    return sha1.hexdigest()

