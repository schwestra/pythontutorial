# bill = float(input('What was the total bill? '))
# tip = int(input('What percentage tip would you like to give? 10, 12, or 15? '))
# people = int(input('How many people to split to bill? '))

# bahsis = tip / 100
# bahsis2 = bahsis * bill

# kisi = bill + bahsis2

# kisibasi = kisi / people

# final = round(kisibasi, 2)

# print(f"Each person should pay {final} ")

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# # 🚨 Don't change the code below 👇
# number = int(input("Which number do you want to check? "))
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇

# if number % 2:
#     print("This is an odd number.")
# else:
#     print("This is an even number.") 

#--------------------------------------------------------------------------------------------------

# luna = int(input("Giriş yapmak için boyunuzu giriniz: "))
# yas = int(input("Yaşınızı Giriniz: "))

# if luna >= 120:
#     print('Giriş yapabilirsiniz')
#     if yas <= 18:
#      print('Fiyat 7$'):
#     if yas > 18:
#      print('Fiyat 12$') 


    
# else:
#     print('Giriş yapamazsınız') 

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


bmi = weight / ( height ** 2)
bmi2 = round(bmi)

if bmi2 < 18.5:
    print(f"Your BMI is {bmi2}, you are underweight.")
elif bmi2 < 25:
    print(f"Your BMI is {bmi2}, you have a normal weight.")
elif bmi2 < 30:
    print(f"Your BMI is {bmi2}, you are slightly overweight.")
elif bmi2 < 35:
    print(f"Your BMI is {bmi2}, you are obese.")
else:
    print(f"Your BMI is {bmi2}, you are clinically obese.")



    
    
    
   

print('git çok zor')
print('git çok zor2222')