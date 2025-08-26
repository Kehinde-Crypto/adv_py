class ValueTooHighError(Exception):
  pass

class ValueTooSmallError(Exception):
    def __init__(self, message, value):
     self.message = message
     self.value = value

def test_value(x):
  if x > 100:
    raise ValueTooHighError('value too high')
  if x < 5:
    raise ValueError('value too low')
try:
    test_value(200)
except ValueTooHighError as e:
    print(e)
except ValueTooSmallError as e:
  print(e.message, e.value)

#try:
 #  a = 5 / 0
  # b = a - "10"
#except Exception as e:
 # print(e)
#except ZeroDivisionError as e:
#  print(e)
#except TypeError as e:
#   print(e)
#else:
#  print('every thing is fine')
# print('cleaning up: ')