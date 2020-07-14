def rotationalCipher(input, rotation_factor):
  # Write your code here
  upper_start = ord('A')
  upper_end = ord('Z')
  upper_len = 26
  lower_start = ord('a')
  lower_end = ord('z')
  lower_len = 26
  num_start = ord('0')
  num_end = ord('9')
  num_len = 10
  
  def get_next_upper(c):
    shift_count = rotation_factor % upper_len
    if c + shift_count > upper_end:
      next_upper = c + shift_count - upper_len
    else:
      next_upper = c + shift_count
    return chr(next_upper)
  
  def get_next_lower(c):
    shift_count = rotation_factor % lower_len
    if c + shift_count > lower_end:
      next_lower = c + shift_count - lower_len
    else:
      next_lower = c + shift_count
    return chr(next_lower)
  
  def get_next_num(c):
    shift_count = rotation_factor % num_len
    if c + shift_count > num_end:
      next_num = c + shift_count - num_len
    else:
      next_num = c + shift_count
    return chr(next_num)
  
  output = ""
  
  for char in input:
    char = ord(char)
    if char >= upper_start and char <= upper_end:
      output += get_next_upper(char)
    elif char >= lower_start and char <= lower_end:
      output += get_next_lower(char)
    elif char >= num_start and char <= num_end:
      output += get_next_num(char)
    else:
      output += chr(char)
    
  return output

#print(rotationalCipher("56789012", 4))
print(rotationalCipher("All-convoYs-9-be:Alert1.", 0))