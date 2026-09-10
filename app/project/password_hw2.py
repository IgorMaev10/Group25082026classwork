special_symbols = "!@#$%^&*()_+-=[]{};':\"\\,.<>/?"

def is_password_reliable(password: str) -> bool:
    if len(password) < 8:
        return False
    if not any(symbol.isdigit() for symbol in password):
        return False
    if not any(symbol.isnumeric() for symbol in password):
        return False
    if not any(symbol in special_symbols for symbol in password):
        return False
    if any(symbol == " " for symbol in password):
        return False
    else:
        return True