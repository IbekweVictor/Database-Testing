import pytest
import sqlalchemy as sa
from sqlalchemy import inspect, Integer, String
from models.Database  import Base, User, Order

class TestSchema:
   @pytest.mark.testschema2
   @pytest.mark.testdb
   def test_order_schema(self, db_session):
       
       '''check orders column'''
       inspector = sa.inspect(db_session.bind)
       expected_columns = {'id', 'user_id'}
       order_columns = {col['name']: col for col in inspector.get_columns("orders")}
       assert expected_columns.issubset(order_columns.keys())

       '''check column types'''
       assert isinstance(order_columns['id']['type'] ,Integer)
       assert isinstance(order_columns['user_id']['type'],Integer)

       '''check index'''
       index = inspector.get_indexes('orders')
       order_index = [tuple(idx['column_names'])for idx in index]
       assert any('user_id' in idx for idx in order_index)
       
       '''check foreign key'''
       foreign_keys = inspector.get_foreign_keys('orders')
       assert len(foreign_keys) == 1
       foreignkey = foreign_keys[0]
       assert foreignkey['referred_table'] == 'users'
       assert foreignkey['referred_columns'] == ['id']
       assert foreignkey['constrained_columns'] == ['user_id']

       '''check relationship'''
       order_mapper = inspect(Order)
       assert 'user' in order_mapper.relationships
       relationship = order_mapper.relationships['user']
       assert relationship.mapper.class_.__name__ == 'User'
       assert relationship.back_populates == 'orders'
