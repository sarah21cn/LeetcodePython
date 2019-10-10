
import sys

def strToInt(s):
  s = s.strip()
  if not s: return 0
  index = 0
  symbol = True
  if s[index] == '-':
    symbol = False
    index += 1
  result = 0
  while index < len(s):
    num = s[index] - '0'
    if num < 0 or num > 9:
      return 0
    result = result * 10 + num
    if result > sys.max:
      return sys.max
    index += 1
  if not symbol:
    result = 0 - result
  return result

print(strToInt("123"))
    