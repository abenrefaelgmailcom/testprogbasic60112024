#כתוב פונקציה avg_my המקבלת 2 פרמטרים מסוג int ומחזירה float של הממוצע
#שלהם. קרא לפונקציה שכתבת עם המספרים ,99 90 ואחסן את התוצאה בתא זיכרון
#בשם- 1avg. לאחר מכן הדפס את 1avg

def my_avg(x: int, y: int) -> float:
    '''חישוב ממוצע של שני מספרים שלמים ומחזירה את הממוצע כ FLOAT'''

    '''חישוב הממוצע'''
    avg_result: float = (x + y) / 2
    return avg_result

avg1: float = my_avg(90, 99)

print(avg1)


#b. כתוב פונקציה headline_my המקבלת פרמטר מסוג str ומחזירה str של אותה
#המחרוזת באותיות גדולות בתוספת סימן קריאה בסוף המשפט. קרא לפונקציה שכתבת
#עם הכותרת "world the concurred has python "ואחסן את התוצאה בתא זיכרון
#בשם- 1head. לאחר מכן הדפס את 1head פעמיים

def my_headline(title: str) -> str:
    '''הפונקציה מקבלת פרמטר מסוג STR, מחזירה אותה באותיות גדולות בתוספת סימן קריאה בסוף'''
    headline: str = title.upper() + "!"
    return headline

head1: str = my_headline("world the concurred has python")

'''הדפסת התוצאה פעמיים'''
print(head1)
print(head1)




#c. כתוב פונקציה list_concat המקבלת 3 פרמטרים מסוג [int[list ומחזירה ]int[list של
#רשימה המכילה את 3 הרשימות מאוחדות לרשימה אחת ארוכה. קרא לפונקציה
#שכתבת עם הרשימות [9 8, 7,] [6 5, 4, 3,] [2 1,] ואחסן את התוצאה ברשימת
#con_res. כעת הדפס את הרשימה שחזרה ואת האורך שלה
#פלט צפוי: [9 8, 7, 6, 5, 4, 3, 2, 1,] אורך9-


def concat_list(list1: list[int], list2: list[int], list3: list[int]) -> list[int]:
    '''הפונקציה מקבלת 3 רשימות מסוג INT, ומחזירה רשימה אחת שהיא איחוד של שלוש הרשימות'''
    combined_list: list[int] = list1 + list2 + list3
    return combined_list

con_res: list[int] = concat_list([9, 8, 7], [6, 5, 4, 3], [2, 1])

print(con_res)

print(len(con_res))
