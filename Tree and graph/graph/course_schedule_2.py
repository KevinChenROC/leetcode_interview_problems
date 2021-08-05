# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

# Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.


class Node:
    def __init__(self):
        self.adj_list = []
        self.discovered = False
        self.finished = False


class Solution(object):
    def _topo_order_sort(self, index, topo_order, graph):
        graph[index].discovered = True
        cyclic = False

        # scan adj_list of node with the index
        for adj_index in graph[index].adj_list:
            adj_node = graph[adj_index]
            if adj_node.discovered:
                if not adj_node.finished:
                    cyclic = True
            else:
                iscyclic, topo_order = self._topo_order_sort(
                    adj_index, topo_order, graph
                )
                cyclic = cyclic or iscyclic

        graph[index].finished = True
        return (cyclic, [index] + topo_order)

    def topo_order_sort(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        # Construct a graph from prereq.
        graph = []
        for i in range(numCourses):
            graph.append(Node())

        for prereq in prerequisites:
            a, b = prereq
            graph[b].adj_list.append(a)

        # Detech a cycle using DFS
        cyclic = False
        topo_order = []
        for index, node in enumerate(graph):
            if not node.discovered and not node.finished:
                iscyclic, topo_order = self._topo_order_sort(index, topo_order, graph)
                cyclic = iscyclic or cyclic
        return (not cyclic, topo_order)

    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        canFinish, topo_order = self.topo_order_sort(numCourses, prerequisites)
        if not canFinish:
            return []
        else:
            return topo_order


# sol = Solution()
# print(sol.findOrder(3, [[1, 0], [1, 2], [2, 1]]))
# print(sol.findOrder(2, [[1, 0]]))
# print(sol.findOrder(1, []))
# print(sol.findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))

# test cases
# 2
# [[1,0]]
# 3
# [[1,0], [1,2], [2,1]]
# 3
# [[1,0]]
# 3
# [[1,0], [2,1],[0,2]]
# 4
# [[1,0],[2,0],[3,1],[3,2]]
