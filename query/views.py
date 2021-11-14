from django.http import JsonResponse, HttpResponse
from . import util
from .models import Data
import asyncio
import json
from celery.result import AsyncResult
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from celery.result import AsyncResult

from .tasks import create_task


def search(request):
    # util.query(request)
    # check if new search req or requesting page from new prev search req
    if request.method == "POST":
        params = request.body.decode('utf-8')
        query = json.loads(params).get("q")
        task = create_task.delay(query)
        return JsonResponse({"task_id": task.id}, status=202)


def search_with_task(request, task_id, page=1):
    if request.method == "GET":
        if page>50:
            return HttpResponse(status=400)
        resp = util.retrive(task_id, page)
        return JsonResponse(resp)
