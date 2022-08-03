sorted_list = ['Aden Rowe', 'Annalise Sullivan', 'Brooklynn Matthews', 'Cohen Walter', 'Connor Nicholson', 'Evangeline Brock', 'Graham Maynard', 'Juliana King', 'Julianne Decker', 'Kadence Sandoval', 'Susan Novak', 'Teagan Suarez']

def binary_search(list, target):
    first = 0
    last = len(list) - 1

    while first <= last:
        midpoint = (first + last)//2
        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint+1
        else:
            last = midpoint-1
    return -1
    
    



def recursive_binary_search(list, target, start=0, end=None):
    if end is None:
        end = len(list) - 1
    if start > end:
        return -1

    mid = (start + end) // 2

    if target == list[mid]:
        return mid
    else:
        if target < list[mid]:
            return recursive_binary_search(list, target, start, mid-1)
        else:
            return recursive_binary_search(list, target, mid+1, end)
            

 
# javascript Syntax 
# function binarySearch(array, key) {
#     let left = 0;
#     let right = array.length - 1;
#     while (left <= right) {
#         const mid = left + Math.floor((right - left) / 2);
#         if (array[mid] === key) {
#             return mid;
#         }
#         if (array[mid] < key) {
#             left = mid + 1;
#         } else {
#             right = mid - 1;
#         }
#     }
#     return -1;
# }

print(binary_search(sorted_list,'Susan '))


