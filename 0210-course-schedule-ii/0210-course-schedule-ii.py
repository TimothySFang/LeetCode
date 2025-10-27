class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        # initialize prereq_dict
        prereq_dict = defaultdict(list)
        result = []
        indeg = [0] * numCourses

        for course, prereq in prerequisites:
            prereq_dict[prereq].append(course)
            indeg[course] += 1
        
        q = deque(i for i in range(numCourses) if indeg[i] == 0)
        # add all to queue that have 0 prereqs
        order = []

        while q:
            curr_node = q.popleft()
            order.append(curr_node)
            
            for course in prereq_dict[curr_node]:
                indeg[course] -= 1
                if indeg[course] == 0:
                    q.append(course)

        if len(order) == numCourses:
            return order
        else:
            return []

        

        
        