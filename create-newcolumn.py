import pandas as pd

def createcolu(employees:pd.DataFrame)->pd.DataFrame:
    employees['bonus']=employees['salary']*2
    return(employees)


# Testcase - create a new bonus column which is twice salary column
employee_input={'name':['Piper','Grace','Georgia','Willow','Finn','Thomas'],'salary':[4548,28150,1103,6593,74576,24433]}
employees=pd.DataFrame(employee_input)
print(createcolu(employees))