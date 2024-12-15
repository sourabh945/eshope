from string import ascii_letters, digits

valid_chars = ascii_letters + '. '

def validate_name(username:str) -> bool:
    for i in username:
        if i not in valid_chars:
            return False
    return True


def validate_phone_no(phone:str) -> bool:
    if len(phone) != 10:
        return False
    for i in phone:
        if i not in digits:
            return False
    return True


def validate_pincode(pincode:str) -> bool:
    for i in pincode:
        if i not in digits:
            return False
    return True
