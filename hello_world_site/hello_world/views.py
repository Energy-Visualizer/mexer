from django.http import HttpResponse

# Hello world view
def hello_world_index(request):
    return HttpResponse("Hello, world!")