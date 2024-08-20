# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 3: GENERATE BINARY NUMBER STRINGS
#
# NAME:         Jon Adams
# ASSIGNMENT:   Project 2: Stacks & Queues

from Queue import Queue

# generate & return a queue of binary number strings from 1 to N
# front of queue begins @ '1', returns empty Queue otherwise
def generate_binary_numbers(N):
      # Create an empty queue
    n = N
    q = Queue([])
    numbers = Queue([])

    s1 = ""
    # Enqueue the first binary number
    q.enq("1")

    # This loop is like BFS of a tree with 1 as root
    # 0 as left child and 1 as right child and so on
    while(n > 0):
        n -= 1
        # Print the front of queue
        s1 = q.deq()
        numbers.enq(s1)

        # Append "0" to s1 and enqueue it
        q.enq(s1+"0")

        # Append "1" to s1 and enqueue it. 
        q.enq(s1+"1")

    return numbers

def main():
    generate_binary_numbers(2).print()
    generate_binary_numbers(3).print()
    generate_binary_numbers(6).print()


# Don't run main on import
if __name__ == "__main__":
    main()

