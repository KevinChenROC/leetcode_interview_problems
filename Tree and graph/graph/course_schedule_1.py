# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

# return False if it's impossible to finish all courses.


class Node:
    def __init__(self):
        self.adj_list = []
        self.discovered = False
        self.finished = False


class Solution(object):
    def isCyclic(self, index, graph):
        graph[index].discovered = True
        cyclic = False

        # scan adj_list of node with the index
        for adj_index in graph[index].adj_list:
            adj_node = graph[adj_index]
            if adj_node.discovered:
                if not adj_node.finished:
                    cyclic = True
            else:
                cyclic = cyclic or self.isCyclic(adj_index, graph)

        graph[index].finished = True
        return cyclic

    def canFinish(self, numCourses, prerequisites):
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
        for index, node in enumerate(graph):
            if not node.discovered:
                cyclic = cyclic or self.isCyclic(index, graph)

        return not cyclic


# sol = Solution()
# print(sol.canFinish(3, [[1, 0], [1, 2], [2, 1]]))

# test cases
# 2
# [[1,0]]
# 3
# [[1,0], [1,2], [2,1]]
# 3
# [[1,0]]
# 3
# [[1,0], [2,1],[0,2]]
