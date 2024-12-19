"""
class ExecutionFlowMiddleware(object):
    def __init__(self,get_response):
        print('init method execution.....')
        self.get_response = get_response
    def __call__(self,request):
        print('Pre processing of request')
        response = self.get_response(request)
        print('Post pocessing of request')
        return response
"""
class FirstMiddleware(object):
    def __init__(self,get_response):
        self.get_response = get_response
    def __call__(self,request):
        print('This line is printed by Middleware-1 before preprocessing request.')
        response = self.get_response(request)
        print('This line is printed by Middleware-1 after preprocessing request.')
        return response

class SecondMiddleware(object):
    def __init__(self,get_response):
        self.get_response = get_response
    def __call__(self,request):
        print('This line is printed by Middleware-2 before preprocessing request.')
        response = self.get_response(request)
        print('This line is printed by Middleware-2 after preprocessing request.')
        return response
