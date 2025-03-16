class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
    
        """
        standard heap/sorting question, get the distances from all the points and sort them by distances from mid
        return first k items in that list. time complexity is O(nlogn) from sorting,

        optimization could be using a maxheap and then having it be a window. get the distance and push pop it into the heap
        with this optimization, the time compleixty would be O(nlogk) and space complexity would be O(k)
        """
        dists = list()
        for x,y in points:
            dist = math.sqrt((x - 0) ** 2 + (y - 0) ** 2)

            dists.append(([x,y], dist))
        dists.sort(key = lambda x: x[1])

        res = list()
        for i in range(k):
            res.append(dists[i][0])
        return res

        #time complexity: O(nlogn), space complexity: O(n)
