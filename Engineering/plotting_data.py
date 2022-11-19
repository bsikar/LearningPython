# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:   Evan Slyter
# Section:   565
# Assignment: 12.17 LAB: Plotting Data
# Date: 11/18/22

import matplotlib.pyplot as plt

# function to turn everything in a list into a float
def turn_float(list):
    for each in range(len(list)):
        list[each] = float(list[each])


# dictionary for month numbers
months = {
    "january": 1,
    "february": 2,
    "march": 3,
    "april": 4,
    "may": 5,
    "june": 6,
    "july": 7,
    "august": 8,
    "september": 9,
    "october": 10,
    "november": 11,
    "december": 12,
}
# empty lists for all my data and other variables
date = []
wind_speed = []
rain = []
avg_temp = []
max_temp = []
min_temp = []
pos = 0
raincount = 0

# opens weather data file
weather_file = open("WeatherDataCLL.csv", "r")
weather = weather_file.read()
weather = weather.split("\n")


# splits all the data
for x in range(len(weather)):
    weather[x] = weather[x].split(",")

for x in range(len(weather)):
    date.append(weather[x][0])
    wind_speed.append(weather[x][1])
    rain.append(weather[x][2])
    avg_temp.append(weather[x][3])
    max_temp.append(weather[x][4])
    min_temp.append(weather[x][5])

# gets rid of the descriptors from the front of each list
avg_temp.pop(0)
date.pop(0)
wind_speed.pop(0)
rain.pop(0)
max_temp.pop(0)
min_temp.pop(0)

# turns all my data in the lists to floats
turn_float(avg_temp)
turn_float(wind_speed)
turn_float(rain)
turn_float(max_temp)
turn_float(min_temp)

avg_temp_2019 = avg_temp[0:366]
avg_temp_2020 = avg_temp[366:732]
avg_temp_2021 = avg_temp[732:]

max_temp_2019 = max_temp[0:366]
max_temp_2020 = max_temp[366:732]
max_temp_2021 = max_temp[732:]

min_temp_2019 = min_temp[0:366]
min_temp_2020 = min_temp[366:732]
min_temp_2021 = min_temp[732:]
# plotting stuff


days_length = []
for x in range(len(wind_speed)):
    days_length.append(x)


plt.figure()
ax = plt.subplot()
wind_plot = ax.plot(days_length, wind_speed, "r-")
ax.set_xlabel("date")
ax.set_ylabel("Average Wind Speed, mph")
ax2 = ax.twinx()
ax2.set_ylabel("Maximum Temperature, F")
max_temp_plot = ax2.plot(days_length, max_temp, "b-")
xaxis = ["2019", "2020", "2021"]
plt.title("Maximum Temperature and Average Wind Speed")
plt.xticks([183, 550, 916], xaxis)
plt.legend(["Avg Wind", "Max Temp"])


plt.show()

plt.figure()
plt.hist(wind_speed, bins=30)
plt.xlabel("Average Wind Speed, mph")
plt.ylabel("Number of days")
plt.title("Histogram of Average Wind Speed")
plt.show()


plt.figure()
plt.scatter(min_temp, wind_speed, s=10, c="black")
plt.title("Average Wind Speed vs Minimum Temperature")
plt.xlabel("Minimum Temperature, F")
plt.ylabel("Average Wind Speed, mph")
plt.show()

avg_temp_month = [
    (sum(avg_temp_2019[0:31]) / 31 + sum(avg_temp_2020[0:31]) / 31 + sum(avg_temp_2021[0:31]) / 31) / 3,
    (sum(avg_temp_2019[31:59]) / 28 + sum(avg_temp_2020[31:59]) / 28 + sum(avg_temp_2021[31:59]) / 28) / 3,
    (sum(avg_temp_2019[59:90]) / 31 + sum(avg_temp_2020[59:90]) / 31 + sum(avg_temp_2021[59:90]) / 31) / 3,
    (sum(avg_temp_2019[90:120]) / 30 + sum(avg_temp_2020[90:120]) / 30 + sum(avg_temp_2021[90:120]) / 30) / 3,
    (sum(avg_temp_2019[130:151]) / 31 + sum(avg_temp_2020[130:151]) / 31 + sum(avg_temp_2021[130:151]) / 31) / 3,
    (sum(avg_temp_2019[151:181]) / 30 + sum(avg_temp_2020[151:181]) / 30 + sum(avg_temp_2021[151:181]) / 30) / 3,
    (sum(avg_temp_2019[181:212]) / 31 + sum(avg_temp_2020[181:212]) / 31 + sum(avg_temp_2021[181:212]) / 31) / 3,
    (sum(avg_temp_2019[212:243]) / 31 + sum(avg_temp_2020[212:243]) / 31 + sum(avg_temp_2021[212:243]) / 31) / 3,
    (sum(avg_temp_2019[243:273]) / 30 + sum(avg_temp_2020[243:273]) / 30 + sum(avg_temp_2021[243:273]) / 30) / 3,
    (sum(avg_temp_2019[273:304]) / 31 + sum(avg_temp_2020[273:304]) / 31 + sum(avg_temp_2021[273:304]) / 31) / 3,
    (sum(avg_temp_2019[304:334]) / 30 + sum(avg_temp_2020[304:334]) / 30 + sum(avg_temp_2021[304:334]) / 30) / 3,
    (sum(avg_temp_2019[334:365]) / 31 + sum(avg_temp_2020[334:365]) / 31 + sum(avg_temp_2021[334:365]) / 31) / 3,
]

