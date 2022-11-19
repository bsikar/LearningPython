# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:   Evan Slyter
# Section:   565
# Assignment: 11.13 LAB: Weather Data
# Date: 11/11/22

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
    max_temp.append(weather[x][4])
    min_temp.append(weather[x][5])

# gets rid of the descriptors from the front of each list
date.pop(0)
wind_speed.pop(0)
rain.pop(0)
max_temp.pop(0)
min_temp.pop(0)

# turns all my data in the lists to floats
turn_float(wind_speed)
turn_float(rain)
turn_float(max_temp)
turn_float(min_temp)


# printing
print(f"3-year maximum temperature: {int(max(max_temp))} F")
print(f"3-year minimum temperature: {int(min(min_temp))} F")
print(f"3-year average precipitation: {(sum(rain))/1096:.3f} inches")

# inputs
month = input("Please enter a month: ")


year = input("Please enter a year: ")

print(f"For {month} {year}: ")

# converts month to lowercase and then to the number equivilent
month = month.lower()
month = months[month]

while pos < len(date):
    if year not in date[pos]:
        date.pop(pos)
        wind_speed.pop(pos)
        rain.pop(pos)
        max_temp.pop(pos)
        min_temp.pop(pos)
        pos = 0
        continue
    pos += 1

pos = 0

# removes all the dates not in the correct year and month
while pos < len(date):
    if int(month) >= 10:
        if str(month) + "/" not in date[pos][:3]:
            date.pop(pos)
            wind_speed.pop(pos)
            rain.pop(pos)
            max_temp.pop(pos)
            min_temp.pop(pos)
            pos = 0
            continue
    else:
        if str(month) + "/" not in date[pos][:2]:
            date.pop(pos)
            wind_speed.pop(pos)
            rain.pop(pos)
            max_temp.pop(pos)
            min_temp.pop(pos)
            pos = 0
            continue
    pos += 1
for each in rain:
    if each != 0:
        raincount += 1

# prints the final part
print(f"Mean maximum daily temperature: {sum(max_temp)/len(max_temp):.1f} F")
print(f"Mean daily wind speed: {sum(wind_speed)/len(wind_speed):.2f} mph")
print(f"Percentage of days with precipitation: {(raincount/len(rain))*100:.1f}%")

# closes file
weather_file.close()