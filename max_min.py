
def max_num(a):
  max_val = a[0] 
  for check in a: 
    if check > max_val: 
      max_val = check 
  return max_val


def min_num(a):
  min_val = a[0] 
  for check in a: 
    if check < min_val: 
      min_val = check 
  return min_val
n = int(input("Enter the size of the list "))
print("\n")
my_list = list(eval(num) for num in input("Enter the list items separated by space ").strip().split())[:n]

print("Maximum of the list", max_num(my_list))
print("Minimum of the list", min_num(my_list))