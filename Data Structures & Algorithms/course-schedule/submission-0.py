class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        no_of_requisites = [0] * numCourses
        adj = [[] for i in range(numCourses)]

        for node1, node2 in prerequisites:
            adj[node1].append(node2)
            no_of_requisites[node2] += 1

        dq = deque([i for i in range(numCourses) if no_of_requisites[i] == 0])

        finish = 0
        while dq:
            course = dq.popleft()
            # mark as finished 
            finish += 1

            for neigh in adj[course]:
                no_of_requisites[neigh] -= 1
                if no_of_requisites[neigh] == 0:
                    dq.append(neigh)

        return finish == numCourses

            


