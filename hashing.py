import hashlib

def transform_arg(arg):
    if arg is None:
        return ""
    return str(arg)

def sha256(input):
    return hashlib.sha256(input).hexdigest()

def calculate(*args):
    return sha256(" ".join(map(transform_arg, args)))

