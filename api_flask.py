from flask import Flask

from .api_result import ApiResult, ApiException


class ApiFlask(Flask):
    def make_response(self, rv):
        if isinstance(rv, ApiResult):
            return rv.to_response()
        return Flask.make_response(self, rv)


def register_error_handlers(app):
    app.register_error_handler(
        ApiException, lambda err: err.to_result())
