months_days = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12,
}

days_months = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "Septemer",
    10: "October",
    11: "November",
    12: "December",
}
date1 = (input("User 1 please enter a birthday:  ")).split()
date2 = (input("User 2 please enter a birthday:  ")).split()
date3 = (input("User 3 please enter a birthday:  ")).split()
date4 = (input("User 4 please enter a birthday:  ")).split()
date5 = (input("User 5 please enter a birthday:  ")).split()


days = [date1[1], date2[1], date3[1], date4[1], date5[1]]

months = [date1[0], date2[0], date3[0], date4[0], date5[0]]

together = dict(zip(months, days))

print(together)

date1 = months_days[date1[0]]
date2 = months_days[date2[0]]
date3 = months_days[date3[0]]
date4 = months_days[date4[0]]
date5 = months_days[date5[0]]


dates = [date1, date2, date3, date4, date5]


dates.sort()

for x in range(len(dates)):
    print(f"{days_months[dates[x]]} {together[days_months[dates[x]]]}")
