import bcrypt
def hash_password(password:str)->str:
    salt=bcrypt.gensalt()# creating pseudo random string
    # THE password must be encode to byte
    byte=password.encode("utf-8")
    hash=bcrypt.hashpw(byte,salt)
    return hash

def is_valid(hashed_password:bytes,password:str)->bool:
    return bcrypt.cheakpw(hash_password,password)
 