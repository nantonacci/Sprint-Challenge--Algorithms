#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) It is O(n) because we are already assigning a to n * n and there's only one more multiple after that


b) It is O(n^2) because we have entered two for loops that are both n based


c) It is O(n) because it goes down by 1 every time so it will reach n in the same number of runs

## Exercise II
Using a binary search tree

The first drop will be at the halfway point of the building height n //2

If the egg breaks, we insert {f: false} to the right of the tree, f being the floor and false being survival of the egg. Then we run again from floor f // 2

If the egg does not break, we insert {f: true} to the left of the tree, f being the floor and true being survival of the egg. Then we run from (n + f) // 2 the halfway point between middle and top

Repeat until this process until the BST's get_max ( on condition that the egg survived ) returns true and also the BST's contains method returns true for a value 1 higher than the max.

