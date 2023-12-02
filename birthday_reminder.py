from collections import defaultdict
from datetime import datetime

users_dict = [{"name": "Bill Gates", "birthday": datetime(1955, 10, 28)},
              {"name": "Tom Cruise", "birthday": datetime(1962, 7, 3)},
              {"name": "Robert John Downey Jr.", "birthday": datetime(1965, 12, 4)},
              {"name": "Tom Hanks", "birthday": datetime(1965, 12, 3)}]


def get_birthdays_per_week(users: list):
    """
    Gets the list of users and print to the console a list of people
    who need to be greeted by days in the next week.
    :param users:
    :return None:
    """
    today_date = datetime.today().date()
    birthdays_this_week = defaultdict(list)
    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today_date.year)
        if birthday_this_year < today_date:
            birthday_this_year = birthday.replace(year=today_date.year + 1)
        delta_days = (birthday_this_year - today_date).days
        if delta_days < 7:
            if birthday_this_year.weekday() in [5, 6]:
                birthdays_this_week['Monday'].append(f'{birthday_this_year.strftime("%d/%m")}-->{name}')
            else:
                birthdays_this_week[birthday_this_year.strftime("%A")].append(
                    f'{birthday_this_year.strftime("%d/%m")}-->{name}')
    for k, v in birthdays_this_week.items():
        print(k, v)


get_birthdays_per_week(users_dict)

