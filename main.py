import time
import pymysql

dayone = 1504454400
eachday = 86400
eachweek = eachday * 7
now = int(time.time())
now -= dayone
week = int(now / eachweek) + 1
day = int((now - (week - 1) * eachweek) / eachday) + 1
hour = int(now % eachday / 3600)
if hour > 16:
	day += 1
	day %= 7
hans = ['零', '一', '二', '三', '四', '五', '六', '日']

db = pymysql.connect("localhost", "root", "4e6d", "kb", charset='utf8')
cursor = db.cursor()
sql = "SELECT * FROM `table1` WHERE `day` = '%d'" % day
try:
	cursor.execute(sql)
	results = cursor.fetchall()
	if results == ():
		str = "周%s没课，嘻嘻\n" % hans[day]
	else:
		str = "周%s的课表如下：\n" % hans[day]
		for row in results:
			id = row[0]
			name = row[1]
			time = row[2]
			start_week = row[3]
			end_week = row[4]
			if week > end_week or week < start_week:
				continue
			teacher = row[5]
			clas = row[6]
			day = row[7]
			str += "第%s节是%s课，老师是%s，教室在%s\n" % (time, name, teacher, clas)
except:
	print("Error")
db.close()
print(str)
