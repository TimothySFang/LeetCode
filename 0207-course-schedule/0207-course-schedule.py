class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course_dict = defaultdict(list)
        visited = set()
        for course, prereq in prerequisites:
            course_dict[prereq].append(course)
        
        def dfs(curr_node, path):
            prereqs = course_dict[curr_node]
            if curr_node in path:
                return False
            if curr_node in visited:
                return True

            for p in prereqs:
                if not dfs(p, path + [curr_node]):
                    return False
            visited.add(curr_node)
            return True


        for n in range(numCourses):
            # call graph traversal algo
            if not dfs(n, []):
                return False
        return True
