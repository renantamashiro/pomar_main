from django.shortcuts import render
from django.http import JsonResponse

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import mixins
from rest_framework import generics


from api.models import (
    Specie,
    TreeGroup,
    Tree,
    Harvest
)

from api.serializers import (
    SpecieModelSerializer,
    TreeModelSerializer,
    TreeGroupModelSerializer,
    HarvestModelSeralizer,
    TreeModelSerializerCreate,
    TreeGroupModelSerializerCreate,
    HarvestModelSeralizerCreate
)


class SpecieList(generics.ListCreateAPIView):
    queryset = Specie.objects.all()
    serializer_class = SpecieModelSerializer


class SpecieDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Specie.objects.all()
    serializer_class = SpecieModelSerializer


class TreeList(generics.ListCreateAPIView):
    queryset = Tree.objects.all()
    serializer_class = TreeModelSerializer


class TreeNew(generics.ListCreateAPIView):
    queryset = Tree.objects.all()
    serializer_class = TreeModelSerializerCreate


class TreeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tree.objects.all()
    serializer_class = TreeModelSerializer


class TreeGroupList(generics.ListCreateAPIView):
    queryset = TreeGroup.objects.all()
    serializer_class = TreeGroupModelSerializer


class TreeGroupNew(generics.ListCreateAPIView):
    queryset = TreeGroup.objects.all()
    serializer_class = TreeGroupModelSerializerCreate


class TreeGroupDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TreeGroup.objects.all()
    serializer_class = TreeGroupModelSerializer


class HarvestList(generics.ListCreateAPIView):
    queryset = Harvest.objects.all()
    serializer_class = HarvestModelSeralizer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['info', 'harvest_date', 'tree', 'tree_group']


class HarvestNew(generics.ListCreateAPIView):
    queryset = Harvest.objects.all()
    serializer_class = HarvestModelSeralizerCreate


class HarvestDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Harvest.objects.all()
    serializer_class = HarvestModelSeralizer

