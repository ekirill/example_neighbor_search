"""
k-d tree implementation for 2-dimensional points
"""
import sys
from collections import namedtuple
from pprint import pformat
from typing import Optional, Any, List


class Point(namedtuple('Point', 'x y')):
    def __repr__(self):
        return pformat(tuple(self))


class SortedDistanceList(object):
    def __init__(self, size):
        self.__list = [None] * size
        self.__len = 0

    def add(self, item: Any, distance: float):
        for idx in range(self.size):
            if self.__list[idx] is None:
                self.__list[idx] = (item, distance)
                self.__len += 1
                break

            if self.__list[idx][1] > distance:
                _cur, self.__list[idx] = self.__list[idx], (item, distance)
                for idx2 in range(idx + 1, self.size):
                    _cur, self.__list[idx2] = self.__list[idx2], _cur
                    self.__len = idx2 + 1
                    if _cur is None:
                        break
                break

    @property
    def max_distance(self) -> Optional[float]:
        if not self.__len:
            return None
        return self.__list[self.__len - 1][1]

    @property
    def size(self):
        return len(self.__list)

    def __len__(self):
        return self.__len

    def __getitem__(self, item):
        if item == self.__len:
            raise IndexError
        return self.__list[item]


class Node(namedtuple('Node', 'location data left right parent')):
    def __repr__(self):
        return pformat(tuple(self))


class KDTree(object):
    DIMENSIONS = 2

    def __init__(self):
        self._root = None

    def get_nearest_leaf_node(self, point: Point):
        if not self._root:
            return None, None

        current = self._root
        current_depth = 0
        while True:
            current_axis = current_depth % self.DIMENSIONS
            _next = point[current_axis] <= current.location[current_axis] and current.left or current.right
            if _next is None:
                return current, current_depth
            current = _next
            current_depth += 1

    def add(self, point: Point, data: Any):
        new_node = Node(point, data, None, None, None)
        parent, depth = self.get_nearest_leaf_node(point)
        if parent is None:
            self._root = new_node
        else:
            axis = depth % self.DIMENSIONS
            new_node.parent = parent
            if point[axis] <= parent.location[axis]:
                parent.left = new_node
            else:
                parent.right = new_node

    @classmethod
    def _distance(cls, p1: Point, p2: Point):
        """
        Using square distance for improving speed
        """
        return (p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2

    def get_neighbours(self, point: Point, k=1) -> List[Node]:
        result = SortedDistanceList(k)

        current_node, current_depth = self.get_nearest_leaf_node(point)
        # TODO
        return result

    def rebalance(self):
        """
        Rebuild the tree for balancing.
        Need to be implemented
        """
        raise NotImplementedError

    def remove(self, node: Node):
        """
        Remove node from the tree.
        Need to be implemented
        """
        raise NotImplementedError
