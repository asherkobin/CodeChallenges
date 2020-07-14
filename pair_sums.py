import math

def numberOfWays(arr, k):
  # Write your code here
  def num_combinations(n, k):
    return math.factorial(n) / math.factorial(k) *  math.factorial(n - k)
  
  count_map = {}
  total_pairs = 0
  total_pairs_of_same = 0
  
  for num in arr:
    if num not in count_map:
      count_map[num] = 1
    else:
      count_map[num] += 1
      
  for num in count_map:
    needed_num = k - num
    if needed_num in count_map:
      num_times = count_map[needed_num]
      if needed_num == num:
        total_pairs_of_same = num_combinations(num_times, 2)
      else:
        total_pairs += num_times     
    
  return int(total_pairs / 2 + total_pairs_of_same)

arr = [1, 5, 3, 3, 3, 3]
#arr = [1, 2, 3, 4, 3]

print(numberOfWays(arr, 6))