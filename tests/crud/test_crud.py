import pytest
from models.Database import User
from sqlalchemy import and_

class Test_CRUD:
    @pytest.mark.testdb
    @pytest.mark.testcrud
    def test_create_user(self, db_session):
        '''Test create user'''
        new_user = User(name='Victor uriel', age=21, email='victor123@example.com')
        db_session.add(new_user)
        db_session.commit()
        created_user = db_session.query(User).filter_by(email='victor123@example.com').first()
        assert created_user is not None
        assert created_user.name == 'Victor uriel'
        assert created_user.age == 21
        assert created_user.email == 'victor123@example.com'

    @pytest.mark.testdb
    @pytest.mark.testcrud
    def test_update_user(self, db_session):
        '''Test update user'''
        new_user = User(name = 'Carley Humpson', age = 23, email ='carley11@example.com')
        db_session.add(new_user)
        db_session.commit()
        user = db_session.query(User).filter_by(email='carley11@example.com').first()
        user.age = 22
        db_session.commit()
        updated_age = db_session.query(User).filter_by(email = 'carley11@example.com').first()
        assert updated_age.age == 22

    @pytest.mark.testdb
    @pytest.mark.testcrud
    def test_delete_user(self, db_session):
        '''Test delete user'''
        new_user = User(name = 'Carley Humpson', age = 23, email ='carley11@example.com')
        db_session.add(new_user)
        db_session.commit()
        user = db_session.query(User).filter_by(email='carley11@example.com').first()
        db_session.delete(user)
        db_session.commit()
        assert db_session.query(User).filter_by(email='carley11@example.com').first() is None
