import pytest
from requests import session
from sqlalchemy import and_, distinct ,func

from models.Database import User, Order

@pytest.mark.realdb
class Test_Constraint:
    @pytest.mark.testdb
    @pytest.mark.testconst
    def test_email_and_name_not_null(self,db_session):
        """Test to ensure that email and name field in User table is not null."""
        user = db_session.query(User).where(and_(User.email is not None, User.name is not None)).all()
        for u in user:
            assert u.email is not None and u.name is not None, "Email and Name should not be null"

    @pytest.mark.testdb
    @pytest.mark.testconst
    def test_unique_email_and_name(self, db_session):
        """Test to ensure that email and name field in User table is unique."""
        # users = db_session.query(User).all()
        total = db_session.query(User.email, User.name).count()
        unique = db_session.query(func.count(distinct(User.email)), func.count(distinct(User.name))).scalar()
        assert total == unique, "Email and Name should be unique"
        