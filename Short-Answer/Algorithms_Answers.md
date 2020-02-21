#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) This function will be )(n):
I'm saying O(n) because for each iteration of a = a + n _ n you will just be adding n + n to a. if n is 10 you will get 0 < 1000(10 _ 10 \* 10), then you'll set a to 100 and then continue to add 100 to it over 10 iterations.

    Your "if" statement is never changing but since you're adding a everytime you're going to slowly iterater up to it n times.

b) This function is O(n^2) because you will be running your second while loop for every instance of i in the first for how ever many n's there are and you will be iterating 1/2 as much in the second loop because of j \*= 2 but since you're having to run the second loop for EVERY n, it's still going to be n squared.

c) This function will also be o(n). While it is a recursive function it will only run n times since we are decrementing the input with each exacution.

## Exercise II

For this problem I would start by declaring that if f - 1 == not broken and f == broken return steps.

The way that I would go about finding f would be by taking n, dividing it in half then checking to see if the egg breaks on n/2. If the egg doesn't break I would take the "left" side of the list and divide it in half again, running the same tests doing this until I have 1 value left that matches my base case.

This function would be a O(log(n)) because we are slowly narrowing down our options until we reach the correct choice.
