import re


def check_phone_number(number):
    mobile_regex = "^09([0-9]{2}|[0-9]{3})-?[0-9]{3}-?[0-9]{4}$"
    if number and re.fullmatch(mobile_regex, number):
        return True

    return False
