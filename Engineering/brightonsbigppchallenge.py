# function that takes integer and string and returns true if valid date
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sept", "Oct", "Nov", "Dec"]
days_31 = ["Jan", "Mar", "May", "Jul", "Aug", "Oct", "Dec"]
days_30 = ["Apr", "Jun", "Sept", "Nov"]


def is_date(day: int, month: str) -> bool:
    month_true = False
    day_true = False
    if month in months:
        month_true = True
    else:
        return False
    if month in days_31 and 0 < day <= 31:
        return True
    if month in days_30 and 0 < day <= 30:
        return True
    if month == "Feb" and 0 < day <= 28:
        return True
    return False


assert is_date(1, "Jan") == True
assert is_date(0, "Jan") == False
