# Sorting Algorithm Visualizer

A desktop application built in Python that visualizes various sorting algorithms in real-time. This tool helps students and developers understand the mechanics, step-by-step operations, and time complexities of basic, intermediate, and advanced sorting algorithms through dynamic graphical animations.

---

## 📂 Project Structure

```text
Project/
│
├── main.py                    # App Entry Point & Algorithm Integration
├── gui.py                     # UI Framework & Animation Rendering (Tkinter/PyQt)
├── algorithms.py              # Core Engine containing all Sorting Logic
│
├── utils/
│   └── benchmarking.py        # Performance analysis & runtime execution tracking
│
└── assets/
    └── performance_charts/    # Generated comparison plots (Matplotlib)
```

 # 📊 Supported Algorithms & Complexities

The application visualizes 5 core sorting algorithms, divided by their algorithmic complexity and paradigm:

## 1. Basic Algorithms ($O(n^2)$)
* **Bubble Sort**: A simple comparison-based algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order.
* **Selection Sort**: Divides the array into sorted and unsorted parts, repeatedly finds the minimum element from the unsorted part, and puts it at the beginning.

## 2. Intermediate Algorithms
* **Insertion Sort ($O(n^2)$)**: Builds the final sorted array one item at a time by inserting elements into their proper position relative to the already-sorted elements.
* **Merge Sort ($O(n \log n)$)**: A classic Divide and Conquer algorithm. It divides the input array into two halves, calls itself for the two halves, and then merges the two sorted halves.

## 3. Advanced Algorithms
* **Quick Sort ($O(n \log n)$)**: Another Divide and Conquer powerhouse. It picks an element as a pivot and partitions the given array around the picked pivot so that smaller elements go left and larger ones go right.

---

# 📈 Complexity Reference Table

| Algorithm | Best Case | Average Case | Worst Case | Space Complexity | Paradigm |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Bubble Sort** | $O(n)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ | Brute Force |
| **Selection Sort** | $O(n^2)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ | Brute Force |
| **Insertion Sort** | $O(n)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ | Incremental |
| **Merge Sort** | $O(n \log n)$ | $O(n \log n)$ | $O(n \log n)$ | $O(n)$ | Divide & Conquer |
| **Quick Sort** | $O(n \log n)$ | $O(n \log n)$ | $O(n^2)$ | $O(\log n)$ | Divide & Conquer |

---

# 👥 Team Roles & Task Distribution

### 🎨 Member 1: GUI & Visualization Developer
* **Role**: Building the main application interface and handling graphical rendering.
* **Tasks**:
  * Design the desktop window layout using Tkinter or PyQt.
  * Create interactive controls: Start/Pause buttons, speed control sliders, and array size selectors.
  * Implement the rendering logic to display numbers as dynamic vertical bars.
  * Handle real-time color updates (e.g., highlighting comparisons, swaps, and pivots).

### 🟢 Member 2: Basic Sorting Algorithms Developer
* **Role**: Implementing foundational sorting mechanisms.
* **Tasks**:
  * Manually code the Bubble Sort and Selection Sort algorithms inside `algorithms.py`.
  * Embed execution delays and trigger state-updates (`draw_callback`) after every key comparison or element swap.

### 🟡 Member 3: Intermediate Sorting Algorithms Developer
* **Role**: Implementing intermediate-level sorting operations.
* **Tasks**:
  * Manually code the Insertion Sort and Merge Sort algorithms inside `algorithms.py`.
  * Manage data streaming configurations to ensure the step-by-step animation supports array division and merging stages.

### 🔴 Member 4: Advanced Algorithms & Integration Lead
* **Role**: Developing advanced recursive logic and managing full-system integration.
* **Tasks**:
  * Manually code the Quick Sort algorithm with optimized pivot selection methods.
  * Implement dynamic Recursion Visualization (handling index active ranges and dimming inactive sub-arrays during partitioning).
  * Design the integration framework inside `main.py` to seamlessly connect the backend algorithm engines with the frontend GUI callbacks.

### 📊 Member 5: Performance Analysis, Testing & Documentation Lead
* **Role**: Quality assurance, empirical benchmarking, and reporting.
* **Tasks**:
  * Profile and benchmark the runtime performance of all implemented algorithms under different scenarios (Best, Average, Worst cases).
  * Generate statistical comparison tables and plot analytical runtime charts using Matplotlib.
  * Document time complexities ($O(n^2)$ vs $O(n \log n)$) and write the final technical report.