from django.http import HttpResponseForbidden

class DisallowedUrlsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # Define your disallowed URLs here
        self.disallowed_urls = ['/api/declare', '/api/undeclare']

    def __call__(self, request):
        # Check if the request path is in the disallowed URLs
        if request.path in self.disallowed_urls:
            # Return an error response if the URL is disallowed
            return HttpResponseForbidden('Access to this URL is not allowed')
        
        # Otherwise, proceed with the next middleware or view
        response = self.get_response(request)
        return response