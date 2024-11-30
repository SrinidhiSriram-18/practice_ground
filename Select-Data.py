import pandas as pd

def select(students:pd.DataFrame)->pd.DataFrame:
    df = students.loc[students['student_id']==101]
    df.drop('student_id',axis=1,inplace=True)
    return df

# Test case
student_input={'student_id':[101,53,128,3],'name':["Ulysses","William","Henry","Henry"],'age':[13,10,6,11]}
# print(student_input)
student=pd.DataFrame(student_input)
print(select(student))
