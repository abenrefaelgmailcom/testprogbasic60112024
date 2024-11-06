# ###############תנאים

#1
#  קלוט שני מספרים עשרוניים והדפס את הקטן שלוש פעמים
num1: float= float(input(' enter number:'))
num2: float= float(input(' enter number:'))
if num1 > num2:
    print('num 1 is bigger')
else:
    print('num 2 is bigger')


#2
# קלוט שני מספרים שלמים והדפס את הממוצע שלהם
solid_num1: int = int(input('enter number:'))
solid_num2: int = int(input('enter number:'))
summery = solid_num1+solid_num2 % 2
print(summery)

#3
# קלוט 3 מספרים והדפס את הגדול מבין שלושתם
x: int = int(input('enter number:'))
y: int = int(input('enter number:'))
z: int = int(input('enter number:'))

if x > y:
    print(f' x is the bigger number, {x} ' )
elif y > z:
    print(f' y is the bigger number, {y} ' )
else:
    print(f' z is the bigger number, {z} ' )


#4
# קלוט אורך של סרט בדקות ןהדפס כמה דקות ושעות הוא לדוגמא אם נקלט 105 התשובה תהיה 1 שעה ו45 דקות
movie_length: float= float(input(' enter number:'))
hours = movie_length // 60
minuts = movie_length % 60

print(f"time by hours = {hours} time by minuts = {minuts}")


#5
#קלוט מספר, מובטח כי הוא בן 4 ספרות. מצא מהי הספרה הימנית ביותר והדפס אותה
number = int(input("Enter a 4-digit number: "))
rightmost_digit = number % 10
print("The rightmost digit is:", rightmost_digit)

#6
#6 קלוט מספר, מובטח כי הוא בן 4 ספרות מצא מהי הספרה השנייה מימין והדפס אותה
number = int(input("Enter a 4-digit number: "))
second_right_digit = (number // 10) % 10
print("The second rightmost digit is:", second_right_digit)


#7
#קלוט מספר דו ספרתי והדפס את סכום ספרותיו#
number = int(input("Enter a two-digit number: "))
digit_sum = (number // 10) + (number % 10)
print("Sum of digits:", digit_sum)



#8
#קלוט מספר דו ספרתי והפוך את ספרותיו. לדוגמא אם נקלט 61 התשובה תהיה 16.#
number = int(input("Enter a two-digit number: "))
backwards = (number % 10) * 10 + (number // 10)
print("Reversed number:", backwards)

#9
#קלוט מספר וכתוב even אם הוא זוגי ו- odd אם הוא אי זוגי
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("even")
else:
    print("odd")



#11
#קלוט גיל וגובה בס"מ של איש והצג האם מותר לאיש לעלות למתקן.
#מותר לעלות לרכבת ההרים מגיל 8 עד 18 אם גובהך מעל 115 ס"מ. אחרי גיל 18 מותר לעלות גם אם גובהך רק מעל 100 ס"מ.
age = int(input("Enter age: "))
height = int(input("Height in cm: "))
if (8 <= age <= 18 and height > 115) or (age > 18 and height > 100):
    print("Allowed it")
else:
    print("Drink more milk, no ride for you")





#############לולאות
#1
# קלוט מספר טבעי שלם חיובי TOP והצג את כל המספרים הטבעיים מ-1 ועד TOP כולל

top = int(input("enter number: "))
if top > 0:
    for i in range(1, top + 1, +1):
        print(i, end=" ")
        print()
else:
    print('number is not positive')


#2
# # קלט שני מספרים שלמים והצג את כל השלמים מבניהם כולל בסדר עולה, לא מובטח שהנתון השני גדול מהראשון
num1 = int(input("enter number: "))
num2 = int(input("enter number: "))
small = min(num1, num2)
big = max(num1, num2)

for i in range(small, big+1):
        print(i, end=" ")


#3
#קלוט מספר טבעי ח. הצג את כל המספרים הזוגיים מ- 0 עד n (כולל). לא מובטח ש-n זוגי.
n = int(input("Enter a positive integer (n): "))
for i in range(0, n + 1, 2):
    print(i)






4
#קלוט שני מספרים טבעיים max ו- den. הצג את כל המספרים הטבעיים עד max (כולל) המתחלקים ב- den.
#לא מובטח ש-max עצמו מתחלק ב- den.
max_num = int(input("Enter the maximum number: "))
den = int(input("Enter the divisor (den): "))
for i in range(den, max_num + 1, den):
    print(i)




# #############עיבוד נתונים
# 1. קלוט מספרים עד שייקלט 99- והצג את סכומם. אם מיד נקלט 99- יודפס None
# אתחול סכום המספרים

total = 0

while True:
    number = int(input('enter number: '))
    if number == -99 and total == 0:
        print('None')
        break
    elif number == -99:
        break
    total += number

if total != 0:
    print('Total sum of numbers entered:', total)



#2
# קלוט מספרים עד שקולטים מספר שלילי או ).
#הצג את הערך הגבוה ביותר והנמוך ביותר שקלטת
#אם מיד נקלט 99- יודפס None

high_val = None
low_val = None

while True:
    number = int(input("enter number : "))

    if number == -99 and high_val is None and low_val is None:
        print("None")
        break

    elif number == -99:
        break

    if high_val is None or number > high_val:
        high_val = number
    if low_val is None or number < low_val:
        low_val = number

if high_val is not None and low_val is not None:
    print("highest num entered:", high_val)
    print("lowest num entered:", low_val)






#3
# קלוט 5 מספרים.
#הצג את המספר הסידורי של הערך הגבוה ביותר. לדוגמא אם נקלט: 88, 99, 4, 5, 12- התשובה תהיה 4. כי 99 נקלט בקלט ה- רביעי
numbers = []

for i in range(5):
    number = int(input(f"Enter number {i + 1}: "))
    numbers.append(number)

highest_value_index = numbers.index(max(numbers)) + 1

print("The serial number of the highest value is:", highest_value_index)



#8
##c
number = int(input("Enter a number: "))

if number <= 1:
    print(f"{number} is not a prime number")
else:
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            print(f"{number} is not a prime number")
            break
    else:
        print(f"{number} is a prime number")




# #######לולאה מורכבת####
# #1
#

temperatures = []
last_was_zero = False

for i in range(12):
    try:
        temp = float(input(f" avg temperature for month {i + 1}: "))

        if temp == 0 and last_was_zero:
            print("Consecutive zero detected, input ignored. Please re-enter.")
            continue

        last_was_zero = (temp == 0)

        if temp < 5 or temp > 40:
            print("wrong data")
            break
        else:
            temperatures.append(temp)

    except ValueError:
        print("wrong data")
        break

if len(temperatures) == 12:
    average_temp = sum(temperatures) / len(temperatures)
    max_temp = max(temperatures)
    min_temp = min(temperatures)

print("correct data")
print(f"Average temperature: {average_temp:.2f}°C")
print(f"Highest temperature: {max_temp}°C")
print(f"Lowest temperature: {min_temp}°C")
