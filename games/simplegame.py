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

if(anws_two == witten_ans.lower()) ==True:
  count+=1
  print("Correct Answer")
else:
  print("Worong Answer")

ques_three = "What is Sanchaita's favourite place?"
print("3rd ques: ",ques_three)
anws_three = "Hill Station"
witten_ans = input("Enter your answer: ")

if(anws_three == witten_ans.lower()) ==True:
  count+=1
  print("Correct Answer")
else:
  print("Worong Answer")

ques_four = "What is Sanchaita's favourite audio book story?"
print("4th ques: ",ques_four)
anws_four = "Kashi"
witten_ans = input("Enter your answer: ")

if(anws_four == witten_ans.lower()) ==True:
  count+=1
  print("Correct Answer : ")
else:
  print("Worong Answer")

ques_five = "Which type of song listen by Sanchaita"
print("5th ques: ",ques_five.lower())
anws_five = "All type of song"
witten_ans = input("Enter your answer: ")

if(anws_five == witten_ans) ==True:
  count+=1
  print("Correct Answer")
else:
  print("Worong Answer")

print("Your totel score: ", count)