def solution(nums):
  Nums = []
  for i in nums:
    Nums.append(int(i) ** 2)  
  return sorted(Nums)