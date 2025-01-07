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
              
