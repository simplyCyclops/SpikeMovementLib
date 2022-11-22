from interpolation import *

def main():
  result = set()
  for i in linear(0.01):
    result.add(i)

  print(sorted(list(result)))

if __name__ == "__main__":
  main()