def entrance_fee(ages: list) -> int:
    """
    Calculates the total entrance fee for an amusement park based on a list of ages.

    Args:
        ages (list): A list of integers representing each visitor's age.

    Returns:
        int: The sum of all entrance fees.
    """

    kid, adult, senior = 5000, 10000, 7000
    total_fee = 0

    for age in ages:
        if age>= 65:
            total_fee += senior
        elif age >= 19:
            total_fee += adult
        else:
            total_fee += kid

    return total_fee