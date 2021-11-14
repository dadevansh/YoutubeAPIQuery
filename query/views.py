
from django.http import JsonResponse
from . import util
import asyncio


def search(request):
    util.query(request)
    


