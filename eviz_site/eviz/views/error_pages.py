####################################################################
## Error pages
#####################

from django.shortcuts import render
from utils.logging import LOGGER

# TODO: log messages should be more descriptive
def error_400(request, exception: Exception | str):
        LOGGER.error(str(exception))
        return render(request, 'error_pages/400.html', status=400)

def error_403(request, exception: Exception | str):
        LOGGER.error(str(exception))
        return render(request, 'error_pages/403.html', status=403)

def error_404(request, exception: Exception | str):
        LOGGER.error(str(exception))
        return render(request, 'error_pages/404.html', status=404)

def error_500(request):
        return render(request, 'error_pages/500.html', status=500)

def csrf_failure(request, reason=""):
        return error_403(request, reason)