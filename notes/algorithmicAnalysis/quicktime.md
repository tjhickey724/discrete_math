# Average case analysis of Quicktime

The quicksort algorithm is a divide and conquer algorithm which sorts a list of size n as follows:
* pick a random member p of the list, called the pivot
* split the list L in two parts L0 and L1 where L0 is everything less than the pivot and L1 is the rest
  this step take time n as you have to go through the entire list L of length n and move each element to L0 or L1
* call quicksort on L0 and L1 to get S0 and S1
* return the list S0 + [p] + S1, which is a sorted list.

In the worst case, the pivot could be the first element and so the time would be n + n-1 + n-2 + ... + 1 = n(n+1)/2

We want to find the average case which will be O(nlog(n))