max_temp_month = [
    (max(max_temp_2019[0:31]) + max(max_temp_2020[0:31]) + max(max_temp_2021[0:31])) / 3,
    (max(max_temp_2019[31:59]) + max(max_temp_2020[31:59]) + max(max_temp_2021[31:59])) / 3,
    (max(max_temp_2019[59:90]) + max(max_temp_2020[59:90]) + max(max_temp_2021[59:90])) / 3,
    (max(max_temp_2019[90:120]) + max(max_temp_2020[90:120]) + max(max_temp_2021[90:120])) / 3,
    (max(max_temp_2019[130:151]) + max(max_temp_2020[130:151]) + max(max_temp_2021[130:151])) / 3,
    (max(max_temp_2019[151:181]) + max(max_temp_2020[151:181]) + max(max_temp_2021[151:181])) / 3,
    (max(max_temp_2019[181:212]) + max(max_temp_2020[181:212]) + max(max_temp_2021[181:212])) / 3,
    (max(max_temp_2019[212:243]) + max(max_temp_2020[212:243]) + max(max_temp_2021[212:243])) / 3,
    (max(max_temp_2019[243:273]) + max(max_temp_2020[243:273]) + max(max_temp_2021[243:273])) / 3,
    (max(max_temp_2019[273:304]) + max(max_temp_2020[273:304]) + max(max_temp_2021[273:304])) / 3,
    (max(max_temp_2019[304:334]) + max(max_temp_2020[304:334]) + max(max_temp_2021[304:334])) / 3,
    (max(max_temp_2019[334:365]) + max(max_temp_2020[334:365]) + max(max_temp_2021[334:365])) / 3,
]

min_temp_month = [
    (min(min_temp_2019[0:31]) + min(min_temp_2020[0:31]) + min(min_temp_2021[0:31])) / 3,
    (min(min_temp_2019[31:59]) + min(min_temp_2020[31:59]) + min(min_temp_2021[31:59])) / 3,
    (min(min_temp_2019[59:90]) + min(min_temp_2020[59:90]) + min(min_temp_2021[59:90])) / 3,
    (min(min_temp_2019[90:120]) + min(min_temp_2020[90:120]) + min(min_temp_2021[90:120])) / 3,
    (min(min_temp_2019[130:151]) + min(min_temp_2020[130:151]) + min(min_temp_2021[130:151])) / 3,
    (min(min_temp_2019[151:181]) + min(min_temp_2020[151:181]) + min(min_temp_2021[151:181])) / 3,
    (min(min_temp_2019[181:212]) + min(min_temp_2020[181:212]) + min(min_temp_2021[181:212])) / 3,
    (min(min_temp_2019[212:243]) + min(min_temp_2020[212:243]) + min(min_temp_2021[212:243])) / 3,
    (min(min_temp_2019[243:273]) + min(min_temp_2020[243:273]) + min(min_temp_2021[243:273])) / 3,
    (min(min_temp_2019[273:304]) + min(min_temp_2020[273:304]) + min(min_temp_2021[273:304])) / 3,
    (min(min_temp_2019[304:334]) + min(min_temp_2020[304:334]) + min(min_temp_2021[304:334])) / 3,
    (min(min_temp_2019[334:365]) + min(min_temp_2020[334:365]) + min(min_temp_2021[334:365])) / 3,
]


plt.figure()
plt.bar([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], avg_temp_month, color="orange")
max_plot = plt.plot([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], max_temp_month, color="red")
min_plot = plt.plot([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], min_temp_month, color="blue")

plt.title("Temperature by Month")
plt.xlabel("Month")
plt.ylabel("Average Temperature, F")
plt.legend(["High T", "Low T"])

plt.show()

# closes file
weather_file.close()
