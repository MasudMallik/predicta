from bcrypt import hashpw,checkpw,gensalt

def hash_pw(password:str)->bytes:
    return hashpw(password.encode("UTF-8"),gensalt(12))

def check_password(new_password:str,old_password:bytes)->bool:
    return checkpw(new_password.encode("UTF-8"),old_password)