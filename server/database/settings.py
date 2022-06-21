from sqlalchemy import create_engine, Table, Integer, MetaData, Column

import config

DB_URL = (
    f'postgresql://{config.pg_user}:'
    f'{config.pg_password}@{config.pg_host}:{config.pg_port}'
    f'/{config.pg_database}'
)

engine = create_engine(
    DB_URL
)

meta = MetaData()


regression_values = Table(
    'regression_values',  meta,
    Column('id', Integer, primary_key=True),
    Column('first_elem', Integer, nullable=False),
    Column('coefficient', Integer, nullable=False),
    Column('number', Integer, nullable=False)
)
