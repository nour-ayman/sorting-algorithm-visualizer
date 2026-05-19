import time

# ==========================================
# MEMBER 4: Quick Sort Logic (Your Main Part)
# ==========================================
def quick_sort_visual(array, draw_callback, delay):
    def _quick_sort(low, high):
        if low < high:
            pivot_idx = partition(low, high)
            _quick_sort(low, pivot_idx - 1)
            _quick_sort(pivot_idx + 1, high)

    def partition(low, high):
        pivot = array[high]
        i = low - 1
        
        for j in range(low, high):
            # Highlight current tracking element (yellow) and pivot (red)
            draw_callback(array, color_map={j: "yellow", high: "red", i: "green"})
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


# ==========================================
# PLACEHOLDERS FOR OTHER MEMBERS (To avoid crashes)
# ==========================================
def bubble_sort_visual(array, draw_callback, delay):
    n = len(array)
    for i in range(n):
        for j in range(0, n - i - 1):
            draw_callback(array, color_map={j: "yellow", j+1: "red"})
            time.sleep(delay)
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                draw_callback(array, color_map={j: "green", j+1: "green"})
                time.sleep(delay)
    draw_callback(array, color_map={x: "green" for x in range(len(array))})

def selection_sort_visual(array, draw_callback, delay):
    # Dummy placeholder for Member 2
    pass

def insertion_sort_visual(array, draw_callback, delay):
    # Dummy placeholder for Member 3
    pass

def merge_sort_visual(array, draw_callback, delay):
    # Dummy placeholder for Member 3
    pass