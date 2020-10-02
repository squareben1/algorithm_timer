# Algorithmic Complexity Timing Function

A program to time algorithms and plot those times to a graph.

### How it Works

One integer is passed into the app - this is the maximum size of the final array. The chosen algorithm is then run on arrays of evenly increasing size, up to the size of the largest array, e.g. 4 would result in: [[1, 2], [1, 2, 3, 4]].

The increasing size of arrays allows for the increasing time taken by each algorithm to be easily plotted on a graph to identify big-O notation for each algorithm.

Example: ```python3 app.py 2000 binary_search```

In the above example:

`2000` = the size of the largest array.

`binary_search` is the name of the algorithm.

The program will run any of the algorithms listed in algorithms.py. The program will return the average of the time it takes the algorithm to run 50,000 times on each array; if it is a search algorithm it will do pass in a random number on each operation.

You can add your own algorithms to that file and run them.

### To run:

Start virtual environment in ROOT:
```source py3_env/bin/activate```

Enter into your terminal:

``` python3 app.py <size of largest array> <function_name to be timed> ```

Example:

```python3 app.py 20000 binary_search```
