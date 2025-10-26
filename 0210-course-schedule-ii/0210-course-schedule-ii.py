class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        # initialize prereq_dict
        prereq_dict = defaultdict(list)
        result = []

        for p in prerequisites:
            course = p[0]
            prereq = p[1]
            prereq_dict[course].append(prereq) 
        
        visited = set()
        path = set()

        def dfs(curr_node):
            if curr_node in path:
                return False

            if curr_node in visited:
                return True

            path.add(curr_node)

            for prereq in prereq_dict[curr_node]:
                if not dfs(prereq):
                    return False
                
            path.remove(curr_node)
            visited.add(curr_node)
            result.append(curr_node)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        return result