import pandas as pd
import datetime as dt
import random

months = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
days = [i for i in range(1, 32)]
years = ["2022", "2023"]

# month string and range of valid temperatures
valid_temps = {
    "01": (-10, 15),
    "02": (-5, 20),
    "03": (-5, 20),
    "04": (0, 25),
    "05": (5, 28),
    "06": (10, 35),
    "07": (10, 40),
    "08": (10, 40),
    "09": (5, 30),
    "10": (0, 25),
    "11": (-5, 20),
    "12": (-10, 15)
}

cities = ["Barcelona", "Vienna", "Paris", "Ljubljana", "Rome"]

# date validator
def validate_date(year, month, day):
    # use datetime package to validate date
    try:
        dt.datetime(int(year), int(month), int(day))
        return True
    except ValueError:
        return False


assert validate_date(2022, "02", 30) == False # expect false
assert validate_date(2022, "02", 28) == True # expect true

# generate random date and temperature for a given city
# make sure not to generate the same date and city combo twice
def generate_data():
    data = []
    date_city = set()
    for i in range(1000):
        year = random.choice(years)
        month = random.choice(months)
        day = random.choice(days)
        city = random.choice(cities)
        temp_range = valid_temps[month]
        temp = random.randint(temp_range[0], temp_range[1])
        if validate_date(year, month, day) and (year, month, day, city) not in date_city:
            date_city.add((year, month, day, city))
            # create string representation for date
            hour = random.randint(9, 15)
            minute = random.randint(0, 59)
            date_string = f"{year}-{month}-{day} {hour}:{minute}:00"
            data.append([date_string, city, temp])

    return data

generated_data = generate_data()

df = pd.DataFrame(generated_data, columns=["date", "city", "temperature"])

df.to_csv("generated_data.csv", index=False)