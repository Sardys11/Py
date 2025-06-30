
# Module 6
# Student: Sardys Avile-Martinez

# Step 1
print("\n===== Step 1=====")

# Simulated input (instead of sys.stdin)
from itertools import islice

sample_data = [
    "2025-06-29\t19:00\tPublix\tMilk\t3.29\tCash",
    "2025-06-29\t19:01\tWalmart\tEggs\t2.89\tCredit",
    "2025-06-29\t19:02\tTarget\tBread\t1.99\tDebit"
]

for line in islice(sample_data, 2):  # only process first 2 lines
    data = line.strip().split("\t")
    if len(data) == 6:
        date, time_val, store, item, cost, payment = data
        print(f"{item}\t{cost}")

from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

# Step 2 — Perform all 3 operations on datetime.now()
print("\n===== Step 2=====")
now = datetime.now()
print("Current time:", now)

# 1. Add 1 day
print("Time + 1 day:", now + timedelta(days=1))

# 2. Subtract 60 seconds
print("Time - 60 seconds:", now - timedelta(seconds=60))

# 3. Add 2 years
print("Time + 2 years:", now + relativedelta(years=2))


# Step 3 — Create timedelta for 100 days, 10 hours, and 13 minutes
print("\n===== Step 3=====")

# Total time in seconds: 100 days + 10 hours + 13 minutes
total_seconds = (
    100 * 24 * 60 * 60 +     # days to seconds
    10 * 60 * 60 +           # hours to seconds
    13 * 60                 # minutes to seconds
)
### Total = 8,676,780 seconds
d = timedelta(seconds=total_seconds)
print("As tuple:", (d.days, d.seconds, d.microseconds))
print("Timedelta object:", d)

# Another way of doing the same much simpler:
print("\n===== Step 3.1=====")
# less confusing ☺️
d = timedelta(days=100, hours=10, minutes=13)
print("Tuple:", (d.days, d.seconds, d.microseconds))
print("Timedelta object:", d)

# Step 4
print("\n===== Step 4=====")

def log_height(feet, inches):
    datetime_object = datetime.now()
    print(f"Current Time: {datetime_object}")
    print(f"Height: {feet} feet, {inches} inches")
    print('Type: - ', type(datetime_object))

# Example calls
log_height(5, 9)
log_height(6, 2)
