import time
import random
import os
import matplotlib.pyplot as plt

#====================================================================
# Fady's Task: Benchmarking Engine for Sorting Algorithms
#====================================================================

# Algorithms safy mn gher GUI callbacks 3ashan el profiling sah
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def quick_sort(arr):
    def _quick_sort(items, low, high):
        if low < high:
            p_idx = partition(items, low, high)
            _quick_sort(items, low, p_idx-1)
            _quick_sort(items, p_idx+1, high)
            
    def partition(items, low, high):
        pivot = items[high]
        i = low - 1
        for j in range(low, high):
            if items[j] < pivot:
                i += 1
                items[i], items[j] = items[j], items[i]
        items[i+1], items[high] = items[high], items[i+1]
        return i + 1
        
    _quick_sort(arr, 0, len(arr)-1)

# --- THE BENCHMARKING ENGINE ---
def run_benchmark():
    # Sizes bto3 el arrays elly han-test 3aleeha (mn 100 le 1500 element)
    sizes = [100, 300, 500, 700, 1000, 1300, 1500]
    
    # Dictionaries n-save gowaha el runtimes
    runtimes = {
        "Bubble Sort": [],
        "Selection Sort": [],
        "Insertion Sort": [],
        "Merge Sort": [],
        "Quick Sort": []
    }
    
    algos = {
        "Bubble Sort": bubble_sort,
        "Selection Sort": selection_sort,
        "Insertion Sort": insertion_sort,
        "Merge Sort": merge_sort,
        "Quick Sort": quick_sort
    }

    print("🚀 Starting Empirical Performance Analysis...")
    
    for size in sizes:
        print(f"Profiling array size: {size} elements...")
        # Generate generic random list
        original_test_list = [random.randint(1, 10000) for _ in range(size)]
        
        for name, algo_func in algos.items():
            # Khod copy 3ashan koll algo t-sort nefs el data safy
            test_copy = original_test_list.copy()
            
            start_time = time.perf_counter()
            algo_func(test_copy)
            end_time = time.perf_counter()
            
            execution_time = end_time - start_time
            runtimes[name].append(execution_time)

    # Plotting using Matplotlib
    plt.figure(figsize=(10, 6))
    plt.style.use('seaborn-v0_8-darkgrid' if 'seaborn-v0_8-darkgrid' in plt.style.available else 'default')
    
    for name, times in runtimes.items():
        plt.plot(sizes, times, marker='o', label=name, linewidth=2)
        
    plt.title("Algorithm Empirical Runtime Comparison", fontsize=14, fontweight='bold')
    plt.xlabel("Array Size ($n$)", fontsize=12)
    plt.ylabel("Execution Time (Seconds)", fontsize=12)
    plt.legend(fontsize=11)
    plt.grid(True, linestyle='--', alpha=0.6)
    
    # E3mel ensure en el output directory mtzabat
    output_dir = os.path.join("assets", "performance_charts")
    os.makedirs(output_dir, exist_ok=True)
    
    chart_path = os.path.join(output_dir, "runtime_comparison.png")
    plt.savefig(chart_path, dpi=300)
    plt.close()
    
    print(f"📊 Chart successfully generated and saved to: {chart_path}")

if __name__ == "__main__":
    run_benchmark()