# 📦 Database Testing with SQLAlchemy & Pytest

A lightweight Python project for **testing database schemas and CRUD operations** using **Pytest** and **SQLAlchemy ORM**.

This project is designed as a template for verifying:

* ✅ Database schemas (tables, columns, keys, constraints, relationships)
* ✅ CRUD operations (Create, Read, Update, Delete)
* ✅ Unique constraints and indexes
* ✅ Relationships between multiple tables (e.g., `User` ↔ `Order`)

---

## ⚙️ Requirements

* Python 3.12+
* [Pytest](https://docs.pytest.org/en/stable/)
* [SQLAlchemy](https://docs.sqlalchemy.org/en/20/)

Install dependencies:

```bash
pip install pytest sqlalchemy
```

---

## 📂 Project Structure

```
.
├── models/                     # Database models (SQLAlchemy ORM)
│   └── Database.py             # Defines User & Order models
│
├── tests/                      # All tests grouped by type
│   ├── schema/                 # Tests for schema (tables, columns, keys, relationships)
│   │   ├── test_user.py
│   │   └── test_order.py
│   │
│   ├── crud/                   # Tests for CRUD operations
│   │   └── test_crud_user.py
│   │
│   ├── constraints/            # Tests for unique, primary key, foreign key constraints
│   │   └── test_constraints.py
│   │
│   └── integrity/              # Tests for referential integrity (relationships, cascades)
│       └── test_integrity.py
│
├── conftest.py                 # Pytest fixtures (db_session, setup/teardown)
├── pytest.ini                  # Pytest config (markers, test paths)
├── requirements.txt            # Dependencies
└── README.md                   # Project documentation

```

---

## ▶️ Running Tests

Run **all tests** (default SQLite in-memory database):

```bash
pytest -m testdb
```

Run only **schema tests**:

```bash
pytest -m testschema
```

Run only **CRUD tests**:

```bash
pytest test_cases/test_crud/
```

---

## 🗄️ Example Models

```python
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True, index=True)
    email = Column(String, nullable=False, unique=True, index=True)
    age = Column(Integer, nullable=True, index=True)
    orders = relationship("Order", back_populates="user")

class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), index=True)
    user = relationship("User", back_populates="orders")
```

---

## ✅ Example Schema Test

```python
def test_user_table_exists(db_session):
    inspector = sa.inspect(db_session.bind)
    tables = inspector.get_table_names()
    assert "users" in tables
    assert "orders" in tables
```

---

## 🚀 Roadmap

* [x] Schema validation tests
* [x] CRUD operation tests
* [ ] Add performance tests (optional)
* [ ] Extend to PostgreSQL / MySQL

---

## 📜 License

This project is licensed under the **MIT License**.

---
