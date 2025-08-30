import pytest
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

TEST_DB_URL = "sqlite:///:memory:"

@pytest.fixture(scope="function")
def db_session():
    """
    Provides a fresh database + session for each test function.
    Ensures no leftover mappings or tables leak across test modules.
    """
    # Import inside fixture so models are always fresh
    from models.Database import Base, User, Order

    # Create fresh engine + schema
    engine = sa.create_engine(TEST_DB_URL)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    # --- preload test data ---
    user1 = User(name="Victor Uriel", email="victor@example.com")
    user2 = User(name="Jane Doe", email="jane@example.com")
    session.add_all([user1, user2])
    session.flush()

    order1 = Order(user_id=user1.id)
    order2 = Order(user_id=user2.id)
    session.add_all([order1, order2])
    session.commit()

    yield session

    # --- teardown ---
    session.close()
    Base.metadata.drop_all(engine)
    engine.dispose()
