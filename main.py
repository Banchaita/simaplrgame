# # print("Sanchaita")
# x=4
# y=1
# z=x+y
# sum=z
# print("this is add",sum)

# x=4
# y=1
# z=x-y
# sub=z
# print("this sub",sub)

# x=4
# y=5
# z=x*y
# multipay=z
# print("this multipay",multipay)

# x=20
# y=5
# z=x/y
# div=z
# print("this div",multipay)

# x = input("Enter any number ");
# y = input("Enter any number ");
# z= int(x) + int(y)
# print("User enter number", z)


# def add_num(a,b):
#     sum=a+b;
#     return sum; 

# num1= int(input("Enter the number: ")) 
# num2=int(input("Enter the number: "))
# print("The sum is",add_num(num1,num2))

persent_year = 2023
age = int(input("Enter your birth year : "))
# if(age.isdigit()) == True:
voter_age= persent_year - age
if (voter_age > 18):
    print("You are eligible for vote")
else:
   print("You are not eligible for vote")