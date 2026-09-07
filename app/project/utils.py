def calculate_discount(price: float, discount: int) -> int:
    result = round(price / 100 * discount)
    return result

def is_even(number: int) -> bool:
    result = number % 2 == 0
    return result

def get_full_name(first_name: str, last_name: str) -> str:
    result =  f"{first_name.title().strip()} {last_name.title().strip()}"
    return result
