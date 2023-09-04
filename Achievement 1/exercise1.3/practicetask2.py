''' 
1. Make a list of the following test scores 
and call it `test_scores`: 45, 23, 89, 78, 98, 55, 74, 87, 95, 75.
2. Sort `test_scores` in descending order with the `sort()` method for lists, 
using `reverse=True` as a parameter.
3. Just as you did in the previous example, 
print only the first three scores from this reverse sorted list.

'''

test_scores = [45, 23, 89, 78, 98, 55, 74, 87, 95, 75]

test_scores.sort(reverse=True)

for i in range(0,3):
    print(test_scores[i])
