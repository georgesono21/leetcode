class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:

        # intuition, use bfs from source pixel, only explore nodes that have same pixel value, if they do update and add to queue.
        # optimization: no visited set and we can mark visited in the matrix itself

        def isValid(r, c, original, image):
            if (
                r < len(image)
                and r >= 0
                and c >= 0
                and c < len(image[0])
                and image[r][c] == original
            ):
                return True
            return False

        queue = [(sr, sc)]
        original = image[sr][sc]

        if color == original:
            return image

        unitVectors = [[0, -1], [0, 1], [1, 0], [-1, 0]]
        while queue:
            r, c = queue.pop(0)
            image[r][c] = color

            for dr, dc in unitVectors:
                newR = r + dr
                newC = c + dc
                if isValid(newR, newC, original, image):
                    queue.append((newR, newC))

        return image

        # time complexity: O(n*m), space complexity: O(n*m)
