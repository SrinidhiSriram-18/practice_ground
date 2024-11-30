import pandas as pd

def dropduplicates(customers: pd.DataFrame)-> pd.DataFrame:
    customers.drop_duplicates('email',inplace=True)
    return(customers)

# Testcase - expected to drop duplicates in email column keeping the first record
customers_input = {'customer_id':[1,2,3,4,5,6],'name':['Ella','David','Zachary','Alice','Finn','Violet'],'email':['emily@example.com','michael@example.com','sarah@example.com','john@example.com','john@example.com','alice@example.com']}
customers = pd.DataFrame(customers_input)
print(dropduplicates(customers))