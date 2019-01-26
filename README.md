# DynamicRegression-
Dynamic Linear Regression by using on a set of points using Gradient descent. Uses both dynamic and set step size for descent.


# Program Execution:

My program asks the user to have a data.txt file with ordered pairs of coordinates.
It does a linear regression through the data points and tries to minimize that error.
The program also asks the user which method to use; one is for a fixed step size for error reduction, the other one is dynamic step size to make the program a bit more efficient. 
If you entered the fixed size, you also have the input the number of iterations you want. 

# Program Design:

The program uses the square of the vertical distance of the points from the guess as for the error and tries to reduce it. To maximize efficiency and not to guess randomly the program does gradient descent on the two variable discrete error function. 

The gradient function used in the program is an estimate and doesn’t come from the partial differentiation to make the error function more scalable. It can be scaled to arbitrarily many dimensions to make different fitting algorithms that are not just linear.

I also tried to implement a dynamic step size to reduce the error. Since gradient descent can be really slow or really fast depending on the step size, this dynamic step size relies on the fact that its a parabolic sheet function and the magnitude of the gradient only decreases as it approaches the minimum. 
The dynamic step size function tries to take a huge step on the curve as long as the gradient is decreasing and it's on the estimated curve.

The program stops when the error reducing graph has turned asymptotic and it doesn't do any more iterations after that in both fixed and dynamic step size.

The initial guess is always m = 0 and b = 0 to compare dynamic and fixed size methods with a set reference. 


# Known Bugs

Dynamic step sizes help mostly with data that are not that linear in nature and big data.
But its not always the most efficient or most accurate in all cases.

The program doesn’t work well with downward sloping datapoints. 



