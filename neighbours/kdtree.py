"""
k-d tree implementation for 2-dimensional points
"""
from collections import namedtuple
from math import sqrt
from pprint import pformat
from typing import Optional, Any


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

    @property
    def is_full(self):
        return self.__len == self.size

    @property
    def is_empty(self):
        return self.__len == 0

    def get_item_distance(self, idx: int) -> Optional[float]:
        return self.__list[idx] and sqrt(self.__list[idx][1]) or None

    def __len__(self):
        return self.__len

    def __getitem__(self, item):
        if item >= self.__len:
            raise IndexError
        return self.__list[item][0]

    def __repr__(self):
        return pformat(tuple(self.__list))


def square_distance(p1: Point, p2: Point):
    """
    Using square distance for speed improving
    """
    return (p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2


class Node(object):
    __slots__ = ('location', 'depth', 'data', 'left', 'right', 'parent')

    def __init__(self, location, depth, data, parent):
        self.location = location
        self.depth = depth
        self.data = data
        self.parent = parent
        self.left = None
        self.right = None

    def __repr__(self):
        return pformat(tuple([self.location, self.data, self.left, self.right]))

    def get_nearest_leaf_node(self, point: Point) -> 'Node':
        current = self
        current_depth = 0
        dimensions = len(self.location)
        while True:
            current_axis = current_depth % dimensions
            if point[current_axis] <= current.location[current_axis]:
                _next = current.left
            else:
                _next = current.right
            if _next is None:
                return current
            current = _next
            current_depth += 1

    def add(self, point: Point, data: Any):
        dimensions = len(self.location)
        parent = self.get_nearest_leaf_node(point)
        axis = parent.depth % dimensions
        new_node = Node(point, parent.depth + 1, data, parent)
        if new_node.location[axis] <= parent.location[axis]:
            parent.left = new_node
        else:
            parent.right = new_node

    def get_neighbours(self, point: Point, cnt: int=1, result: SortedDistanceList=None) -> SortedDistanceList:
        root = self

        dimensions = len(self.location)
        if result is None:
            result = SortedDistanceList(cnt)

        leaf = self.get_nearest_leaf_node(point)
        current_node = leaf
        while True:
            current_distance = square_distance(point, current_node.location)
            if not result.is_full or current_distance < result.max_distance:
                result.add((current_node.location, current_node.data), current_distance)

            # if our nearest radius sphere intersects with splitting pane,
            # there could be nearer points on the other side of the plane
            # we must search all children if we are at the leaf node
            current_axis = current_node.depth % dimensions
            need_search_children = (
                current_node == leaf or
                (point[current_axis] - current_node.location[current_axis]) ** 2 <= result.max_distance
            )
            if need_search_children:
                if current_node == leaf or point[current_axis] < current_node.location[current_axis]:
                    if current_node.right:
                        result = current_node.right.get_neighbours(point, cnt, result)
                if current_node == leaf or point[current_axis] >= current_node.location[current_axis]:
                    if current_node.left:
                        result = current_node.left.get_neighbours(point, cnt, result)

            if current_node == root:
                break
            current_node = current_node.parent

        return result


class KDTree(object):
    """
    K-D tree implementation
    https://en.wikipedia.org/wiki/K-d_tree
    """

    def __init__(self):
        self._root = None

    def add(self, point: Point, data: Any):
        if self._root is None:
            self._root = Node(point, 0, data, None)
        else:
            self._root.add(point, data)

    def get_neighbours(self, point: Point, cnt=1) -> SortedDistanceList:
        if self._root is None:
            return SortedDistanceList(cnt)
        result = self._root.get_neighbours(point, cnt)

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

    def __repr__(self):
        return repr(self._root)
