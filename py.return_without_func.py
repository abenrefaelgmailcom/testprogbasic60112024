# a. כתוב פונקציה ascending_my המקבלת 2 פרמטרים מסוג int ומדפיסה את המספרים
# בסדר עולה. קרא לפונקציה שכתבת עם המספרים ,7 -12

def my_ascending(num1: int, num2: int) -> None:
    '''קבלת 2 פרמטרים מסוג int ומדפיסה את המספרים
בסדר עולה.'''
    if num1 < num2:
        print(num1, num2)
    else:
        print(num2, num1)

my_ascending(7, 12)

#b.  כתוב פונקציה details_my המקבלת מחרוזת str ומדפיסה את התו הראשון של
#המחרוזת, את התו האמצעי ואת התו האחרון. קרא לפונקציה שכתבת עם המחרוזת
# "AI is the best"


def my_details(notes: str) -> None:
    '''מקבלת מחרוזת ומדפיסה את התו הראשון, האמצעי והאחרון'''
    first_char = notes[0]
    middle_char = notes[len(notes) //2]
    last_char = notes[-1]
    print('first:', first_char, 'middle:', middle_char, 'last:', last_char)

my_details('ai is the best')


#כתוב פונקציה bool_say המקבלת בוליאני. c
#אם הבוליאני הוא True היא תדפיס  " yes "
#אחרת היא תדפיס "no".
# קרא לפונקציה שכתבת פעמיים: פעם אחת עם True ופעם
# נוספת עם False

def bool_say(value: bool) -> None:
    '''מקבלת ערך בוליאני ותדפיס YES אם TRUE ואם NO אז  FALSE '''
    if value:
        print('yes')
    else:
        print('no')
bool_say(True)
bool_say(False)

# d כתוב פונקציה zugi_print המקבלת כפרמטר רשימה של מספרים מסוג [int[list
# ומדפיסה עבור כל מספר ברשימה "even( "זוגי( או "odd( "אי-זוגי(.
# קרא לפונקציה
# שכתבת עם רשימת המספרים [14 14, 15, 10, 2, 3, 5,]
# odd, odd, even, even, odd, even, even :הצפוי הפלט

def print_zugi(numbers: list[int]) -> None:
    '''קבלת רשימת מספרים ומדפיסה עבור כל מספר אם הוא זוגי או אי זוגי'''
    for num in numbers:
        if num % 2 == 0:
            print('even', end=', ')
        else:
            print('odd', end=', ')

print_zugi([14, 15, 10, 2, 3, 5,])

# e כתוב פונקציה statistics_my המקבלת רשימה של ציונים ומדפיסה את הציון הכי גבוה,
#הציון הכי נמוך, כמות הציונים, ממוצע הציונים
# כעת כתוב קטע קוד הקולט ציונים מהמשתמש עד שנקלט הציון מינוס .99
# התעלם מציונים קטנים מ- 0 או גדולים מ- .100 כל ציון שנקלט הוסף לרשימה.
# אחרי הלולאה - קרא לפונקציית statistics_my ושלח לה את רשימת הציונים שיצרת

def statistics_my(grades: list[int]) -> None:
    '''מקבלת רשימת ציונים ומדפיסה את הציון הגבוה ביותר, הנמוך ביותר, כמות הציונים והממוצע'''

    if not grades:
        print('no valid grades entered.')
        return
    highest = max(grades)
    lowest = min(grades)
    count = len(grades)
    average = sum(grades) / count

    print("Highest:", highest)
    print("Lowest:", lowest)
    print("Lowest:", lowest)
    print("Average:", average)

grades = []

while True:
    grade = int(input('enter grade (enter -99 to stop):'))
    if grade == -99:
        break
    elif 0 <= grade <= 100:
        grades.append(grade)
statistics_my(grades)
