# project: binary search
# created: 12/10/2023

def binary_search(list, element):
  # initializes indices and steps
  middle = 0
  start = 0
  end = len(list)
  steps = 0
  
  # loops until the element is found
  while (start <= end):
    print("Step", steps, ":", str(list[start:end+1]))
    # finds the middle index
    steps = steps + 1
    middle = (start + end) // 2
    # checks if the middle index is the element
    if element == list[middle]:
      return middle
    if element < list[middle]:
      end = middle - 1
    else:
      start = middle + 1
      
  return -1

my_list = []
target = 0

binary_search(my_list, target)
