from flask import app, request

from api_result import ApiException, ApiResult


@app.route('/add')
def add_numbers():
    a = request.args('a', type=int)
    b = request.args('b', type=int)

    if a is None or b is None:
        raise ApiException('Numbers must be integers')

    return ApiResult({'sum': a + b})
