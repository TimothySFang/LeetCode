class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq_graph = defaultdict(list)
        for course, prereq in prerequisites:
            prereq_graph[prereq].append(course)

        
        visited = set()
        path = set()

        def dfs(node):
            if node in path:
                return False
            if node in visited:
                return True

            path.add(node)
            for prereqs in prereq_graph[node]:
                if not dfs(prereqs):
                    return False
            path.remove(node)
            visited.add(node)

            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True