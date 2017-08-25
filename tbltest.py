from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from datetime import datetime, tzinfo, timedelta
import pytz
from flask_table import Table, Col, create_table


class ItemTable(Table):
    name = Col('Name')
    description = Col('Description')

items = [dict(name='Name1', description='Description1'),
         dict(name='Name2', description='Description2'),
         dict(name='Name3', description='Description3')]

table = ItemTable(items)
print(table.__html__())

TableCls = create_table('TableCls').add_column('name', Col('Name'))
TableCls.add_column('description', Col('Description'))
print(TableCls.__html__())
