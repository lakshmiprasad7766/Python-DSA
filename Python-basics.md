# This is the python basics file

-> print("hello"world")

 **complete Python basics guide** with **explanations + code examples** covering everything from **Stage 1: Fundamentals**

---

## **1. Python Setup**

* **Install Python** → [python.org](https://www.python.org/downloads/)
* **Install VS Code** or **PyCharm**
* **Check version:**

```bash
python --version
```

* **Run a Python file:**

```bash
python myfile.py
```

---

## **2. Variables & Data Types**

```python
# Variables
name = "Lakshmi"
age = 25
height = 5.8
is_student = True

print(name, age, height, is_student)
print(type(name))   # str
print(type(age))    # int
print(type(height)) # float
print(type(is_student)) # bool
```

# Data Types:

1. None -> The variable which is not assigned to any variable is called None.

2. Numeric -> Int(2), float(2.5), complex(6+9j), bool(true)

3.  a = 5.6
    b = int(a)
    type(b) = int


# List
L = [ 12, 33, 45,]

# set
s = {36, 12, 35, 36}
-> it won't allow duplicates

# Range

range(10)
-> list (range(10))
[0,1,2....9]

range(2,10,2) -> prints even numbers

# Dictonary

key should be unique, value may same/different

d = {'navin': 'Samsung', 'mlp': Iphone'}



---

## **3. Operators**

```python
# Arithmetic
x = 10
y = 3
print(x + y)   # 13
print(x - y)   # 7
print(x * y)   # 30
print(x / y)   # 3.333...
print(x // y)  # 3 (floor division)
print(x % y)   # 1
print(x ** y)  # 1000 (exponent)

# Comparison
print(x > y)  # True
print(x == y) # False

# Logical
a = True
b = False
print(a and b) # False
print(a or b)  # True
print(not a)   # False
```

---

## **4. Type Conversion**

```python
num_str = "10"
num_int = int(num_str)
print(num_int + 5)  # 15

num_float = float("3.14")
print(num_float)
```

---

## **5. Input/Output**

```python
name = input("Enter your name: ")
print("Hello", name)

age = int(input("Enter your age: "))
print("Next year, you will be", age + 1)
```

---

## **6. Control Flow**

```python
# if-elif-else
marks = 85
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
else:
    print("Grade C")

# Loops
for i in range(1, 6):
    print("For loop:", i)

count = 1
while count <= 5:
    print("While loop:", count)
    count += 1

# break, continue
for num in range(1, 6):
    if num == 3:
        continue  # skip 3
    if num == 5:
        break  # stop at 5
    print(num)
```

---

## **7. Data Structures**

```python
# List
fruits = ["apple", "banana", "cherry"]
fruits.append("mango")
print(fruits)
print(fruits[0])
fruits[1] = "orange"

# Tuple (immutable)
colors = ("red", "green", "blue")
print(colors[1])

# Set (unique elements)
nums = {1, 2, 3, 3}
print(nums)

# Dictionary
person = {"name": "Lakshmi", "age": 25}
print(person["name"])
person["city"] = "Hyderabad"
print(person)
```

---

## **8. Functions**

```python
def greet(name):
    return f"Hello, {name}"

print(greet("Lakshmi"))

# With default value
def add(a, b=5):
    return a + b

print(add(10))      # 15
print(add(10, 20))  # 30

# *args and **kwargs
def details(*args, **kwargs):
    print(args)      # tuple
    print(kwargs)    # dict

details(1, 2, 3, name="Lakshmi", age=25)
```

---

✅ This covers **Stage 1: Python Fundamentals** with **all basics + code**.
If you run through these examples and tweak values, you’ll master the foundations quickly.

---

