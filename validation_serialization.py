from functools import update_wrapper

from flask import request, app
from voluptuous import Invalid, Schema, REMOVE_EXTRA

from api_result import ApiException, ApiResult


def dataschema(schema):
    def decorator(f):
        def new_func(*args, **kwargs):
            try:
                kwargs.update(schema(request.get_json()))
            except Invalid as e:
                raise ApiException('Invalid data: %s (path "%s")', % (e.msg, '.'.join(e.path)))

            return f(*args, **kwargs)
        return update_wrapper(new_func, f)
    return decorator


@app.route('/add', methods=['POST'])
@dataschema(Schema({
    'a': int,
    'b': int,
}, extra=REMOVE_EXTRA))
def add_numbers(a, b):
    return ApiResult({'sum': a + b})
