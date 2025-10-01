import pytest
from models.Database import User, Order
from sqlalchemy import func

class Test_Integrity:
    @pytest.mark.testdb
    @pytest.mark.testintegrity
    def test_no_duplicate_email(self,db_session):
        '''Test that duplicate emails are avoided'''
        duplicate = (
            db_session.query(User.email,func.count(User.id))
            .group_by(User.email)
            .having(func.count(User.id) > 1)
            .all()
        )
        assert len(duplicate) == 0, f"Duplicate emails found: {duplicate}"
        
    
    @pytest.mark.testdb
    @pytest.mark.testintegrity
    def test_no_orphan(self,db_session):
        """Ensure every order belongs to a valid user (no orphan FKs)."""
        orphan_order = (
                db_session.query(Order)
                .outerjoin(User,Order.user_id == User.id)
                .filter(User.id.is_(None))
                .all()
        )
        assert len(orphan_order) == 0, f"Orphan orders found: {orphan_order}"
    
    @pytest.mark.testdb
    @pytest.mark.testintegrity
    def test_email_format(self,db_session):
        '''check that email contains{@}'''
        invalid_emails = db_session.query(User).filter(~User.email.contains("@")).all()
        assert len(invalid_emails) == 0, f"Invalid email formats found: {invalid_emails}"