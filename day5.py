import datetime

# datetime module is used to work with dates and times.
# The datetime module has many methods to return information about the date object.
# here are a few examples, you will learn more about them later in this chapter:
# its pre built in module in python so no need to install it.
# datetime.now()
# datetime.strptime()
# datetime.strftime()
# datetime.timedelta()
# datetime.date()
# datetime.time()

x = datetime.datetime.now()


print(x)
print(x.year)
print(x.month)
print(x.day)
# print(x.hour)

# strftime() method is used to format the date and time. It takes one argument, the format code.

print(x.strftime("%A")) # %A is used to print the day of the week in full.
print(x.strftime("%a")) # %a is used to print the day of the week in short.
print(x.strftime("%A %B"))
print(x.strftime("%B")) # %B is used to print the month in full.
print(x.strftime("%b")) # %b is used to print the month in short.
print(x.strftime("%C")) # %C is used to print the century.
print(x.strftime("%c")) # %c is used to print the date and time.
print(x.strftime("%D")) # %D is used to print the date in mm/dd/yy format.
print(x.strftime("%F")) # %F is used to print the date in yyyy-mm-dd format.
print(x.strftime("%G")) # %G is used to print the year in yyyy format.
print(x.strftime("%H")) # %H is used to print the hour in 24 hour format.
print(x.strftime("%I")) # %I is used to print the hour in 12 hour format.
print(x.strftime("%j")) # %j is used to print the day of the year.
print(x.strftime("%m")) # %m is used to print the month in mm format.
print(x.strftime("%M")) # %M is used to print the minute in mm format.
print(x.strftime("%p")) # %p is used to print the AM/PM.
print(x.strftime("%S")) # %S is used to print the second in ss format.
print(x.strftime("%U")) # %U is used to print the week number in mm format.
print(x.strftime("%W")) # %W is used to print the week number in ww format.
print(x.strftime("%x")) # %x is used to print the date in mm/dd/yy format.
print(x.strftime("%X")) # %X is used to print the time in HH:MM:SS format.
print(x.strftime("%y")) # %y is used to print the year in yy format.
print(x.strftime("%Y")) # %Y is used to print the year in yyyy format.
print(x.strftime("%Z")) # %Z is used to print the timezone.
print(x.strftime("%z")) # %z is used to print the timezone in +HHMM or -HHMM format.
print(x.strftime("%%")) # %% is used to print the % symbol.
print(x.strftime("%%")) # %% is used to print the % symbol.
print(x.strftime("%%")) # %% is used to print the % symbol.


print(x.strftime("%d/%m/%Y"))
print(x.strftime("%d-%m-%Y"))
print(x.strftime("%d-%m-%Y %H:%M:%S"))
print(x.strftime("%d-%m-%Y %H:%M:%S %p"))
print(x.strftime("%d-%m-%Y %H:%M:%S %p %A"))
print(x.strftime("%d-%m-%Y %H:%M:%S %p %A %B"))
print(x.strftime("%d-%m-%Y %H:%M:%S %p %A %B %Y"))
print(x.strftime("%d-%m-%Y %H:%M:%S %p %A %B %Y %H:%M:%S"))

y = datetime.datetime(2026, 4, 13)
print(y)



