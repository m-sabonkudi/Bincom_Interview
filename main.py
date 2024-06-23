import random
from bs4 import BeautifulSoup
import statistics


# Read the HTML file, and prepare for scraping.
with open(file='site.html') as file:
    content = file.read()

# Parse the HTML for scraping
soup = BeautifulSoup(content, 'html.parser')

# We check any `td` tag inside a `tr` tag
scraped_data = soup.select(selector='tr td')

# In the HTML, there's a `tr` tag for each day, which has two `td` tags, one for the day and the other for its set of
# colors. So data variable above returns a list which contains of all days and their sets of colors

days_and_colors = {}


def list_of_days_and_dict():
    global scraped_data
    data = scraped_data
    """
    This function loops through the list data containing the days and their sets of colors. In the if block, since the 
    first element in data list is a day, the next is its set of colors, another day, then its colors, another day, its 
    colors....etc. The day var is changed in every loop and then in the else block, we make the day var a key with the 
    value of its set of colors (in the days_and_colors dict), and ultimately, the function returns a list containing only the days.
    :param data: 
    :return: list
    """
    days_ = []
    for i in range(len(data)):
        if i % 2 == 0:
            day = data[i].text
            days_.append(day)
        else:
            days_and_colors[day] = data[i].text.strip().upper()
    return days_, days_and_colors


days, dict_of_days_colors = list_of_days_and_dict()

overall_colors = []
# This will give us a list of all the colors in all days, stripped of any trailing or leading spaces, and in uppercase
for day in days:
    colors_for_day = dict_of_days_colors[day].split(',')
    for color in colors_for_day:
        overall_colors.append(color.strip().upper())


# 1. Mean
"""
A mean is calculated by diving the sum of given numbers by the total number of numbers e.g mean of [1, 2] is (1 + 3) / 2 = 2
So we can't calculate the mean of letters/words.
"""

# 2. Mode (Most Worn Color)
mode = statistics.mode(overall_colors)

# 3. Median color
median = statistics.median(overall_colors)  # we don't have to use the sort() because the statistics.median() auto-sorts

# 4. Variance
"""
Variance measures the spread of numerical data around the mean, calculated by averaging the squared differences from the
 mean. For example, the variance of [1, 2, 3] is calculated as [(1-2)^2 + (2-2)^2 + (3-2)^2] / 3 = 0.67. Since colors 
 are categorical data, variance cannot be calculated.
"""

# 5. Probability that a random color is red
""" We should calculate this by getting the total number of RED in the overall colors, and then divide it by the total
 number of the overall colors."""
no_red = overall_colors.count('RED')
probability_of_red = round(no_red / len(overall_colors), 2)  # rounded to 2 decimal places


# 6. PostgreSQL
import psycopg2
from psycopg2 import extras  # Import extras explicitly
# Connect to your PostgreSQL database
conn = psycopg2.connect(
    dbname="bincomdev",
    user="msabonkudii",
    password="Bincom",
    host="localhost",
    port="5432"
)

# Create a cursor object
cur = conn.cursor()

# Define the table schema
table_name = 'colors'
create_table_query = '''
CREATE TABLE IF NOT EXISTS {} (
    id SERIAL PRIMARY KEY,
    color VARCHAR(50) NOT NULL,
    frequency INTEGER NOT NULL
);
'''.format(table_name)

# Execute the create table query
cur.execute(create_table_query)
conn.commit()

# Data insertion query
insert_query = '''
INSERT INTO {} (color, frequency)
VALUES %s;
'''.format(table_name)
# Prepare data to be inserted
data = [(color.strip(), overall_colors.count(color)) for color in overall_colors]

# Execute the insertion query with the data
try:
    psycopg2.extras.execute_values(cur, insert_query, data)
    conn.commit()
    print("Data inserted successfully!")
except Exception as e:
    conn.rollback()
    print("Failed to insert data:", e)

# Close cursor and connection
cur.close()
conn.close()


# 7. Recursive searching (1-100)
def search(number, initial_index=0):
    numbers = [9, 2, 0, 5]
    if initial_index >= len(numbers):
        return f"{number} is not found in the list."

    if numbers[initial_index] == number:
        return f"{number} is found at index {initial_index} of list."
    else:
        return search(number=number, initial_index=initial_index + 1)


# 8. Conversion to base 10
def generate4d_binary() -> str:
    """
    Generates a 4-digit int and return it as str
    :return: str
    """
    binary = random.randint(0, 15)
    return format(binary, '04b')


number = generate4d_binary()
number_tobase_10 = int(number, 2)


# 9: Fibonacci
def fibonacci():
    list_fibonacci = [0, 1]
    for i in range(49):
        f = list_fibonacci[-2]
        s = list_fibonacci[-1]
        t = f + s
        list_fibonacci.append(t)

    return list_fibonacci[1:]
