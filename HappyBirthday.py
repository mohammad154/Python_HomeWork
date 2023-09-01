from datetime import datetime
from jdatetime import datetime as jdatetime


def seconds_alive(birthdate, birthtime):
    """
    Calculate the number of seconds a person has been alive
    given their birthdate and birthtime.

    Args:
        birthdate (str): A string representing the birthdate in the format "YYYY-MM-DD".
        birthtime (str): A string representing the birthtime in the format "HH:MM:SS".

    Returns:
        int: The number of seconds the person has been alive.
    """
    birth_datetime = datetime.strptime(birthdate + ' ' + birthtime, '%Y-%m-%d %H:%M:%S')
    current_datetime = datetime.now()
    delta = current_datetime - birth_datetime
    return int(delta.total_seconds())


def days_minutes_to_next_birthday(birthdate, birthtime):
    """
    Calculate the number of days and minutes remaining to a person's next birthday
    given their birthdate and birthtime.

    Args:
        birthdate (str): A string representing the birthdate in the format "YYYY-MM-DD".
        birthtime (str): A string representing the birthtime in the format "HH:MM:SS".

    Returns:
        tuple: A tuple containing the number of days and minutes remaining to the next birthday.
    """
    birth_datetime = datetime.strptime(birthdate + ' ' + birthtime, '%Y-%m-%d %H:%M:%S')
    current_datetime = datetime.now()

    # Get the next birthday
    if current_datetime.month > birth_datetime.month or (
            current_datetime.month == birth_datetime.month and current_datetime.day >= birth_datetime.day):
        next_birthday_year = current_datetime.year + 1
    else:
        next_birthday_year = current_datetime.year

    next_birthday = datetime(next_birthday_year, birth_datetime.month, birth_datetime.day, birth_datetime.hour,
                             birth_datetime.minute, birth_datetime.second)

    # Calculate the time remaining to the next birthday
    delta = next_birthday - current_datetime
    days_remaining = delta.days
    minutes_remaining = int(delta.seconds / 60)

    return days_remaining, minutes_remaining


def ad_to_solar_date(ad_date, ad_time):
    """
    Convert an AD date to a solar date using the jdatetime package.

    Args:
        ad_date (str): A string representing the AD date in the format "YYYY-MM-DD".
        ad_time (str): A string representing the time in the format "HH:MM:SS".

    Returns:
        tuple: A tuple containing the solar date in the format (year, month, day) and the solar time in the format (hour, minute, second).
    """
    ad_datetime = datetime.strptime(ad_date + ' ' + ad_time, '%Y-%m-%d %H:%M:%S')
    solar_datetime = jdatetime.fromgregorian(datetime=ad_datetime)
    solar_date = (solar_datetime.year, solar_datetime.month, solar_datetime.day)
    solar_time = (solar_datetime.hour, solar_datetime.minute, solar_datetime.second)
    return solar_date, solar_time


print(seconds_alive('2023-05-09', '10:28:00'))
print(days_minutes_to_next_birthday('2023-05-09', '10:28:00'))
print(ad_to_solar_date('2023-05-09', '10:28:00'))
