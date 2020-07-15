def encrypt(s):
  length = len(s)

  if length == 1:
    return s
  elif length == 0:
    return ""

  mpc = None
  left = None
  right = None

  if length % 2 == 0:
    mp = (length // 2) - 1
    mpc = s[mp]
    left = s[0:mp]
    right = s[mp+1:]
  else:
    mp = length // 2
    mpc = s[mp]
    left = s[0:mp]
    right = s[mp+1:]

  return mpc + encrypt(left) + encrypt(right)

def findEncryptedWord(s):
  result = encrypt(s)

  return result



src1 = "abcxcba"
out1 = "xbacbca"

src2 = "bacd"
out2 = "abcd"

print(src1)
print(findEncryptedWord(src1))
print(out1)
print("---------")
print(src2)
print(findEncryptedWord(src2))
print(out2)