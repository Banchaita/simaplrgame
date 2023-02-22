

birds="Nyctibiu Bluebirds Penguins Columbidae Budgeriga"
birds_guess = input("Guess a birds name:")
if(birds_guess.capitalize() in birds) == False: 
 print("No, not thaning of", birds_guess)
 print()
else:
  print("You guess it correct")

count = 0
print("How much know you Sanchaita")

name = input("Enter your name: ")
print("Welcome to ", name )


ques_one = "What is Sanchaita's heighest qualification"
print("1st ques: ",ques_one)
anws_one = "MCA"

witten_ans = input("Enter your answer: ")
if(anws_one.lower() == "MCA".lower()):
  count+=1
  print("Correct Answer : ")
else:
  print("Worong Answer : ")

ques_two = "What is Sanchaita's favourite food?"
print("2nd ques: ",ques_two)
anws_two = "Bengali food"
witten_ans = input("Enter your answer: ")

if(anws_two == witten_ans) ==True:
  count+=1
  print("Correct Answer")
else:
  print("Worong Answer")

ques_three = "What is Sanchaita's favourite place?"
print("3rd ques: ",ques_three)
anws_three = "Hill Station"
witten_ans = input("Enter your answer: ")

if(anws_three == witten_ans) ==True:
  count+=1
  print("Correct Answer")
else:
  print("Worong Answer")

ques_four = "What is Sanchaita's favourite audio book story?"
print("4th ques: ",ques_four)
anws_four = "Kashi"
witten_ans = input("Enter your answer")

if(anws_four == witten_ans) ==True:
  count+=1
  print("Correct Answer : ")
else:
  print("Worong Answer")

ques_five = "Which type of song listen by Sanchaita"
print("5th ques: ",ques_five)
anws_five = "All type of song"
witten_ans = input("Enter your answer: ")

if(anws_five == witten_ans) ==True:
  count+=1
  print("Correct Answer")
else:
  print("Worong Answer")

print("Your totel score: ", count)

ques = range(6)
for i in ques:
  if i==0:
    pass
  else:
    print(i, "Which type of song listen by Sanchaita")
    # print(i, "What is Sanchaita's favourite place?")

word = input("Type the word: ")
# waht_letter = input("Type a letter in the word:  ")

print(len(word))
print(word.count("o"))
print(word.find("for"))

menu = ["seafood", "pizza","suop","salad"]
item = input("enter item name: ")
count = 0

for i in menu:
  if (i in item):
    count=+1
if(count>0):
  print("item is found in the list", item)
else:
  print("item is not found")

name = input("What is your name? ")
age = int(input("What is your age? "))

if age > 18:
  print("The name you entered is", name+ " You are eligible for vote ")
elif age > 18 and age <= 30:
  print("The name you entered is" , name+ " You are eligible for vote ")
elif age > 30 and age <= 50:
  print("The name you entered is" , name+ " You are eligible for vote ")
elif age >= 50:
  print("The name you entered is" , name+ " You are eligible for vote ")
else:
  print("The name you entered is" , name+"You are not eligible for vote")

x=["python","javascript","c++"]
for i in x:
  print(x[1])

x = 0
while x < 10:
  print(x)
  x= x + 1
  # if(x==6):
  # break;

print("1 for Addition")
print("2 for Subsraction")
print("3 for Mutiplication")
print("4 for Division")
print("5 for Exit")

def add_num(n1,n2):
  sum= n1+n2
  return sum
  
def sub_num(n1,n2):
  sub= n1-n2
  return sub

def multi_num(n1,n2):
  multi= n1*n2
  return multi

def div_num(n1,n2):
  div= n1/n2
  return div


while(True):
  user = int(input("Enter a option 1-5 : "))
  if(user == 1): 
    print("Addition",add_num(5,5))
  if(user == 2):
    print("Subsraction",sub_num(10,5))
  if(user == 3):
    print("Mutiplication",multi_num(11,5))
  if(user == 4):
    print("Division",div_num(36,6))
  if(user == 5):
    print("Ended")
    break;

name_1 = input("Plases enter your name: ")
length = len(name_1) -1
index_num = int(input("Please enter a character number 0" + str(length) + ": "))

if index_num > length:
   print("Error invild input")
else:
  print(name[index_num])

# name = "Sanchaita"
# print(name[2:6])

name = "Sanchaita"
print(name[:4])
print(name[4:])
print(name[:])
print(name[::4])

string = input("Enter any word: ")
vowel = 'a','e','i','o','u'

for letter in string:
  if(letter in vowel):
     print("vowel in present is word: ",letter)
     break
  else:
    print("vowel in not present is word: ", letter)

my_str = input("Enter any word: ")
vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

for char in my_str:
  if char in vowels:
        print(char+ " is a vowel")
        break
  else:
        print(char+ " is a consonant")

example = input("Enter any word: ")

vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
count = 0
for character in example:
    if character in vowels:
        count += 1
if(count > 0):
  print("vowels is present")
else:
 print("vowels is not present")


print("Number of vowels in the given string is: ", count)

city_list = ["Tokyo", "Beijing", "New York", "Mexico City", "Moscow", "Los Angeles", "Paris","London"]
# print(type(city_list))
print("The 4th city on the list is : ", city_list[3])
add_possition = int(input("Enter the postion of the list: "))
new_city= input("Type new city name: ")
city_list.insert(add_possition,new_city)
print(city_list)