from bcrypt import gensalt,checkpw,hashpw

def hashed_password(password:str)->bytes:
    return hashpw(password.encode("UTF-8"),gensalt(12))

def check_password(password:str,hash:bytes)->bool:
    return checkpw(password.encode("UTF-8"),hash)