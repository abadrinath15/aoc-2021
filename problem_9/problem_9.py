import numpy as np
from typing import Sequence
from collections import deque
import heapq
from math import prod


def is_basin(arr, x: int, ind: Sequence[int]) -> bool:
    above, below, left, right = None, None, None, None
    if ind[0] == 0:
        above = np.inf
    elif ind[0] == np.shape(arr)[0] - 1:
        below = np.inf
    if ind[1] == 0:
        left = np.inf
    if ind[1] == np.shape(arr)[1] - 1:
        right = np.inf
    above = above if above is not None else arr[ind[0] - 1, ind[1]]
    below = below if below is not None else arr[ind[0] + 1, ind[1]]
    left = left if left is not None else arr[ind[0], ind[1] - 1]
    right = right if right is not None else arr[ind[0], ind[1] + 1]
    if x == min(x, above, below, left, right) and x not in [
        above,
        below,
        left,
        right,
    ]:
        return True
    return False


def part_1(filename: str) -> None:
    with open(filename) as fp:
        count = 0
        arr = np.loadtxt((x.replace("", " ") for x in fp)).astype(int)
        it = np.nditer(arr, flags=["multi_index"])
        for x in it:
            ind = it.multi_index
            above, below, left, right = None, None, None, None
            if ind[0] == 0:
                above = np.inf
            elif ind[0] == np.shape(arr)[0] - 1:
                below = np.inf
            if ind[1] == 0:
                left = np.inf
            if ind[1] == np.shape(arr)[1] - 1:
                right = np.inf
            above = above if above is not None else arr[ind[0] - 1, ind[1]]
            below = below if below is not None else arr[ind[0] + 1, ind[1]]
            left = left if left is not None else arr[ind[0], ind[1] - 1]
            right = right if right is not None else arr[ind[0], ind[1] + 1]
            if x == min(x, above, below, left, right) and x not in [
                above,
                below,
                left,
                right,
            ]:
                count += x + 1

    print(count)


def get_basin_size(arr, ind) -> int:
    queue = deque([ind])
    seen = set()
    while len(queue) > 0:
        curr_ind = queue.popleft()
        seen.add(curr_ind)
        x, y = curr_ind
        curr_val = arr[curr_ind]
        if x != 0:
            top_ind = x - 1, y
            top_val = arr[top_ind]
            if top_val > curr_val and top_val != 9:
                queue.append(top_ind)
        if x != arr.shape[0] - 1:
            bottom_ind = x + 1, y
            bottom_val = arr[bottom_ind]
            if bottom_val > curr_val and bottom_val != 9:
                queue.append(bottom_ind)
        if y != 0:
            left_ind = x, y - 1
            left_val = arr[left_ind]
            if left_val > curr_val and left_val != 9:
                queue.append(left_ind)
        if y != arr.shape[1] - 1:
            right_ind = x, y + 1
            right_val = arr[right_ind]
            if right_val > curr_val and right_val != 9:
                queue.append(right_ind)

    return -1 * len(seen)


def part_2(filename):
    with open(filename) as fp:
        arr = np.loadtxt((x.replace("", " ") for x in fp))
        it = np.nditer(arr, flags=["multi_index"])
        size_heap = []
        for x in it:
            ind = it.multi_index
            if is_basin(arr, x, ind):
                heapq.heappush(size_heap, get_basin_size(arr, ind))

    print(abs(prod(heapq.nsmallest(3, size_heap))))


def main():
    part_1("problem_9/input.txt")
    part_2("problem_9/input.txt")


if __name__ == "__main__":
    main()
