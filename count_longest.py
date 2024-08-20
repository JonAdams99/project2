# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 4: COUNT THE LONGEST SUBSEQUENCE
#
# NAME:         Jon Adams
# ASSIGNMENT:   Project 2: Stacks & Queues

from Queue import Queue

# count longest sequence of duplicates in a queue
# can destroy the queue & make it empty
def count_longest(q):
    len = 0
    # s= stack[]
    count1 =1
    countLongest = 0
    previous = q.deq()
    next = ""
    while not q.is_empty():
        next = q.deq()
        #print(previous, next)
        if previous == next:
            count1 +=1
            #print(count1)
        
        elif previous != next:
            if countLongest < count1:
                countLongest = count1
                count1=1
      

        previous = next
    if countLongest <count1:
        countLongest = count1
    return countLongest



def main():
    print("out 2:", count_longest(Queue([l for l in "helloo"])))
    print("out 5:", count_longest(Queue([l for l in "m" * 5])))
    print("out 3:", count_longest(Queue([l for l in "heee" ])))


# Don't run main on import
if __name__ == "__main__":
    main()

