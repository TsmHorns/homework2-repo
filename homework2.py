#Ian Grant
#1641420

from calendar import month
import datetime

f = open("inputDates.txt")
output_file = open('parsedDates.txt','w')
my_file_data = f.readlines()


string_var = ','
string_var2 = ''
monthlist = {	"January": "1",
		"February": "2",
		"March": "3",
		"April":"4",
		"May": "5" ,
		"June": "6",
		"July": "7",
		"August": "8",
		"September": "9",
		"October": "10",
		"November": "11",
		"December": "12"		}

print("lets print this..")



array1 = []
parsed_count = 0
for x in range(len(my_file_data)):
  #print(my_file_data[x].find(string_var))
  array1.append(my_file_data[x].find(string_var))

parsed_arr = []
parsed_arr2 = []

for x in range(len(array1)):
  print("gets here inside of the loop" + str(x))
  #print(my_file_data[x].find(string_var))
  if(array1[x] != -1):
      print("gets here 1")
      parsed_arr.append(my_file_data[x])
      parsed_count = parsed_count + 1


for x in range(len(parsed_arr)):
  print("***************************")
  print("This is parsed_arr")
  print(parsed_arr[x])

#month + "/" + day + "/" + year
#3/1/1990
month_arr = []
day_arr = []
year_arr = []
final_arr = []
print("!!!!!!!!!!!!!!!!!!!!!!")
#split based off of white space

for x in range(len(parsed_arr)):
  print("***************************")
  print("This is parsed_arr")
  var = str(parsed_arr[x])
  var = var.split()
  print(var)
  month_arr.append(var[0])
  day_arr.append(var[1])
  year_arr.append(var[2])
 

for x in range(len(parsed_arr)):
  print("***************************")
  print(month_arr[x])
  print(day_arr[x])
  print(year_arr[x])
  print("***************************")

#now let us loop through the for loop,and see if the month arr
#is inside of the dictionairy
for x in range(len(month_arr)):
  try:
     print(monthlist[month_arr[x]])
     print("Let us see if this works 1")
     print(month_arr[x])
  except:
    month_arr.remove(month_arr[x])
    day_arr.remove(day_arr[x])
    year_arr.remove(year_arr[x])
    print("Tried to do this")
a = datetime.datetime.now();
for x in range(len(month_arr)):
  print("***************************")
  var = str(monthlist[month_arr[x]])
  res_str = str(day_arr[x]).replace(',','')
  print(res_str)
  final_arr.append(var + "/" + res_str + "/" + str(year_arr[x]))
  print(final_arr[x])
  print("***************************")

currentDay = datetime.datetime.now().day
currentMonth = datetime.datetime.now().month
currentYear = datetime.datetime.now().year
print(currentMonth)
print(currentDay)
print(currentYear)

for x in range(len(final_arr)):
  if int(year_arr[x]) > currentYear:
    print(year_arr[x])
    print(currentYear)
    final_arr.remove(final_arr[x])
    continue
    if int(year_arr[x]) > currentYear:
      if int(monthlist[month_arr[x]]) > currentMonth:
        final_arr.remove(final_arr[x])
        continue
    if int(year_arr[x]) > currentYear:
      if int(monthlist[month_arr[x]]) > currentMonth:
        if int(day_arr[x]) > currentDay:
          final_arr.remove(final_arr[x])
          continue
    

#okay so everything is working i just need to reroute this.
for x in range(len(final_arr)):
  print("***************************")
  final_string = str(final_arr[x]) + "\n" 
  output_file.write(final_string)

#ignore any dates that are later than the current date

#then you will need to work on the other labs
print("Gets to the bottom")
output_file.close()
f.close()
