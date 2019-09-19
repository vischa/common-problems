# O(nlogn) solution for given an integer array, find all pairs that sum up to a specific value k.

def find_index(arr,target):
  sorted_arr = sorted(arr)
  lower = 0
  upper = len(arr)-1
  sum = None
  while sum!=target:
    sum = arr[lower] + arr[upper]
    if sum<target:
      lower+=1
    if sum>target:
      upper-=1
  return [lower,upper]

input_arr =  [1, 1, 2, 3, 4]
target_val = 4
print(find_index(input_arr,target_val))
