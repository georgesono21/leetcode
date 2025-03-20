class MyQueue:

    """
    use two stacks. when you pop all the elements off and insert them inot the other stack
    the top of the other stack will be the bottom element of the stack you popped off from.
    in this case, that bottom element is the first element in the queue, so for peek and prev
    return that. to make everything back to how it was, move everything back to the origina stack
    and clear the other stack you made to see the bottom element of the original stack.
    """

    def __init__(self):
        self.s1 = list()
        self.s2 = list()

    def push(self, x: int) -> None:
        s1 = self.s1
        s1.append(x)
        #O(1)
        

    def pop(self) -> int:
        s1,s2 = self.s1,self.s2
        s1Len = len(s1)
        for i in range(s1Len):
            s2.append(s1.pop(-1))
        top = s2[-1]
        s2.pop(-1)
        for i in range(s1Len-1):
            s1.append(s2.pop(-1))
        return top

        #O(n)

        

    def peek(self) -> int:
        s1,s2 = self.s1,self.s2
        s1Len = len(s1)
        for i in range(s1Len):
            s2.append(s1.pop(-1))
        top = s2[-1]
        for i in range(s1Len):
            s1.append(s2.pop(-1))
        s2 = list()
        return top
        #O(n)
        

    def empty(self) -> bool:
        s1,s2 = self.s1,self.s2
        if not len(s1):
            return True
        else:
            return False
        #O(1)
        



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
