# Python Data Science Internship -- Month 1

## Detailed Theory & Concept Explanation

------------------------------------------------------------------------

# WEEK 1 -- Python Basics

## Topics Covered

-   Variables
-   Data Types
-   Operators
-   Input / Output
-   Conditional Statements
-   Loops

### Variables

Variables are containers used to store data values. Python automatically
detects the data type.

Example: name = "Himanshu" age = 21

### Data Types

-   int → 10
-   float → 10.5
-   str → "Hello"
-   bool → True/False
-   list → \[1,2,3\]
-   tuple → (1,2,3)
-   dict → {"key": value}
-   set → {1,2,3}

### Operators

Arithmetic: +, -, \*, /, %, \*\*\
Comparison: ==, !=, \>, \<, \>=, \<=\
Logical: and, or, not

### Conditional Statements

Used for decision making.

Example: if age \>= 18: print("Eligible") else: print("Not Eligible")

### Loops

For Loop: for i in range(5): print(i)

While Loop: count = 0 while count \< 5: print(count) count += 1

### Client Project Logic -- Average Temperature

1.  Take number of days as input
2.  Collect temperature values using loop
3.  Calculate total
4.  Compute average

------------------------------------------------------------------------

# WEEK 2 -- Data Structures & Functions

## Topics Covered

-   Lists
-   Tuples
-   Dictionaries
-   Sets
-   Functions
-   Lambda
-   Recursion
-   List Comprehension

### Lists

Ordered, mutable collection. numbers = \[1,2,3\]

### Tuples

Ordered, immutable collection. coordinates = (10,20)

### Dictionaries

Key-value storage. student = {"name":"Himanshu", "age":21}

### Sets

Unique values only. numbers = {1,2,3}

### Functions

Reusable code block.

def greet(name): return "Hello" + name

### Lambda Function

square = lambda x: x\*x

### Recursion

Function calling itself. def factorial(n): if n == 1: return 1 return n
\* factorial(n-1)

### Client Project -- Data Cleaning

Steps: - Remove None values - Remove duplicates - Sort data

------------------------------------------------------------------------

# WEEK 3 -- NumPy & Pandas

## NumPy

Used for numerical computation.

import numpy as np arr = np.array(\[1,2,3\])

Common operations: - np.mean() - np.sum() - np.std()

Broadcasting allows operations on entire array.

## Pandas

Used for data manipulation.

import pandas as pd df = pd.DataFrame(data)

Operations: - dropna() - drop_duplicates() - groupby() - mean()

### Client Project -- Dataset Cleaning

-   Remove missing values
-   Remove duplicates
-   Group by category
-   Calculate average

------------------------------------------------------------------------

# WEEK 4 -- Data Visualization

## Matplotlib

Used for basic graphs.

import matplotlib.pyplot as plt plt.bar(subjects, marks) plt.show()

## Seaborn

Advanced visualization library.

sns.pairplot(df) sns.heatmap(df.corr(), annot=True)

### Client Project -- Dashboard Creation

-   Bar Chart
-   Pairplot
-   Heatmap
-   Correlation analysis

------------------------------------------------------------------------

# Overall Learning Outcome

By completing Month 1 internship: - Learned Python fundamentals - Worked
with real datasets - Performed data cleaning - Used NumPy & Pandas -
Created visualizations - Built mini client projects

------------------------------------------------------------------------

Prepared by: Himanshu Kumar Upadhyay\
Program: B.Tech AIML\
Internship Month: 1
