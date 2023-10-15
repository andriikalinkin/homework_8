import time

from . write_dict_to_file import write


class LogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        start_time = time.time()
        data = {
            "request_path": request.path,
            "request_method": request.method
        }

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.
        data["execution_time"] = time.time() - start_time
        write(data)

        return response
