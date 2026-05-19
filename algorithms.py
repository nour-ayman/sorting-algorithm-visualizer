import time

# =====================================================================
# 1. BASIC ALGORITHMS 
# =====================================================================
def bubble_sort_visual(array, draw_callback, delay):
    """ Yasmeen's Task: Bubble Sort """
    n = len(array)
    for i in range(n):
        for j in range(0, n - i - 1):
            # Highlight adjacency comparison
            draw_callback(array, color_map={j: "yellow", j + 1: "red"})
            time.sleep(delay)
            
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                # Highlight swap
                draw_callback(array, color_map={j: "green", j + 1: "green"})
                time.sleep(delay)
                
    # Done: All Green
    draw_callback(array, color_map={x: "green" for x in range(len(array))})


def selection_sort_visual(array, draw_callback, delay):
    """ Yasmeen's Task: Selection Sort """
    n = len(array)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            # Yellow for current element, Red for current minimum found
            draw_callback(array, color_map={j: "yellow", min_idx: "red", i: "purple"})
            time.sleep(delay)
            
            if array[j] < array[min_idx]:
                min_idx = j
                
        # Swap the found minimum element with the first element
        array[i], array[min_idx] = array[min_idx], array[i]
        draw_callback(array, color_map={i: "green", min_idx: "green"})
        time.sleep(delay)
        
    draw_callback(array, color_map={x: "green" for x in range(len(array))})

# =====================================================================
# 2. INTERMEDIATE ALGORITHMS
# =====================================================================
def insertion_sort_visual(array, draw_callback, delay):
    """ Ibrahim's Task: Insertion Sort """
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        
        # Highlight the key element being inserted
        draw_callback(array, color_map={i: "red"})
        time.sleep(delay)
        
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            # Yellow for shifting elements
            draw_callback(array, color_map={j: "yellow", j + 1: "green"})
            time.sleep(delay)
            j -= 1
            
        array[j + 1] = key
        draw_callback(array, color_map={j + 1: "green"})
        time.sleep(delay)
        
    draw_callback(array, color_map={x: "green" for x in range(len(array))})


def merge_sort_visual(array, draw_callback, delay):
    """ Ibrahim's Task: Merge Sort (Divide & Conquer) """
    
    def _merge_sort(start, end):
        if start < end:
            mid = (start + end) // 2
            _merge_sort(start, mid)
            _merge_sort(mid + 1, end)
            merge(start, mid, end)

    def merge(start, mid, end):
        # Context range highlight (purple)
        draw_callback(array, color_map={x: "purple" for x in range(start, end + 1)})
        time.sleep(delay)
        
        p = start
        q = mid + 1
        temp_arr = []
        
        while p <= mid and q <= end:
            # Yellow for comparisons
            draw_callback(array, color_map={p: "yellow", q: "yellow", start: "purple", end: "purple"})
            time.sleep(delay)
            
            if array[p] <= array[q]:
                temp_arr.append(array[p])
                p += 1
            else:
                temp_arr.append(array[q])
                q += 1
                
        while p <= mid:
            temp_arr.append(array[p])
            p += 1
        while q <= end:
            temp_arr.append(array[q])
            q += 1
            
        # Write back to original array with visualization updates
        for i, val in enumerate(temp_arr):
            array[start + i] = val
            draw_callback(array, color_map={start + i: "green", start: "purple", end: "purple"})
            time.sleep(delay)

    _merge_sort(0, len(array) - 1)
    draw_callback(array, color_map={x: "green" for x in range(len(array))})

# =====================================================================
# 3. ADVANCED ALGORITHMS 
# =====================================================================

def quick_sort_visual(array, draw_callback, delay):
    """ Wezza's Task: Quick Sort (Divide & Conquer) """
    def _quick_sort(low, high):
        if low < high:
            pivot_idx = partition(low, high)
            _quick_sort(low, pivot_idx - 1)
            _quick_sort(pivot_idx + 1, high)

    def partition(low, high):
        pivot = array[high]
        i = low - 1
        
        for j in range(low, high):
            # Highlight tracking element (yellow), pivot (red), and boundary boundary i (purple)
            draw_callback(array, color_map={j: "yellow", high: "red", i: "purple"})
            time.sleep(delay)
            
            if array[j] < pivot:
                i += 1
                array[i], array[j] = array[j], array[i]
                draw_callback(array, color_map={i: "green", j: "yellow", high: "red"})
                time.sleep(delay)
                
        array[i + 1], array[high] = array[high], array[i + 1]
        draw_callback(array, color_map={i + 1: "green", high: "purple"})
        time.sleep(delay)
        return i + 1

    _quick_sort(0, len(array) - 1)
    # Success state: All Green
    draw_callback(array, color_map={x: "green" for x in range(len(array))})