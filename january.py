# 6. Maximum Subarray
def max_subarray(nums):
  start_ptr = 0
  end_ptr = 0
  largest_sum = max(nums)
  nums_length = len(nums)
  for start_ptr in range(0, nums_length):
    for end_ptr in range(start_ptr+1, nums_length):
      new_sum = sum(nums[start_ptr:end_ptr+1])
      if new_sum > largest_sum:
        largest_sum = new_sum
  return largest_sum

# Kadane's algorithm solution
def max_subarray_kadane(nums):
    current_sum = max_sum = nums[0]
    for num in nums[1:]: # For each element, find the maximum sum among all subarrays ending at that element
        current_sum = max(num, current_sum + num) # With each new element, you can either start fresh (num) or append the new element to the contiguous subarray (current_sum + num).
        max_sum = max(max_sum, current_sum) # The maximum subarray thus far might not end at that element (it might end sooner) 
    return max_sum
             
# 7. Valid Parenthesis
# With Mia
def valid_parens(s):
  stack = []
  bracket_dict = {
    '(':')',
    '{':'}',
    '[':']'
  }

  for char in s:
    if char in bracket_dict.keys(): # Push openers onto the stack
      stack.append(char)
    elif char in bracket_dict.values():
      if not stack or char != bracket_dict.get(stack.pop()): # Check that the closers match the openers in stack order
        return False
    else:
      pass
  return not stack # Stack should be empty at the end because all openers should have closers
