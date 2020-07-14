def get_total_time(arr):
  total_time = 0
  arr.sort(reverse=True)
  
  while True:
    if len(arr) == 1:
      return total_time
    
    sum = arr[0] + arr[1]
    
    total_time += sum
    
    arr = [sum, *arr[2:]]





arr = [4, 2, 1, 3]
expected = 26
print(str(arr) + ":" + str(expected))
a = get_total_time(arr)
print(a)
