from typing import TypeAlias

from sqlalchemy import select, insert, desc
from database.settings import engine, regression_values


first_elem = int
coefficient = int
number = int
RegressionParams: TypeAlias = tuple[first_elem, coefficient, number]


def insert_regression_params(params: RegressionParams) -> None:
    with engine.connect() as connection:
        stmt = insert(regression_values).values(
            first_elem=params[0], coefficient=params[1], number=params[2]
        )
        connection.execute(stmt)


def get_last_five_values() -> list[RegressionParams]:
    with engine.connect() as connect:
        stmt = select(
            regression_values.c.first_elem, regression_values.c.coefficient,
            regression_values.c.number
        ).order_by(desc('id')).limit(5)
        result = connect.execute(stmt).fetchall()

        return result


def get_last_five_coefficients() -> list[tuple[int]]:
    with engine.connect() as connect:
        stmt = select(regression_values.c.coefficient).order_by(
            desc('id')
        ).limit(5)

        result = connect.execute(stmt).fetchall()

        return result
