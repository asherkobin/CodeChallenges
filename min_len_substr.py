def min_length_substring(s, t):
  # Write your code here
  substrings = []
  for i in range(len(s)):
    bucket = list(t)
    if s[i] in bucket:
      bucket.remove(s[i])
      for j in range(i + 1, len(s)):
        if s[j] in bucket:
          bucket.remove(s[j])
          if len(bucket) == 0:
            substrings.append(s[i:j+1])
            break
  
  print(substrings)

  shortest = 0
  for subs in substrings:
    if len(subs) < shortest or shortest == 0:
      shortest = len(subs)
  
  if shortest == 0:
    return -1
  else:
    return shortest

# 5
s1 = "dcbefebce"
t1 = "fd"

# -1
s2 = "bfbeadbcbcbfeaaeefcddcccbbbfaaafdbebedddf"
t2 = "cbccfafebccdccebdd"

# 4
s3 = "gtagfhyhlatwet"
t3 = "hat"

print(min_length_substring(s3, t3))
