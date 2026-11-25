![Banner](https://capsule-render.vercel.app/api?type=waving&color=0:3776AB,100:FFD43B&height=200&section=header&text=Phase%201%20Python&fontSize=50&fontColor=ffffff)

<p align="center">
  <img src="https://skillicons.dev/icons?i=python,jupyter,git,github,vscode" alt="tools" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Jupyter-Notebook-F37626?logo=jupyter&logoColor=white" />
  <img src="https://img.shields.io/badge/Git-GitHub-181717?logo=github&logoColor=white" />
  <img src="https://img.shields.io/badge/Status-Learning-brightgreen" />
</p>

My practice and notes from Phase 1 of my learning path: Python beyond the basics. 🐍

## Topics covered

- Comprehensions and built-in helpers
- Functions: `*args`, `**kwargs`, lambda
- Object-oriented programming
- Exception handling
- File handling (text, CSV, JSON)
- Modules and packages
- Decorators and generators

## Notes with examples

### 1. Comprehensions
```python
squares = [x**2 for x in range(1, 6)]            # [1, 4, 9, 16, 25]
even = {x for x in range(10) if x % 2 == 0}      # set
lengths = {w: len(w) for w in ["apple", "kiwi"]} # dict
```

### 2. map, filter, zip, enumerate
```python
nums = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, nums))
odds = list(filter(lambda x: x % 2, nums))

for i, (n, d) in enumerate(zip(nums, doubled), start=1):
    print(i, n, d)
```

### 3. Flexible functions
```python
def summary(title, *scores, **info):
    print(title, sum(scores) / len(scores), info)

summary("Test", 80, 90, 85, student="Aarav", year=2)
```

### 4. Classes and inheritance
```python
class Student:
    def __init__(self, name, cgpa):
        self.name = name
        self.cgpa = cgpa

    def is_topper(self):
        return self.cgpa >= 9

class Intern(Student):
    def __init__(self, name, cgpa, company):
        super().__init__(name, cgpa)
        self.company = company

    def __str__(self):
        return f"{self.name} @ {self.company}"
```

### 5. Exception handling
```python
try:
    value = int("abc")
except ValueError as e:
    print("Invalid number:", e)
else:
    print("Converted:", value)
finally:
    print("Done")
```

### 6. File handling
```python
import json, csv

with open("data.json", "r") as f:
    data = json.load(f)

with open("students.csv", newline="") as f:
    rows = list(csv.DictReader(f))
```

### 7. Decorators
```python
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {time.time() - start:.4f}s")
        return result
    return wrapper

@timer
def slow_sum(n):
    return sum(range(n))
```

### 8. Generators
```python
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for i in countdown(3):
    print(i)   # 3, 2, 1
```

## What I practised
- Writing clean, reusable functions
- Modelling real things with classes
- Handling errors without crashing the program
- Reading and writing data files
- Processing data lazily with generators

## Next
Phase 2: NumPy, Pandas and data analysis. 🚀

![Footer](https://capsule-render.vercel.app/api?type=waving&color=0:FFD43B,100:3776AB&height=100&section=footer)
