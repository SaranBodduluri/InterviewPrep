## given a list of integers find the number of pairs which differ by just one digit
## brute force: double for loop and check
## better: while loop and TWO pointers!!!
## best: hash map

def soln(numbers):
  // numbers = [1,151,241,1,9,22,351]
  actualCount = 0
  
  left = 0
  right =1
  # two pointers left and right
  # once right moves till the end; we advance left one step and get right to just beside left
  while right< len(numbers):
    count = 0
    if len(str(numbers[left])) == len(str(numbers[right])) and numbers[left] != numbers[right]:
      t1 = str(numbers[left])
      t2 = str(numbers[right])
      for k,m in zip(t1,t2):
        if k!=m
        count+=1
      if count ==1:
        actualCount+=1
    if right == len(numbers)-1:
      left+=1
      right= left+1
    else:
      right+=1
  return actualCount