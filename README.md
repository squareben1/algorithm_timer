# Algorithmic Complexity Timing Function

A program to time algorithms and plot those times to a graph.

### How it Works

Two integers are passed into the app - the first is the number of total arrays, the second is the size of the largest array. Each array increases in size evenly up to the largest array, e.g. 2 4 would result in: [[1, 2], [1, 2, 3, 4]]. 

The increasing size of arrays allows for the increasing time taken by each algorithm to be easily plotted on a graph to identify big-O notation for each algorithm.

Example: ```python3 app.py 20 2000 binary_search```

In the above example: 

`20` = the number of arrays.

`2000` = the size of the largest array. 

The program will run any of the algorithms listed in algorithms.py. The program will return the average of the time it takes the algorithm to run 50,000 times on each array; if it is a search algorithm it will do pass in a random number on each operation. 

You can add your own algorithms to that file and run them. 

### To run:

Start virtual environment in ROOT:
```source py3_env/bin/activate```

Enter into your terminal: 

``` python3 app.py <no# of arrays> <size of largest array> <function_name to be timed> ```

Example:

```python3 app.py 20 20000 binary_search```


