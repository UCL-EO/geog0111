# Formative Assessment: Groups : Answers to exercises

#### Exercise 1

* create a list called `months` with the names of the months of the year
* create a list called `ndays` with the number of days in each month (for this year)
* confirm that the two lists have the same length (12)
* Use these two lists to make a dictionary called `days_in_month` with the key as month name and value as the number of days in that month.
* print out the dictionary and confirm it is as expected
* set a variable `m` to be the name of a month
* using `m` and your dictionary, print out the number of days in month `m`


```python
# ANSWER
# create a list called `months` with the names of the months of the year
months = ["January","February","March","April","May",\
         "June","July","August","September","October",\
         "November","December"]
# create a list called `ndays` with the number of days in each month (for this year)
ndays = [31,29,31,30,31,30,31,31,30,31,30,31]

# confirm that the two lists have the same length (12)
print(f'length of months: {len(months)}')
print(f'length of ndays:  {len(ndays)}')

# Use these two lists to make a dictionary called `days_in_month` 
# with the key as month name and value as the number of days in that month.
days_in_month = dict(zip(months,ndays))

# print out the dictionary and confirm it is as expected
print(days_in_month)

# set a variable `m` to be the name of a month
m = 'January'
print(f'The number of days in {m} is {days_in_month[m]}')
```

    length of months: 12
    length of ndays:  12
    {'January': 31, 'February': 29, 'March': 31, 'April': 30, 'May': 31, 'June': 30, 'July': 31, 'August': 31, 'September': 30, 'October': 31, 'November': 30, 'December': 31}
    The number of days in January is 31

