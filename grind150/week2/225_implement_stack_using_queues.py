class MyStack:
    """
    the most recently added item would be at the end of the queue, so we would need to therefore
    pop all elements off to get the most recently added element. to preserve the order, when
    we pop off the front of the queue, we enqueue it to the other queue. the last item in our 
    original queue would be what we return in pop/top, except in pop, we wouldnt add it into our
    other queue—instead discarding it
    """
    def __init__(self):
        q1 = list()
        q2 = list()
        self.q1, self.q2 = q1, q2

    def push(self, x: int) -> None:
        q1, q2 = self.q1, self.q2 
        q1.append(x)
        #O(1) time
        

    def pop(self) -> int:
        q1, q2 = self.q1, self.q2 
        q1Len = len(q1)
        lastPopped = None
        for i in range(q1Len-1):
            lastPopped = q1.pop(0)
            q2.append(lastPopped)
        top = q1[0]

        print("pop", top, q2, q1)
        q1 = list()

        for i in range(q1Len-1):
            q1.append(q2.pop(0))
        self.q1 = q1
        
        return top

    def top(self) -> int:
        q1, q2 = self.q1, self.q2 
        q1Len = len(q1)
        lastPopped = None

        for i in range(q1Len):
            lastPopped = q1.pop(0)
            q2.append(lastPopped)
        top = lastPopped


        for i in range(q1Len):
            q1.append(q2.pop(0))
        
        return top
    #O(n) time O(n) space
        

    def empty(self) -> bool:
        q1, q2 = self.q1, self.q2 
        if not q1:
            return True
        else:
            return False
    #O(1) time O(1) space
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
