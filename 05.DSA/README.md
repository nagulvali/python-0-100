# Data Structures and Algorithms (DSA)

## Data Structures
- Data Structures are ways to organize and store data in a computer so that it can be accessed and modified efficiently.
- A data structure is not only used for organizing data but also used for processing, retrieving, and storing data.
- There are different basic and advanced types of data structures.
  - Linear Data Structures
    - Static Data Structures
      - Arrays
    - Dynamic Data Structures
      - Linked Lists
      - Stacks
      - Queues
  - Non-Linear Data Structures
    - Trees
      - Binary Trees
      - Binary Search Trees
      - AVL Trees
      - Red-Black Trees
      - B-Trees
    - Graphs
      - Directed Graphs
      - Undirected Graphs

### Arrays
- An array is a collection of items stored at contiguous memory locations.
- So, if we initialize an array, the elements will be allocated sequentially in memory. This allows for efficient access and manipulation of elements.
- Arrays can be classified in two ways
  - On the basis of Size
    - Static Arrays: Fixed size, allocated at compile time.
    - Dynamic Arrays: Size can change during runtime, allocated at runtime.
  - On the basis of Dimensions
    - One-Dimensional Arrays: A single row or column of elements.
    - Multi-Dimensional Arrays: Arrays with more than one dimension, such as 2D arrays (matrices).

#### Fixed Size Arrays
- We cannot alter or update the size of this array.
- Here only a fixed size (i,e. the size that is mentioned in square brackets []) of memory will be allocated for storage.
- In case, we don't know the size of the array then if we declare a larger size and store a lesser number of elements will result in a wastage of memory.
- or we declare a lesser size than the number of elements then we won't get enough memory to store all the elements. In such cases, static memory allocation is not preferred.
```Java
// Fixed sized array examples
int[] arr1 = new int [5];

// Another way (Array creation and 
// initialization both)
int[] arr2 = {1, 2, 3, 4, 5};
```
```python
# Create a fixed-size list of length 5, 
# initialized with zeros
arr = [0] * 5

# Output the fixed-size list
print(arr)
```

#### Dynamic Arrays
- The size of the array changes as per user requirements during execution of code so we do not have to worry about sizes.
- 
# TBA






## Algorithms
- An algorithm is a step-by-step procedure or formula for solving a problem.
- Algorithms are used to manipulate data structures.
- Algorithms are essential for solving complex computational problems efficiently and effectively. The provide a systematic approach to.
  - Solving problems: Algorithms break down problems into smaller, manageable steps.
  - Optimizing solutions: Algos find the best or near-optimal solutions to problems.
  - Automating tasks: Algorithms can automate repetitive or complex tasks, saving time and effort.

- Algorithms can be classified into different categories based on their design and application.
- Some common types of algorithms include:
  - Sorting Algorithms
    - Bubble Sort
    - Selection Sort
    - Insertion Sort
    - Merge Sort
    - Quick Sort
  - Searching Algorithms
    - Linear Search
    - Binary Search
  - Graph Algorithms
    - Dijkstra's Algorithm
    - Kruskal's Algorithm
    - Prim's Algorithm
  - Dynamic Programming Algorithms
  - Greedy Algorithms