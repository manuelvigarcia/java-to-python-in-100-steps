week_days = {
    0: 'Sunday',
    1: 'Monday',
    2: 'Tuesday',
    3: 'Wednesday',
    4: 'Thursday',
    5: 'Friday',
    6: 'Saturday'
}

print(week_days.get(1,'invalid'))
print(week_days.get(6,'invalid'))
print(week_days.get(7,'invalid'))
