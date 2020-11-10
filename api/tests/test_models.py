from datetime import date

from django.test import TestCase

from api.models import (
    Harvest,
    Specie,
    Tree,
    TreeGroup
)


class TestTree(TestCase):
    def setUp(self):
        Tree.objects.create(
            description="White Ash",
            age=12,
            specie=Specie.objects.create(description="Americana"))

    def test_tree_get_name(self):
        tree_name = str(Tree.objects.get(description="White Ash"))
        self.assertEqual(tree_name, "White Ash - Americana")


class TestTreeGroup(TestCase):
    def setUp(self):
        self.tree_group = TreeGroup.objects.create(
            name="Group1",
            description="White Tree")
        self.tree_group.trees.add(
            Tree.objects.create(
                description="White Ash",
                age=12,
                specie=Specie.objects.create(description="Americana")))
    
    def test_tree_group_get_name(self):
        tree_group_name = str(TreeGroup.objects.get(name="Group1"))
        self.assertEqual(tree_group_name, "Group1")


class TestSpecie(TestCase):
    def setUp(self):
        Specie.objects.create(description="Brasileira")
    
    def test_specie_get_name(self):
        specie_name = str(Specie.objects.get(description="Brasileira"))
        self.assertEqual(specie_name, "Brasileira")


class TestHarvest(TestCase):
    def setUp(self):
        Harvest.objects.create(
            info="Winter's harvest",
            harvest_date=date(year=2020, month=8, day=24),
            gross_weight=78.7,
            tree=Tree.objects.create(
                description="White Ash",
                age=12,
                specie=Specie.objects.create(description="Americana")))
    
    def test_harvest_information(self):
        harvest = Harvest.objects.get(info="Winter's harvest")
        harvest_info = harvest.get_all_info()
        string = f"""
        Winter's harvest occurs in 2020-08-24

        Tree: White Ash - Americana
        Gross weight: 78.70
        """
        self.assertEqual(harvest_info, string)
        self.assertEqual(str(harvest), "Date 2020-08-24 - Winter's harvest")