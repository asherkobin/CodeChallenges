# hint: recursion

def canGetExactChange(targetMoney, denominations):
  purse = targetMoney
  for i in range(len(denominations) - 1, 0, -1):
    if purse == denominations[i]:
      return True
    elif purse > denominations[i]:
      while purse >= denominations[i]:
        purse -= denominations[i]

  
  return purse == 0

def take_coin_from_purse(purse, denominations, denomination_idx):
  coin = denominations[denomination_idx]
  if coin <= purse:
    purse -= coin
  else:
    denomination_idx -= 1

  if denomination_idx < 0:
    return False

  if purse == 0:
    return True

  return take_coin_from_purse(purse, denominations, denomination_idx)

def canGetExactChange_R(targetMoney, denominations):
  denomination_idx = len(denominations) - 1
  purse = targetMoney
  
  result = take_coin_from_purse(purse, denominations, denomination_idx)

  return result


targetMoney_1 = 94
denominations_1 = [5, 10, 25, 100, 200] # 1-10000

denominations_2 = [4, 17, 29]
targetMoney_2 = 75


print(canGetExactChange(targetMoney_1, denominations_1))
print(canGetExactChange(targetMoney_2, denominations_2))

print(canGetExactChange_R(targetMoney_1, denominations_1))
print(canGetExactChange_R(targetMoney_2, denominations_2))