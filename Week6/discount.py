
def apply_discount(price, percentage):
    if percentage < 0 or percentage > 100:
        raise ValueError("Percentage must be between 0 and 100.")  
    return price * (1 - percentage / 100)