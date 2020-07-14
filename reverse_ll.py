class Node():
  def __init__(self, value):
    self.value = value
    self.next = None

def linked_list_from_array(arr):
  head = Node(arr[0])
  cur = head
  
  for i in range(1, len(arr)):
    cur.next = Node(arr[i])
    cur = cur.next
  
  return head

def array_from_linked_list(head):
  arr = []
  cur = head

  while cur:
    arr.append(cur.value)
    cur = cur.next

  return arr

def reverse_linked_list(head):
  prev = None
  cur = head

  while cur:
    next = cur.next # save
    cur.next = prev # assign next to prev
    prev = cur
    cur = next

  return prev

array = [9, 1, 2, 3, 6, 8, 11, 5]
ll = linked_list_from_array(array)
rev_ll = reverse_linked_list(ll)
rev_array = array_from_linked_list(rev_ll)

print(array)
print(rev_array)

def reverse_linked_list_section(head, start, end):
  pass

# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# (0, 3) => [3, 2, 1, 0, 4, 5, 6, 7, 8, 9]
# (2, 4) => [0, 1, 4, 3, 2, 5, 6, 7, 8, 9]
# (6, 9) => [0, 1, 2, 3, 4, 5, 9, 8, 7, 6]

