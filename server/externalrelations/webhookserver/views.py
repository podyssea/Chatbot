# from django.shortcuts import render
from json import loads
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .utils import deep_get
from .intent_handler import handle


@csrf_exempt
def webhook(request):
    if request.method == 'GET':
        return HttpResponse("Hello World, from webhook!", content_type='text/html')
    else:
        data = loads(request.body)
        user_intent = deep_get(data, 'queryResult.intent.displayName')
        if user_intent is None:
            return JsonResponse({
                'fulfillmentText': 'Something happened on our end.'
            })
        elif user_intent == 'Test':
            return JsonResponse({
                'fulfillmentText': 'Test Passed'
            })
        
        parameters = deep_get(data, 'queryResult.parameters')
        return_data = handle({'intent': user_intent, 'parameters': parameters})

        return JsonResponse({
            'fulfillmentText': return_data
        })
