# CBC on Modal

To solve the toy example problem a single time and also 25 times concurrently, use:

```sh
python -m modal run main.py
```

The output looks like this:

```
...

With a knapsack size of 23
We achieve an objective value of 29.0 with values
x1=1.0, x2=1.0, x3=1.0, x4=1.0
Problem description:

- Name: unknown
  Lower bound: 29.0
  Upper bound: 29.0
  Number of objectives: 1
  Number of constraints: 0
  Number of variables: 0
  Number of binary variables: 4
  Number of integer variables: 4
  Number of nonzeros: 0
  Sense: maximize

Solution description:

- Status: ok
  User time: -1.0
  System time: 0.0
  Wallclock time: 0.0
  Termination condition: optimal
  Termination message: Model was solved to optimality (subject to tolerances), and an optimal solution is available.
  Statistics: 
    Branch and bound: 
      Number of bounded subproblems: 0
      Number of created subproblems: 0
    Black box: 
      Number of iterations: 0
  Error rc: 0
  Time: 0.010016441345214844

    
Calling numerical solver
Numerical solver done!

With a knapsack size of 24
We achieve an objective value of 29.0 with values
x1=1.0, x2=1.0, x3=1.0, x4=1.0
Problem description:

- Name: unknown
  Lower bound: 29.0
  Upper bound: 29.0
  Number of objectives: 1
  Number of constraints: 0
  Number of variables: 0
  Number of binary variables: 4
  Number of integer variables: 4
  Number of nonzeros: 0
  Sense: maximize

Solution description:

- Status: ok
  User time: -1.0
  System time: 0.0
  Wallclock time: 0.0
  Termination condition: optimal
  Termination message: Model was solved to optimality (subject to tolerances), and an optimal solution is available.
  Statistics: 
    Branch and bound: 
      Number of bounded subproblems: 0
      Number of created subproblems: 0
    Black box: 
      Number of iterations: 0
  Error rc: 0
  Time: 0.010912179946899414

    
With a knapsack size of 0 We achieve an objective value of 0.0.
With a knapsack size of 1 We achieve an objective value of 0.0.
With a knapsack size of 2 We achieve an objective value of 0.0.
With a knapsack size of 3 We achieve an objective value of 4.0.
With a knapsack size of 4 We achieve an objective value of 6.0.
With a knapsack size of 5 We achieve an objective value of 8.0.
With a knapsack size of 6 We achieve an objective value of 8.0.
With a knapsack size of 7 We achieve an objective value of 11.0.
With a knapsack size of 8 We achieve an objective value of 12.0.
With a knapsack size of 9 We achieve an objective value of 14.0.
With a knapsack size of 10 We achieve an objective value of 15.0.
With a knapsack size of 11 We achieve an objective value of 17.0.
With a knapsack size of 12 We achieve an objective value of 19.0.
With a knapsack size of 13 We achieve an objective value of 19.0.
With a knapsack size of 14 We achieve an objective value of 21.0.
With a knapsack size of 15 We achieve an objective value of 23.0.
With a knapsack size of 16 We achieve an objective value of 25.0.
With a knapsack size of 17 We achieve an objective value of 25.0.
With a knapsack size of 18 We achieve an objective value of 25.0.
With a knapsack size of 19 We achieve an objective value of 29.0.
With a knapsack size of 20 We achieve an objective value of 29.0.
With a knapsack size of 21 We achieve an objective value of 29.0.
With a knapsack size of 22 We achieve an objective value of 29.0.
With a knapsack size of 23 We achieve an objective value of 29.0.
With a knapsack size of 24 We achieve an objective value of 29.0.
```