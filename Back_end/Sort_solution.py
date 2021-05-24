import logging
import math
from utils import logging_config


def bubble_sort(Orig_Seq):
    seq = Orig_Seq.copy()
    compare_count = 0
    move_count = 0
    for i in range(len(seq)):
        for j in range(len(seq) - i - 1):
            if seq[j] > seq[j + 1]:
                seq[j + 1], seq[j] = seq[j], seq[j + 1]
                move_count += 1
            else:
                pass
            compare_count += 1
    logging.info('bubble sort: sorted seq:{}, compare_count={}, move_count={}'.format(seq, compare_count, move_count))
    return [seq, compare_count, move_count]


def quick_sort(seq_o):
    """
    : seq: 未排序的列表，例如[10, 3, 5, 6]
    : return: [seq, compare, exchange]，seq为排好序的列表[3,5,6,10]，compare为比较次数，exchange为交换次数
    """
    seq = [i for i in seq_o]
    compare = 0
    exchange = 0
    if len(seq) < 2:
        logging.info('quick sort: sorted seq:{}, compare_count={}, move_count={}'.format(seq, compare, exchange))
        return [seq, compare, exchange]
    l = 0
    r = len(seq) - 1
    stack = [l, r]
    while stack:
        low = stack.pop(0)
        high = stack.pop(0)
        if high - low <= 0:
            continue
        x = seq[high]
        i = low - 1
        for j in range(low, high):
            compare += 1
            if seq[j] <= x:
                i += 1
                if i == j:
                    continue
                exchange += 1
                seq[i], seq[j] = seq[j], seq[i]
        if i + 1 != high:
            exchange += 1
            seq[i + 1], seq[high] = seq[high], seq[i + 1]
        stack.extend([low, i, i + 2, high])
    logging.info('quick sort: sorted seq:{}, compare_count={}, move_count={}'.format(seq, compare, exchange))
    return [seq, compare, exchange]


# %% 选择排序
def select_sort(Orig_Seq):
    seq = Orig_Seq.copy()
    compare = 0
    exchange = 0
    for i in range(len(seq) - 1):
        min_index = i
        for j in range(i + 1, len(seq)):
            compare += 1
            if seq[j] < seq[min_index]:
                min_index = j
        if min_index != i:
            seq[min_index], seq[i] = seq[i], seq[min_index]
            exchange += 1
    logging.info(
        'select sort: sorted seq:{}, compare_count={}, move_count={}'.format(seq, compare, exchange))
    return [seq, compare, exchange]


def merge(a, b):
    c = []
    a_idx, b_idx = 0, 0
    compare = 0
    exchange = 0
    if isinstance(a[0], list):
        compare += a[1]
        exchange += a[2]
        a = a[0]
    if isinstance(b[0], list):
        compare += b[1]
        exchange += b[2]
        b = b[0]
    while a_idx < len(a) and b_idx < len(b):
        compare += 1
        if a[a_idx] < b[b_idx]:
            c.append(a[a_idx])
            a_idx += 1
        else:
            c.append(b[b_idx])
            b_idx += 1
            exchange += 1
    if a_idx == len(a):
        c.extend(b[b_idx:])
    else:
        c.extend(a[a_idx:])
        exchange += 1
    logging.info(
        'merge sort: sorted seq:{}, compare_count={}, move_count={}'.format(c, compare, exchange))
    return [c, compare, exchange]


# performs merge sort on the input array
def merge_sort(Orig_Seq):
    seq = Orig_Seq.copy()
    # a list of zero or one elements is sorted, by definition
    if len(seq) <= 1:
        logging.info(
            'merge sort: sorted seq:{}, compare_count={}, move_count={}'.format(seq, 0, 0))
        return seq, 0, 0
    # split the list in half and call merge sort recursively on each half
    left, right = merge_sort(seq[:int(len(seq) / 2)]), merge_sort(seq[int(len(seq) / 2):])
    # merge the now-sorted sublists
    return merge(left, right)


def insert_sort(Orig_Seq):
    # 插入排序
    seq = Orig_Seq.copy()
    compare = 0
    exchange = 0
    for i in range(1, len(seq)):
        key = seq[i]
        j = i - 1
        while j >= 0:
            compare += 1
            if seq[j] > key:
                seq[j + 1] = seq[j]
                seq[j] = key
                exchange += 1
            j -= 1
    logging.info(
        'insert sort: sorted seq:{}, compare_count={}, move_count={}'.format(seq, compare, exchange))
    return [seq, compare, exchange]


def heapify(arr, n, i, cn, num):
    largest = i
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    if l < n and arr[i] < arr[l]:
        largest = l
        cn += 1

    if r < n and arr[largest] < arr[r]:
        largest = r
        cn += 1

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # 交换
        num += 1
        cn += 1
        heapify(arr, n, largest, cn, num)
        # print(cn, num)
    # print('-', cn, num)
    return cn, num


def heap_sort(seq):
    arr = [i for i in seq]
    n = len(arr)
    exchange = 0
    compare = 0
    flag = 0

    if n <= 1:
        logging.info(
            'merge sort: sorted seq:{}, compare_count={}, move_count={}'.format(arr, compare, exchange))
        return [seq, compare, exchange]

    for i in range(0, n - 1, 1):
        if arr[i] > arr[i + 1] or arr[i] == arr[i + 1]:
            flag = -1
            break
        else:
            flag += 1
    if flag == n - 1:
        return [arr, int(n * math.log(n, 2)), 0]

    # Build a maxheap.
    for i in range(n, -1, -1):
        cpr, exc = heapify(arr, n, i, 0, 0)
        compare += cpr
        exchange += exc

        # 一个个交换元素
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # 交换
        exchange += 1
        cpr, exc = heapify(arr, i, 0, 0, 0)
        compare += cpr
        exchange += exc

    logging.info(
        'merge sort: sorted seq:{}, compare_count={}, move_count={}'.format(arr, compare, exchange))
    return [arr, compare, exchange]


if __name__ == '__main__':
    logging_config(folder='log', name='sort_solution')
    sequence = [1]
    bubble_sort(sequence)
    quick_sort(sequence)
    select_sort(sequence)
    merge_sort(sequence)
    insert_sort(sequence)
    heap_sort(sequence)
    # print(heap_sort(sequence))
    print(merge_sort(sequence))
    # print(quick_sort(sequence))
