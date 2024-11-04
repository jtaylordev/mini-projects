# File Management System

## Concepts Covered
- Trees
- File Input/Output, Recursion, Encapsulation

### Project Overview

- **Objective**: Create a system that simulates folder and file storage using a tree structure.
- **Key Features**:
  - Each folder can contain files or other folders.
  - Ability to navigate through the folder hierarchy.
  - File I/O operations for saving and loading the file system.
- **Concepts Covered**:
  - **Trees**: To manage the folder hierarchy.
  - **Recursion**: For navigating and manipulating the tree structure.
  - **File I/O**: To persist the file system data.
  - **Encapsulation**: For managing file and folder properties securely.

### Trees

- **Definition**: A tree is a hierarchical data structure consisting of nodes connected by edges.
- **Terminology**:
  - **Node**: Represents an entity (file or folder).
  - **Root**: The top node in a tree (e.g., the root folder).
  - **Child**: A node directly connected to another node when moving away from the root.
  - **Parent**: The converse notion of a child.
  - **Leaf**: A node with no children (e.g., a file).
- **Types of Trees**:
  - **Binary Tree**: Each node has at most two children.
  - **N-ary Tree**: Each node can have any number of children (suitable for this project).
- **Applications**:
  - File systems, organizational structures, parsing expressions.

###  File I/O

- **Definition**: Operations that involve reading from and writing to files.
- **Python File I/O Basics**:
  - **Opening Files**: Using `open()` function with modes like `'r'`, `'w'`, `'a'`, `'rb'`, `'wb'`.
  - **Reading Files**: Methods like `.read()`, `.readline()`, `.readlines()`.
  - **Writing Files**: Methods like `.write()`, `.writelines()`.
  - **Closing Files**: Using `.close()` or context managers (`with` statement).
- **Serialization**:
  - **Purpose**: Convert objects to a format that can be stored or transmitted and reconstructed later.
  - **Methods**: JSON, Pickle, etc.

### Recursion

- **Definition**: A process where a function calls itself directly or indirectly.
- **Use in Trees**:
  - Traversing tree structures (e.g., pre-order, in-order, post-order traversal).
- **Key Components**:
  - **Base Case**: The condition under which the recursion ends.
  - **Recursive Case**: The function calls itself with a subset of the original problem.

### Encapsulation

- **Definition**: Bundling data (attributes) and methods that operate on the data within one unit (class), restricting access to some components.
- **Access Modifiers in Python**:
  - **Public**: Accessible from anywhere (`self.attribute`).
  - **Protected**: Suggests non-public (`self._attribute`).
  - **Private**: Name mangling to prevent access (`self.__attribute`).
- **Benefits**:
  - Data hiding, protection from unauthorized access, and control over attribute manipulation.
