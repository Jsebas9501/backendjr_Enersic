from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Person
from .forms import PersonForm
import json

# Create your views here.

class PersonView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if(id>0):
            people = list(Person.objects.filter(id = id).values())
            if len(people) > 0:
                person = people[0]
                data = {'message': 'Succes', 'person':person}
            else:
                data = {'message': 'People not found...'}
            return JsonResponse(data)
        else:
            people = list(Person.objects.values())
            if len(people) > 0:
                data = {'message': 'Succes', 'people':people}
            else:
                data = {'message': 'People not found...'}
            return JsonResponse(data)

    def post(self, request):
        form = PersonForm(json.loads(request.body))
        if form.is_valid():
            form.save()
            data = {'message': 'Success'}
            return JsonResponse(data)
        else:
            data = {'message': 'Error', 'errors': form.errors}
            return JsonResponse(data)

    def put(self, request, id):
        person = get_object_or_404(Person, id=id)
        form = PersonForm(json.loads(request.body), instance=person)
        if form.is_valid():
            form.save()
            data = {'message': 'Success'}
            return JsonResponse(data)
        else:
            data = {'message': 'Error', 'errors': form.errors}
            return JsonResponse(data)


    def delete(self, request, id):
        person = get_object_or_404(Person, id=id)
        person.delete()
        data = {'message': 'Success'}
        return JsonResponse(data)
