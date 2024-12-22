import streamlit as st
import time
import random
import matplotlib.pyplot as plt

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def measure_sort_time(sort_func, arr):
    start_time = time.time()
    sort_func(arr.copy())
    end_time = time.time()
    return end_time - start_time

def main():
    st.title("NextMid Technology Sorting Comparison")

    st.write("This app compares the performance of Insertion Sort, Bubble Sort, and Selection Sort for different input sizes.")

    max_n = st.slider("Maximum number of elements", 100, 10000, 1000)
    step = st.slider("Step size", 100, 1000, 100)

    sizes = list(range(step, max_n + 1, step))
    insertion_times = []
    bubble_times = []
    selection_times = []

    progress_bar = st.progress(0)

    for i, n in enumerate(sizes):
        arr = [random.randint(1, 1000) for _ in range(n)]
        
        insertion_times.append(measure_sort_time(insertion_sort, arr))
        bubble_times.append(measure_sort_time(bubble_sort, arr))
        selection_times.append(measure_sort_time(selection_sort, arr))
        
        progress = (i + 1) / len(sizes)
        progress_bar.progress(progress)

    st.success("Sorting completed!")

    plt.figure(figsize=(10, 6))
    plt.plot(sizes, insertion_times, label="Insertion Sort")
    plt.plot(sizes, bubble_times, label="Bubble Sort")
    plt.plot(sizes, selection_times, label="Selection Sort")
    plt.xlabel("Number of elements")
    plt.ylabel("Time (seconds)")
    plt.title("Sorting Algorithm Comparison")
    plt.legend()
    st.pyplot(plt)

    

if __name__ == "__main__":
    main()
