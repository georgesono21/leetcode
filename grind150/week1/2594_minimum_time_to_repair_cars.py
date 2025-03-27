class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        """
        intuiton: similar to koko eating banans, determine an upperbound of the time needed

        what was tricky was finding. the equation to see n cars are even able to finish
        n cars within a given time, honestly once i saw the equation of T = r * n^2, it makes
        sense how you can calculate the total cars done. 

        i was mainly stuck on finding the right distribution but once i got the equation it all
        started. tomake sense. go over all the mechanics ranks and see the total number of cars
        they can all repair. check if we can keep decresing this number until we reach the condition
        that we cant repairs `cars` cars within `mid` time.

        looked at intuition 18 minutes in
        solved and submitted 34 minutes in

        """
        highestTime = r = min(ranks)*(cars**2)
        lowestTime = l = 0

        #T = r * n^2
        #n = sqrt(r/T)

        def totalCarsGivenTime(ranks,cars,fixedTime):
            totalCars = 0
            for i, rank in enumerate(ranks):
                maxCars = math.sqrt(fixedTime/rank)
                totalCars += int(maxCars)
            return totalCars


        while l < r:

            mid = (l + r) // 2
            maxCars = totalCarsGivenTime(ranks,cars,mid)

            if maxCars >= cars:
                r = mid
            else:
                l = mid+1
        
        return r

        #time complexity: O(len(ranks)*log(min(ranks) * cars * cars)), space complexity: O(1)
    
