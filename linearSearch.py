def linear_search(lst, target):
    """Returns the index position of the target if found, else returns -1"""

    for i in range(0, len(lst)):
        if lst[i] == target:
            return i
    return -1
    
    
def linear_search2(lst, target):
    for index, value in enumerate(lst):
        if value == target:
            return index
    return -1 
    
# javascript syntax  
# function linearSearch(array, key){
#   for(let i = 0; i < array.length; i++){
#     if(array[i] === key) {
#         return i;
#     }
#   }
#   return -1;
# }    
