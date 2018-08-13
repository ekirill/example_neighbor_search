# -*- coding: utf-8 -*-
from pprint import pformat

from neighbours.kdtree import SortedDistanceList, KDTree, Point


def test_sorted_distance_list():
    lst_size = 4

    lst = SortedDistanceList(lst_size)
    assert lst_size == lst.size

    lst.add('item 1', 10.0)
    assert lst_size == lst.size
    assert 1 == len(lst)
    assert lst[0] == 'item 1'
    assert lst.get_item_distance(0) == 3.1622776601683795

    lst.add('item 2', 11.0)
    assert lst_size == lst.size
    assert 2 == len(lst)
    assert lst[0] == 'item 1'
    assert lst[1] == 'item 2'
    assert lst.get_item_distance(1) == 3.3166247903554

    lst.add('item 3', 9.0)
    assert lst_size == lst.size
    assert 3 == len(lst)
    assert lst[0] == 'item 3'
    assert lst[1] == 'item 1'
    assert lst[2] == 'item 2'
    assert lst.get_item_distance(2) == 3.3166247903554

    lst.add('item 4', 10.5)
    assert lst_size == lst.size
    assert 4 == len(lst)
    assert lst[0] == 'item 3'
    assert lst[1] == 'item 1'
    assert lst[2] == 'item 4'
    assert lst[3] == 'item 2'
    assert lst.get_item_distance(3) == 3.3166247903554

    lst = SortedDistanceList(lst_size)
    lst.add('item 1', 1.0)
    lst.add('item 2', 2.0)
    lst.add('item 3', 3.0)
    lst.add('item 4', 4.0)
    assert lst_size == lst.size
    assert 4 == len(lst)
    assert lst[0] == 'item 1'
    assert lst[1] == 'item 2'
    assert lst[2] == 'item 3'
    assert lst[3] == 'item 4'


def test_kd_tree_add():
    tree = KDTree()
    tree.add(Point(11, 10), '1')
    assert pformat(((11, 10), '1', None, None)) == str(tree)
    tree.add(Point(20, 10), '2')
    assert pformat(((11, 10), '1', None, ((20, 10), '2', None, None))) == str(tree)
    tree.add(Point(5, 10), '3')
    assert pformat(((11, 10), '1', ((5, 10), '3', None, None), ((20, 10), '2', None, None))) == str(tree)
    tree.add(Point(8.7, 35.3), '4')
    assert \
        pformat(((11, 10), '1', ((5, 10), '3', None, ((8.7, 35.3), '4', None, None)), ((20, 10), '2', None, None))) == \
        str(tree)


def test_kd_tree_search():
    tree = KDTree()
    tree.add(Point(1, 1), 1)
    tree.add(Point(2, -1), 2)
    tree.add(Point(-2, 1), 3)
    tree.add(Point(-1, -1), 4)
    tree.add(Point(-2, 3), 5)
    tree.add(Point(5, 4), 6)

    assert [6] == [item[1] for item in tree.get_neighbours(Point(3, 3), 1)]
    assert [6, 1] == [item[1] for item in tree.get_neighbours(Point(3, 3), 2)]
    assert [6, 1, 2] == [item[1] for item in tree.get_neighbours(Point(3, 3), 3)]
    assert [6, 1, 2, 5] == [item[1] for item in tree.get_neighbours(Point(3, 3), 4)]
    assert [6, 1, 2, 5, 3] == [item[1] for item in tree.get_neighbours(Point(3, 3), 5)]
    assert [6, 1, 2, 5, 3, 4] == [item[1] for item in tree.get_neighbours(Point(3, 3), 6)]
