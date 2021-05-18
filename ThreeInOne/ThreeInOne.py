'''
Credit to https://quastor.org/cracking-the-coding-interview/stacks-and-queues/three-in-one
Cracking the coding interview
Chapter 3 - Stacks and Queues
Stacks and Queues: Three In One
----------------------------------------
Question: Describe how you can use a single array to implement three stacks
Example:  
input: 
output: 
Constraits or Questions you need to ask:
Going to have to understand this solution as I go, doesn't seem to make too much sense to me

Solution notes:
Implement our stacks with fixed capacity
Once a stack is filled, a user cannon push more items to it without
first popping off items
we'll implement the stacks using a single array that has a fixed capacity
Stack 1: uses elements [0, n/3]
Stack 2: uses elements [n/3, 2n/3]
Stack 3: usues elements [2n/3, n]
We will maintain 2 lists of pointers 
List 1 - Tracks where the tops are for each of the 3 stacks
List 2 - Tracks the limits for each of the 3 stacks
'''
class Threestack:
    def __init__(self, capacity = 5):
        capacity = capacity * 3 #3 for 3 stacks
        self.items = [None] * capacity

        #List of Pointers for tops of stacks 0,1,2
        self.tops = [0, capacity//3, 2 * (capacity // 3)]
        self.limits = [capacity//3, 2 * (capacity// 3), capacity ]

    def push(self, stack, item):
        if stack > 2:
            raise ValueError("Stack does no exist")

        if self.tops[stack] >= self.limits[stack]:
            raise Exception(f"stack {stack} is full")

        self.items[self.tops[stack]] = item
        self.tops[stack] += 1

    def pop(self, stack):
        if stack > 2:
            raise ValueError("stack does not exist")
        top = self.tops[stack] - 1
        if top < 0 or self.items[top] == None:
            raise IndexError("pop from empty stack")
        
        item = self.items[top]
        self.items[top] = None
        self.tops[stack] = top

        return item



#Initalize a instance of Threestack
a = Threestack()

#Push value 4 onto stack 0
a.push(0,4)
#Push value 5 onto stack 1
a.push(1,5)
#Push value 7 onto stack 2
a.push(2,7)
#Push value 6 onto stack 0
a.push(0,6)

print(a.pop(0)) #Should pop 6
print(a.pop(1)) #Should pop 5
print(a.pop(2)) #Should pop 7
