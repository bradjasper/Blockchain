import hashlib

def calculate(* args):
    return hashlib.sha256(" ".join([str(arg) for arg in args if arg is not None])).hexdigest()

