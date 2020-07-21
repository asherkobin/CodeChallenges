def findPositions(arr, x):
  for i in range(len(arr)):
    arr[i] = (arr[i], i)

  queue = arr
  popped_items = []
  largest_value_item_idx = -1
  num_times_to_run = x
  result = []

  while num_times_to_run > 0:
    num_to_pop = x
    # step 1 - pop x from queue
    if num_to_pop > len(queue):
      num_to_pop = len(queue)
    
    while num_to_pop > 0:
      popped_items.append(queue.pop(0))
      num_to_pop -= 1

    # step 2 - remove largest item from popped_items

    for i in range(len(popped_items)):
      if largest_value_item_idx == -1:
        largest_value_item_idx = i
      elif popped_items[i][0] > popped_items[largest_value_item_idx][0]:
        largest_value_item_idx = i

    result.append(popped_items[largest_value_item_idx][1] + 1)
    popped_items.remove(popped_items[largest_value_item_idx])
    

    # step 3 - decement value of popped items, then push back to the queue
    for i in range(len(popped_items)):
      if popped_items[i][0] > 0:
        popped_items[i] = (popped_items[i][0] - 1, popped_items[i][1])
      queue.append(popped_items[i])

    popped_items = []
    largest_value_item_idx = -1
    num_times_to_run -= 1
  
  return result
  


arr = [1, 2, 2, 3, 4, 5]
x = 5

x_2 = 4
arr_2 = [2, 4, 2, 4, 3, 1, 2, 2, 3, 4, 3, 4, 4]

print(arr)
#print([5, 6, 4, 1, 2])
print([2, 5, 10, 13])
print(findPositions(arr_2, x_2))

