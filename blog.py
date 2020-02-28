import pymysql
import matplotlib.pyplot as plt

db = pymysql.connect('45.15.11.42', 'root', 'F/M`]d{Y?4_S', 'weather')
cursor = db.cursor()
sql = "select weather from w_city"
sql2 = "select time from w_city"
cursor.execute(sql)
data = cursor.fetchall()
cursor.execute(sql2)
date = cursor.fetchall()
db.close()
list_weather=[]
list_date=[]
for i in data:
    list_weather.append(i[0])

for s in date:
    list_date.append(str(s[0]))

plt.plot(list_date, list_weather)
plt.title('test')
plt.show()