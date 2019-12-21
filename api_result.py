from flask import json, Response, request
from werkzeug.urls import url_join


class ApiResult(object):

    def __init__(self, value, status=200, next_page=None):
        self.value = value
        self.status = status
        self.next_page = next_page

    def to_response(self):
        rv = Response(json.dumps(self.value),
                      status=self.status,
                      mimetype='application/json')
        if self.next_page is not None:
            rv.headers['link'] = '<%s>; rel="next' % url_join(request.url, self.next_page)

        return rv


class ApiException(object):

    def __init__(self, message, status=400):
        self.message = message
        self.status = status

    def to_result(self):
        return ApiResult({'message': self.message},
                         status=self.status)
