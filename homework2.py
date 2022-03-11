
f = open("inputDates.txt")
output_file = open('parsedDates.txt','w')
my_file_data = f.readlines()
print(my_file_data)
print("testing right there 123")
#/ now i need a function to check the formatting

string_var = ','
string_var2 = ''
monthlist = {	'1': 'January',
		'2': 'February',
		'3': 'March',
		'4':'April',
		'5': 'May' ,
		'6': 'June',
		'7': 'July',
		'8': 'August',
		'9': 'September',
		'10': 'October',
		'11': 'November',
		'12': 'December'		}

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
      parsed_arr.append(array1[x])
      parsed_count = parsed_count + 1

for x in range(len(parsed_arr)):
  print("***************************")
  print(parsed_arr[x])

for x in range(len(parsed_arr2)):
  print("***************************")
  print(parsed_arr2[x])

#month + "/" + day + "/" + year
#3/1/1990
month_arr = []
day_arr = []
year_arr = []

print("!!!!!!!!!!!!!!!!!!!!!!")
#split based off of white space
for x in range(len(parsed_arr)):
   print(parsed_arr[x])

   
   var = str(parsed_arr[x])
   var = var.split()
   print("i dont think they understand")
   print(var[0])
   #parse month
   month_str = str(var[0])
   print(month_str)
   
   month_str = monthlist.get(var[0])
   print("Right before print")
   print("This is the month string " )
   varcheck = month_str
   month_arr.append(str(month_str))
   print("About to start parsing")


for x in range(len(month_arr)):
  print("***************************")
  print(month_arr[x])
  output_file.write(month_arr[x])

print("Gets to the bottom")
output_file.close()
f.close()