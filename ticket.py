def entrance_fee(ages) -> int:
    """
    Calculates entrance fee for the amusement park.
    Parameters :
          ages : List of Ages
    Returns:
        int: The total entrance fee.
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