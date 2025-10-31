import cpi

# Convert $1 from 1950 to 2025
year = 2000
MIN_YEAR = 1913
CURRENT_YEAR = 2017
try:
    value_today = cpi.inflate(1, year, CURRENT_YEAR)
except Exception as e:
    print(str(e))
    value_today = cpi.inflate(1, MIN_YEAR, CURRENT_YEAR)
print(value_today)
