#Selection sort with helper functions swap and find min

def swap(lst, a, b):
    """
    >>> family = ['Ransom', 'Linda', 'Walt', 'Joni']
    >>> swap(family, 3, 2)
    >>> family
    ['Ransom', 'Linda', 'Joni', 'Walt']

    The swap function is relatively simple. Given a list swap to elements at indexes a and b
    This method is great as you dont have to worry about using a third variable to store an
    intermediate state 
    The , packages up the data in a tuple and this method will be very usefull in your coding 
    career so it is a good one to remember

    The pass keyword is similar to return Null. This is becasue the swap code changes the 
    orgignal list
    """
    lst[a], lst[b] = lst[b], lst[a]
    pass
    
def find_min(lst, index):
    """
    >>> find_min(['candlestick', 'pipe', 'rope', 'knife', 'wrench'], 2)
    3
    >>> find_min([1, 3, 5, 11, 7, 3, 2, 6, 2], 3)
    6

    The find min function is used to find the index of the minimum element in a list.
    Finding a minimum element in a list is a common process so it would be good to remember this code

    However, in this example, due to its use in the selection sort function it must find the minimum element
    in the list with indexes greater than the provided index.

    Esentially the best process is to first find the minimum element in a list of length 1,
    aka the first element will always be the minimum element. Then iterate over the list,
    checking if that element is bigger than the current minimum.
    If it is update the minimum index. 
    Finally after the entire list has been iterated upon, return the list
    """
    mini = lst[index] #set the minimum element to the first entry (note that only checking from index to the end of the list) 
    miniIndex = index #store the minimum index
    for i in range(index,len(lst)): #for each element in the list with index greater than inex
        if(mini > lst[i]): #is the current element smaller than the minimum
            mini = lst[i] #if so update index and minimum element
            miniIndex = i
    return miniIndex #return the index of the smallest element found 

# Selection sort
def selection_sort(lst):
    """
    >>> outsiders = ['Marta', 'Edi', 'Frank', 'Benoit']
    >>> selection_sort(outsiders)
    >>> outsiders
    ['Benoit', 'Edi', 'Frank', 'Marta']

    Finally selection sort will utilise the two helper functions to sort the list.
    Creating and using helper functions is a very useful programming practice called decompisiton
    This makes code more readable by decomposing the function into smaller steps.
    Also tests can be run on each section, rather than selection sort as a whole which means
    it is much easier to bugtest and ensure validity of code

    Selection sort works by finding the smallest element in a list and swapping it into position 1
    It then searches the rest of the list (aka from position 2 to the end) for the next smallest 
    element. This will be inserted at position 2.
    It will do this for the entire list untill it is sorted.
    Note that position 1 is actually list index 0 (because arrays start at 0)
    """

    for i in range(len(lst)): #for every element in the list
        #find the index of the minimum element that is abouve (index with a greater magniude)
        min_index = find_min(lst,i) 
        swap(lst,i,min_index) #swap that minimum element with the element at the current position
    pass #because the original list is modified pass instead of return
    # see how in the test case the function returns nothing but the list variable (named outsiders has been modified)


"""
Merge sort with helper function merge 

Merge sort code is provided if the student is interested in a faster sorting method.
Also uses recursion so may be more complex 
"""

def merge(lst1, lst2):
    """
    Input: Two sorted lists lst1, lst2
    Output: One sorted list 'res' merged together

    >>> merge([1, 2, 4, 6], [3, 5, 7, 8])
    [1, 2, 3, 4, 5, 6, 7, 8]

    >>> merge([1, 2, 3], [4, 5, 6])
    [1, 2, 3, 4, 5, 6]

    >>> merge([11, 13, 15], [])
    [11, 13, 15]

    >>> merge([], [16, 18, 20])
    [16, 18, 20]
    """
    n1 = len(lst1)
    n2 = len(lst2)
    i = 0
    j = 0
    a = lst1
    b = lst2

    ret_value = []

    while i<n1 and j <n2:
        if a[i] > b[j]:
            ret_value.append(b[j])
            j += 1
        else:
            ret_value.append(a[i])
            i += 1
    return ret_value + a[i::] + b[j::]  

def merge_sort(lst):
    """
    Input: list of elements
    Output: Sorted list of elements
    >>> merge_sort([3, 7, 9, 6, 2, 5, 4, 1, 8])
    [1, 2, 3, 4, 5, 6, 7, 8, 9]

    >>> merge_sort([11, 0, 1, 5, 7, 2])
    [0, 1, 2, 5, 7, 11]

    >>> merge_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    """
    n = len(lst)

    if n<=1:
        return lst
    else:
        sub1 = merge_sort(lst[:n//2])
        sub2 = merge_sort(lst[n//2:])
        return merge(sub1,sub2)

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)