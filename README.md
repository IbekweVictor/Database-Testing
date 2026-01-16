# 🧪 Database Testing Framework with SQLAlchemy & Pytest

## 📌 Project Summary

This repository contains a **Python testing framework** for validating database schemas and CRUD (Create, Read, Update, Delete) operations using the **SQLAlchemy ORM** and **Pytest**.

It ensures database integrity, verifies schema correctness, and tests data operations in a repeatable and automated way. This project can be used as a **template for database testing** in various applications or services.

---

## 🧰 Technologies & Concepts

* **Python** — programming language for test automation
* **SQLAlchemy ORM** — object-relational mapper for defining database models
* **Pytest** — testing framework for writing and running tests
* **SQLite (in-memory)** — default database for isolated test runs

---

## 📂 Project Structure

```
Database-Testing/
├── models/
│   └── Database.py               # SQLAlchemy ORM models (User, Order)
├── tests/
│   ├── schema/
│   │   ├── test_user.py          # Schema tests for users table
│   │   └── test_order.py         # Schema tests for orders table
│   ├── crud/
│   │   └── test_crud_user.py     # CRUD tests for User model
│   ├── constraints/
│   │   └── test_constraints.py   # Unique and constraint validation tests
│   └── integrity/
│       └── test_integrity.py     # Referential integrity & relationships
├── conftest.py                   # Pytest fixtures (DB setup/teardown)
├── pytest.ini                    # Pytest configuration
├── requirements.txt              # Python dependencies
└── README.md                     # Project documentation
```

---

## ▶️ Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/IbekweVictor/Database-Testing.git
cd Database-Testing
```

### 2️⃣ Set Up a Python Environment

```bash
python -m venv venv
source venv/bin/activate        # For Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run All Tests

```bash
pytest
```

### 5️⃣ Run Specific Test Groups

Schema tests:

```bash
pytest tests/schema
```

CRUD tests:

```bash
pytest tests/crud
```

---

## 🧠 What This Tests

### 🔹 Schema Validation

Verifies that database tables, columns, and relationships are defined correctly.

### 🔹 CRUD Operations

Tests Create, Read, Update, and Delete operations through ORM models.

### 🔹 Constraints & Unique Rules

Ensures that unique keys, indexes, and other constraints behave as expected.

### 🔹 Referential Integrity

Validates relationships between models (such as foreign key cascades).

---

## 📈 Example Model Definitions

```python
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    orders = relationship("Order", back_populates="user")

class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="orders")
```

---

## 🎯 Why This Project Matters

* **Ensures database correctness** before releases
* **Automates database testing** with a scalable framework
* **Supports CI/CD integration** for database checks
* Provides a **reference template for ORM-based database testing**

---

## 📈 Future Enhancements

* Add support for **PostgreSQL, MySQL, or other RDBMS**
* Include **data migration tests**
* Add **performance benchmarks**
* Provide **CI/CD pipeline examples**

Do you want me to do that next?
