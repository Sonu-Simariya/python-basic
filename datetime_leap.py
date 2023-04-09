import datetime as dt
import calendar as vc
# a=dt.date(2022,1,1)
# b=dt.date.today()
# c=b-a
# print(b)
# print(c.days)

# f_date = dt.date(2014, 7, 2)
# l_date = dt.date(2014, 7, 11)
# delta = l_date - f_date
# print(delta.days)


a=int(input("enter year: "))
if (a):
    print(vc.isleap(a))
else:
    print("not leapyear")