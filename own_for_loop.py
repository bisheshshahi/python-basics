#Creating my own for loop

def create_loop(iterable):
  iterator = iter(iterable)

  while True:
    try:
      print(next(iterator))
    except StopIteration:
      break

a = [1,2,3,4,5]
create_loop(a)