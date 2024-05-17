from typing import Any


# def my_middleware(get_response):
#     print('one Time Initialization')
#     def my_function(request):
#         print("This is before view")
#         response = get_response(request)
        
#         return response
#     return my_function


class MyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print('One time exec')
    def __call__(self, request):
        print('Before view is called')
        response = self.get_response(request)
        print('After view is called')
        return response