from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database.settings import meta, engine
from database.service import (
    get_last_five_values, insert_regression_params,
    get_last_five_coefficients
)

import redis

import config

from service import gs_calculator

app = FastAPI()

origins = [
    "http://localhost:3050",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

meta.create_all(bind=engine)


r = redis.Redis(
    host=config.redis_host, port=config.redis_port,
)


@app.get('/')
def get_index():
    return {
        'title': 'Realizacja zadania nr2 w ramach laboratorium TCh',
        'author': 'Mark Zaianchkovskyi'
        }


@app.get('/gs_cal/')
def get_gs(a: int, k: int, n: int):
    result = gs_calculator(a, k, n)
    result_str = ' '.join(str(elem) for elem in result)

    insert_regression_params((a, k, n))

    r.set(f'{a} {k} {n}', result_str)

    return {'result': result_str}


@app.get('/gs_cal/history/')
def get_gs_history():
    last_five_values = get_last_five_values()
    last_five_values_str = [
        ' '.join(str(elem_) for elem_ in elem) for elem in last_five_values
    ]

    result = {}
    for str_elem in last_five_values_str:
        result[str_elem] = r.get(str_elem)

    return result


@app.get('/gs_cal/history/coefficients/')
def get_coefficient_history():
    last_five_coefficient: list = get_last_five_coefficients()
    return {'result': last_five_coefficient}
