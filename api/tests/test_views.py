from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from api.models import (
    Specie,
    Tree,
    TreeGroup,
    Harvest
)


class ViewsTests(APITestCase):
    def setUp(self):
        self.test_data = [
            ('specie-list', {'description': 'dummy-specie'}),
            ('tree-list',
            {'description': 'dummy-tree', 'age': 12, 'specie': 1}),
            ('tree-group-list', {
                'name': 'dummy-group',
                'description': 'dummy-group-tree',
                'trees': [1]
                }
            ),
            ('harvest-list', {
                'info': 'harvest-dummy',
                'harvest_date': '2020-08-24',
                'gross_weight': 78.4,
                'tree': 1
                }
            )
        ]

        self.invalid_test_data = [
            ('specie-list', {'description': None}),
            ('tree-list',
            {'description': 'dummy-tree', 'age': '12', 'specie': 0}),
            ('tree-group-list', {
                'name': 'dummy-group',
                'description': 'dummy-group-tree',
                'trees': 1
                }
            ),
            ('harvest-list', {
                'info': 'harvest-dummy',
                'harvest_date': 'date',
                'gross_weight': 78.4,
                'tree': '1'
                }
            )
        ]

    def test_creating_and_destroying_models(self):
        for url, data in self.test_data:
            response = self.client.post(reverse(url), data, format='json')
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        self.assertEqual(Specie.objects.get().description, 'dummy-specie')
        self.assertEqual(Tree.objects.get().description, 'dummy-tree')
        self.assertEqual(TreeGroup.objects.get().name, 'dummy-group')
        self.assertEqual(Harvest.objects.get().info, 'harvest-dummy')

        views_names = (
            'harvest-detail',
            'tree-group-detail',
            'tree-detail',
            'specie-detail'
        )

        for url in views_names:
            response = self.client.delete(reverse(url, kwargs={'pk': 1}))
            self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


    def test_create_invalid_models(self):
        for url, data in self.invalid_test_data:
            response = self.client.post(reverse(url), data, format='json')
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
