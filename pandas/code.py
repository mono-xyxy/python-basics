import pandas as pd
import numpy as np

# employess table
employees = pd.DataFrame({
    "emp_id": [1, 2, 3, 4, 5, 6],
    "name": ["A", "B", "C", "D", "E", "F"],
    "dept": ["HR", "IT", "IT", "HR", "Sales", "Sales"],
    "salary": [50000, 60000, None, 52000, 45000, None]
})
# Orders table
orders = pd.DataFrame({
    "order_id": [101, 102, 103, 104, 105],
    "emp_id": [1, 2, 2, 5, 7],  # notice 7 doesn't exist in employees
    "amount": [200, 300, None, 150, 400],
    "product": ["A", "B", "A", "B", "C"]
})

employees["salary"]= employees["salary"].fillna(
    employees.groupby("dept")["salary"].transform("mean")
)

orders["amount"]=orders["amount"].fillna(0)

df = pd.merge(employees,orders,on="emp_id",how="left")

no_orders = df[df["order_id"].isna()]
emp_sales = df.groupby("emp_id")["amount"].sum().reset_index()

dept_salary=df.group_by("dept")["salary"].mean()

unique_products=df.groupby("dept")["product"].nunique()
df["dept_avg_salary"]=df.groupby("dept")["salary"].transform("mean")
df["above_avg"]=df["salary"]>df["dept_avg_salary"]

pivot = df.pivot_table(
    index="dept",
    columns="product",
    values="amount",
    aggfunc="sum",
    fill_value=0
)