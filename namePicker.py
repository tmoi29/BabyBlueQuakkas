## Team BabyBlueQuokkas
## Queenie Xiang and Tiffany Moi
## SoftDev1 pd7
## HW02 -- NO-body expects the Spanish Inquisition!
## 2017-09-13 
import random

def namePicker(period): 
    CLASSES = {7: [ 'Helen', 'Shakil', 'Eric', 'Jennifer Y', 'Jennifer Z', 'Arif', 'Queenie', 'Jawadul', 'Shaina', 'Vivien', 'Brian', 'Naotaka', 'Bayan', 'Adam', 'Caleb', 'Terry', 'Jason', 'Alessandro', 'Samantha', 'Carol', 'Joyce', 'Shannon', 'Charles', 'Taylor', 'Kelly', 'Leo', 'Khyber', 'Ibnul', 'Eugene', 'Yuyang', 'Karina', 'Tiffany', 'Holden', 'Michael'], 8: ['Masha', 'Adrian', 'David', 'Eric', 'Josh', 'Jerome', 'Henry', 'Jackie', 'Giorgio', 'Karen', 'Sonal', 'Xavier', 'Bermet', 'Alex', 'Iris', 'Manahal', 'Donia', 'Md', 'Connie', 'Lisa', 'Xing', 'Angelica', 'Angel', 'Augie', 'Dimitriy', 'Yiduo', 'Gordon', 'Tiffany', 'Clive', 'Jonathan', 'Sasha', 'Daniel'], 9: [ 'Yu Qi', 'Michela', 'Kristin', 'Fabiha', 'Maxim', 'Marcus', 'Ish', 'James', 'Ryan', 'Edward', 'Adeeb', 'Jake', 'Cynthia', 'Kevin', 'Levi', 'Edmond', 'Kyle', 'Andrew', 'Max', 'Jenny', 'Philip', 'Shan', 'Mansour', 'Ray', 'Jake', 'Ida', 'Kerry', 'Stanley', 'Jackie', 'William', 'Tina', 'Michael']} 
    class_list = CLASSES[period]
    try:
        return class_list[random.randint(0, (len(class_list)-1))]
    except:
        return "Please enter in a valid period: 7, 8, or 9"


print namePicker(7)
  
