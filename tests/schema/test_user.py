import pytest
import sqlalchemy as sa 
from sqlalchemy import inspect , Integer,String
from models.Database import Base,User
from conftest import db_session

class TestSchema:
    @pytest.mark.testdb
    @pytest.mark.testschema
    def test_user_schema(self, db_session):
        '''Check table names'''
        inspector = sa.inspect(db_session.bind)
        expected_tables = {"users", "order"}
        actual_tables = set(inspector.get_table_names())
        assert expected_tables.issubset(actual_tables)
    
        '''check columns in users table'''
        inspector = sa.inspect(db_session.bind)
        expected_columns = {"id", "name", "email", "age"}
        columns = {col['name']: col for col in inspector.get_columns("users")}
        assert expected_columns.issubset(columns.keys())

        '''check column types'''
        assert isinstance(columns['id']['type'],Integer)
        assert isinstance(columns['name']['type'],String)
        assert isinstance(columns['email']['type'],String)
        assert isinstance(columns['age']['type'],Integer)

        '''check nullability and primary_key'''
        assert columns['name']['nullable'] is False
        assert columns['email']['nullable'] is False
        assert columns['age']['nullable'] is True
        

        '''check indexes'''
        indexes = inspector.get_indexes('users')
        index_columns = [tuple(index['column_names']) for index in indexes]
        assert any('email' in index for index in index_columns)
        assert any('name' in index for index in index_columns)
        
        '''check relationship'''
        user_mapper = inspect(User)
        assert 'orders' in user_mapper.relationships
        relationship = user_mapper.relationships['orders']
        assert relationship.mapper.class_.__name__ == 'Order'
        assert relationship.back_populates == 'user'

