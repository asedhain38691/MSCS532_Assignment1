def insertion_sort(array):
    for i in range(1, len(array)):
        item = array[i]
        j = i - 1

        while j >= 0 and array[j] > item:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = item

    return array


if __name__ == "__main__":
    test1 = [2, 8, 5, 3, 9, 4]
    print(f"Before sorting: {test1}")
    sorted_test1 = insertion_sort(test1)
    print(f"After sorting: {sorted_test1}")
