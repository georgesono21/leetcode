class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        """
        initial approach: BFS from every non zero node until we reach a zero, than breakout and then
        set that node's value to the distance. we explore the entire matrix m*n times per cell (m * n)
        obviously, this led to a TLE

        second approach: start from all zero positions with them loaded in the queue and span out from
        each point in a BFS manner. this makes it so we only have to explore the matrix once. passes now!
        """
        queue = []
        visited = set()
        for i,_ in enumerate(mat):
            for j,v in enumerate(mat[i]):
                if v == 0:
                    queue.append((i,j))
                    visited.add((i,j))
    
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        while queue:
            x = queue.pop(0)
            for dr,dc in dirs:
                r,c = dr + x[0], dc + x[1]
                if r >= 0 and r < len(mat) and c >= 0 and c < len(mat[r]) and (r,c) not in visited:
                    mat[r][c] = mat[x[0]][x[1]] + 1
                    visited.add((r,c))
                    queue.append((r,c))

        return mat

        # time complexity O(m * n), space complexity O(m * n)
