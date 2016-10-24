from django.utils.deprecation import MiddlewareMixin


class MyMiddleWare1(MiddlewareMixin):

    def __init__(self,get_response=None):
        self.get_response = get_response

    def process_request(self, request):
        print("MyMiddleware1.process_request()")

    def process_response(self, request, response):
        print("MyMidelware1.process_response()")
        return response

class MyMiddleWare2(MiddlewareMixin):

    def __init__(self,get_response=None):
        self.get_response = get_response

    def process_request(self, request):
        print("MyMiddleware2.process_request()")

    def process_response(self, request, response):
        print("MyMidelware2.process_response()")
        return response
