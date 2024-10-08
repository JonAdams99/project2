# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 1: REVERSE QUEUE
#
# NAME:         Jon Adams
# ASSIGNMENT:   Project 2: Stacks & Queues

from Queue import Queue
from Stack import Stack


# Return a new queue in reverse order
# Hint: can use a stack to help
def reverse(q_orig):
    q_new = Queue([])
    s_new = Stack([])
    # FIXME
    while not q_orig.is_empty():
        s_new.push(q_orig.deq())

    while not s_new.is_empty():
        q_new.enq(s_new.pop())
        
    return q_new

def main():
    q = Queue(list(range(1, 5)))
    q.print()
    print("reverse: ", end="")
    reverse(q).print()

# Don't run main on import
if __name__ == "__main__":
    main()
