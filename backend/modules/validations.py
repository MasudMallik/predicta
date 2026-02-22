from pydantic import BaseModel,validator,EmailStr,Field

def password_validate(password:str)->bool:
    check={
        "capital_letter":0,
        "small_letter":0,
        "digit":0,
        "special_character":0
    }
    for i in password:
        if i.isdigit():
            check["digit"]+=1
        elif i.isalpha():
            if i.islower():
                check["small_letter"]+=1
            else:
                check["capital_letter"]+=1
        else:
            check["special_character"]+=1
    if 0 in check.values():
        return False
    else:
        return True


class login(BaseModel):
    email:EmailStr
    password:str=Field(...,min_length=4)

    @validator("password")
    def check_pw(cls,password):
        if not password_validate(password):
            raise ValueError(
                "Password must contain at least one uppercase, one lowercase, one digit, and one special character."
            )
        else:
            return password
        
class register(BaseModel):
    name:str=Field(...)
    email:EmailStr
    contact:str=Field(...,max_length=12,min_length=10)
    password:str=Field(...)
    confirm_password:str=Field(...)

    @validator("password")
    def check_pw(cls,password):
        if not password_validate(password):
            raise ValueError(
                "Password must contain at least one uppercase, one lowercase, one digit, and one special character."
            )
        else:
            return password