# 🐍Python Visualization Exercises

## Sorting Visualizer

A small program that shows how different sorting algorithms work.

### Bubble Sort
On every iteration it does on a list, it compares the current element with the next and swaps their places if they are not in order.

"""python
def bubble_sort(i, max_value, list):
    if i == max_value:
        return list
    for j in range(max_value):
        if list[j]["value"] > list[j+1]["value"]:
            list[j], list[j+1] = list[j+1], list[j]
    return list
"""

### Insertion Sort
It's a bit more intuitive; in fact, if you ever tried putting a deck of cards in order, this is probably the method you used. On every iteration it does on a list, it compares the current item with the next, if they are not in order, it swaps them, and then it does the same thing fot the next item; it ends one iteration when it reaches two items that shouldn't be swaped.

"""python
def insetion_sort(i, list):

    key = list[i]
    j = i - 1
    while j >= 0 and key['value'] < list[j]['value']:
        list[j+1] = list[j]
        j -= 1
    list[j+1] = key
    return list
"""

## Matplotlib

Some exercises to get a feel of the library.

## Fitbit

A slightly more advanced exercise in da plotting.
