def findSignatureCounts(arr):
  sig_count = [0] * len(arr)
  signed_own_book = [False] * len(arr)
  num_signed = 0
  num_students = len(arr)
  
  while num_signed < num_students:
    for i in range(len(arr)):
      student_id = i + 1
      student_id_of_book = arr[i]
      
      if student_id == student_id_of_book:
        signed_own_book[student_id - 1] = True

      sig_count[student_id_of_book - 1] += 1
    
    arr = []
    
    for i in range(len(signed_own_book)):
      student_id = i + 1
      did_sign = signed_own_book[student_id - 1]
      if did_sign:
        num_signed += 1
      else:
        arr.append(student_id)
  
  return sig_count

arr = [1, 2]
arr = [2, 2]
arr = [4, 3, 2, 5, 1]
  #expected_3 = [3,2,2,3,3]

print(str(findSignatureCounts(arr)))