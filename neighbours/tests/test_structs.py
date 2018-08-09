# -*- coding: utf-8 -*-
from neighbours.kdtree import SortedDistanceList


def test_sorted_distance_list():
    lst_size = 4

    lst = SortedDistanceList(lst_size)
    assert lst_size == lst.size

    lst.add('item 1', 10.0)
    assert lst_size == lst.size
    assert 1 == len(lst)
    assert lst[0] == ('item 1', 10.0)

    lst.add('item 2', 11.0)
    assert lst_size == lst.size
    assert 2 == len(lst)
    assert lst[0] == ('item 1', 10.0)
    assert lst[1] == ('item 2', 11.0)

    lst.add('item 3', 9.0)
    assert lst_size == lst.size
    assert 3 == len(lst)
    assert lst[0] == ('item 3', 9.0)
    assert lst[1] == ('item 1', 10.0)
    assert lst[2] == ('item 2', 11.0)

    lst.add('item 4', 10.5)
    assert lst_size == lst.size
    assert 4 == len(lst)
    assert lst[0] == ('item 3', 9.0)
    assert lst[1] == ('item 1', 10.0)
    assert lst[2] == ('item 4', 10.5)
    assert lst[3] == ('item 2', 11.0)

    lst = SortedDistanceList(lst_size)
    lst.add('item 1', 1.0)
    lst.add('item 2', 2.0)
    lst.add('item 3', 3.0)
    lst.add('item 4', 4.0)
    assert lst_size == lst.size
    assert 4 == len(lst)
    assert lst[0] == ('item 1', 1.0)
    assert lst[1] == ('item 2', 2.0)
    assert lst[2] == ('item 3', 3.0)
    assert lst[3] == ('item 4', 4.0)
