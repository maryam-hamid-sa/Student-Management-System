# 🎓 College Student Management System

A simple Python-based console application that demonstrates the use of **custom modules**, **lists**, **tuples**, and **sets** to manage student records for a college.

---

## 📌 Project Overview

This project simulates a basic Student Management System where student information is stored and manipulated using Python's core data structures. The program is split into a **custom module** (`college.py`) that contains reusable functions, and a **main script** (`main.py`) that uses those functions to demonstrate various operations.

---

## ✨ Features

| Data Structure | Operations Demonstrated |
|---|---|
| **Custom Module** | Reusable functions imported and used in the main program |
| **List** | Create, display, add, remove, update, and count students |
| **Tuple** | Store student info (Roll No, Department, Semester), access via indexing, and demonstrate immutability |
| **Set** | Store club names, remove duplicates automatically, add/remove items, and membership checking |

---

## 📁 Project Structure
Student-Management-System/
│
│
├── college.py # Custom module with reusable function
│
├── main.py # Main program that uses the module and data structures
│
└── README.md # Project documentation
---

## 🧩 Module Functions — `college.py`

| Function | Description |
|---|---|
| `welcome()` | Displays a welcome message |
| `display_students(student_list)` | Displays all student names |
| `total_students(student_list)` | Returns the total number of students |

---

## 🚀 How to Run

1. **Clone the repository**
```bash
   git clone https://github.com/maryam-hamid-sa/Student-Management-System.git
```

2. **Navigate to the project folder**
```bash
   cd Student-Management-System
```

3. **Run the program**
```bash
   python main.py
```

> Requires **Python 3.x** — no external libraries needed.

---

## 📋 Task Breakdown

### ✅ Task 1 — Custom Module
Created `college.py` with three functions and imported it into `main.py` to display a welcome message, list all students, and count them.

### ✅ Task 2 — Lists
A list of at least five student names is created, with operations to display, add, remove, and update a student, followed by the updated total count.

### ✅ Task 3 — Tuples
A tuple stores a student's **Roll Number**, **Department**, and **Semester**. Values are accessed via indexing, and an attempt to modify a tuple element demonstrates Python's immutability error.

### ✅ Task 4 — Sets
A set of club names (with intentional duplicates) shows how sets automatically remove duplicates. Includes adding, removing, and checking membership with the `in` operator.

### ✅ Task 5 — Final Output
Combines all the above into a single, clean summary output: welcome message, student list, total count, student info, and club set.

---

## 🖥️ Sample Output
Welcome to the College Student Management System

student list: ['Muhammad Ali', 'Sara', 'Fatima', 'Hassan', 'Zainab']

Total number of students: 5

Student information

Roll Number : 230

Department : Computer Science

Semester : 5

Club set: {'Sports', 'Cricket', 'Music', 'Drama'}
---

## Tech Stack

- **Language:** Python 3
- **Concepts Used:** Modules, Lists, Tuples, Sets, Exception Handling

---

