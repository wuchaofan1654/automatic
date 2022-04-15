from django.http import HttpResponse

# Create your views here.


def test_view(request, api_id):
    return HttpResponse(f'test: {api_id}')
