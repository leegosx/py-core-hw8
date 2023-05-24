from datetime import datetime, timedelta

users = [
        {'name': 'Alice', 'birthday': datetime(1990, 5, 13)},
        {'name': 'Bob', 'birthday': datetime(1995, 5, 10)},
        {'name': 'Sandy', 'birthday': datetime(1995, 5, 10)},
        {'name': 'Charlie', 'birthday': datetime(1985, 5, 8)},
        {'name': 'Abbey', 'birthday': datetime(1993, 9, 7)},
        {'name': 'Eddie', 'birthday': datetime(1994, 3, 22)}
]

def get_birthday_per_week(users):
    #Отримуємо сьогоднішню дату
    today = datetime.now().date()
    #Отримуємо дату початку неділі
    begin_week = today - timedelta(days=today.weekday())

    week_days = {
        "Monday": [],
        "Tuesday": [],
        "Wednesday": [],
        "Thursday": [],
        "Friday": [],
        "Saturday": [],
        "Sunday": []
}
    #Ітеруємося по іменниникам та додаємо їх до відповідних днів тижня
    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        #Знаходимо різницю між днем народження та понеділком на цьому тижні
        diff_date = (birthday - begin_week).days
        if diff_date >= 5:
            week_days['Monday'].append(name)
        else:
            # Додаємо пользв. до відповідного дня тижня
            weekday = (begin_week + timedelta(days=diff_date)).strftime('%A')
            week_days[weekday].append(name)
    for day, names in week_days.items():
        name_str = ", ".join(names)
        print(f"{day}: {name_str}")
    
print(get_birthday_per_week(users))





