from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Sport
from .serializers import SportSerializer
from .forms import SportInsertForm
import requests


# Create your views here.
@api_view(['POST'])
def savesport_api(request):
    if request.method == 'POST':
        serialized_color_obj = SportSerializer(data=request.data)
        if serialized_color_obj.is_valid():
            serialized_color_obj.save()
            return Response(serialized_color_obj.data, status=status.HTTP_201_CREATED)
        return Response(serialized_color_obj.data, status=status.HTTP_400_BAD_REQUEST)


def savesport(request):
    form = SportInsertForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save(commit=False)
            data = {"name": form.cleaned_data.get("sportnames")}
            post_data = requests.post(
                'http://localhost:8000/api/sportnew/',
                headers={'Content-Type': 'application/json'},
                json=data,
            )
            return redirect('/')
    return render(request, 'core/insert.html', {'form': form})
