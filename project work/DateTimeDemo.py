import datetime
from xmlrpc.client import DateTime

data = datetime.datetime.now()
print("Current Date & Time :",data)

data1 = datetime.date.today()
print("Current Date",data1)
print("Year",data1.year)
print("Month",data1.month)
print("Day",data1.day)

data2 = datetime.date(2022,1,31)
print("Custom Date",data2)

data3 = datetime.datetime.now().timestamp()
print("Timestamp Type : ",type(data3))
print("Timestamp : ",data3)

data4 = datetime.date.fromtimestamp(data3)
print("From Date : ",data4)

data5 =datetime.time(2,51,50,123123)
print("Current Time",data5)
print("Hour",data5.hour);
print("Minute",data5.minute);
print("Second",data5.second);
print("MilliSecond",data5.microsecond);


date1 = datetime.timedelta(days=3,seconds=123123,microseconds=34555,minutes=10,hours=12,weeks=2)
print("Date 1 : ",date1)
date2 = datetime.timedelta(days=5,seconds=123456,microseconds=64355,minutes=50,hours=5,weeks=1)
print("Date 2 : ",date2)

print("Difference",date1-date2)

data6 = datetime.datetime.now()
print("Current Date Time : ",data6)

print("Date : ",data.strftime("%d-%m-%Y"))
print("Date : ",data.strftime("%d-%m-%y"))
print("Date : ",data.strftime("%d-%B-%y"))
print("Date : ",data.strftime("%d-%B-%Y"))
print("Date : ",data.strftime("%d-%B-%Y %H:%M:%S"))

data7 = "27 February 2022"
data8 = datetime.datetime.strptime(data7,'%d %B %Y')
print(data8)