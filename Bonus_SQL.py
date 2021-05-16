import pandas as pd
import sqlalchemy
import pprint
import psycopg2
import matplotlib.pyplot as plt
%matplotlib inline

from sqlalchemy import create_engine


# connect to local database
from sqlalchemy import create_engine
engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost:5433/Homework')
connection = engine.connect()

departments = pd.read_sql('select * from departments', connection)
departments


### Import the Employees table"
employees = pd.read_sql('select * from employees', connection, parse_dates=['birth_date', 'hire_date'])
employees.head()

### Import the Departments table"
departments = pd.read_sql('select * from departments', connection)
departments.head()


### Import the Salaries table
salaries = pd.read_sql('select * from salaries', connection, parse_dates=['from_date', 'to_date'])
salaries.head()



### Import the Department Manager table
dept_manager = pd.read_sql('select * from dept_manager', connection, parse_dates=['from_date', 'to_date'])
dept_manager.head()


###Replace null dates
dept_manager.to_date = dept_manager['to_date'].fillna(pd.to_datetime('2050-12-31'))
dept_manager.head()


### Import the Titles table
titles = pd.read_sql('select * from titles', connection, parse_dates=['from_date', 'to_date'])
titles.head()



#### Replace null dates
titles.to_date = titles['to_date'].fillna(pd.to_datetime('2050-12-31'))
titles.head()



#### Create a merged dataframe of titles and salaries
employee_salaries = titles.merge(salaries, on='emp_no')
employee_salaries.head()


### Creating Dataframe with emp_no, title, salary
employee_salaries_df = employee_salaries[['emp_no', 'title', 'salary']]
employee_salaries_df.head()

employee_salaries_df.groupby('title')['salary'].mean().round(2)
employee_salaries_df.head()

employee_salaries_df.hist(column='salary')

employees_grouped_by_title = employee_salaries_df.groupby(['title'])['salary'].mean()
employees_grouped_by_title


employees_grouped_by_title.plot.bar()
