def merge_sort(lst):
  if len(lst) > 1:
    mid = len(lst)//2 #mid point

    #dividing list in two halves
    left = lst[:mid]
    right = lst[mid:]

    #recursion
    merge_sort(left)
    merge_sort(right)

    #merge
    i=j=k=0
    while i < len(left) and j < len(right):
      if left[i] < right[j]:
        lst[k] = left[i]
        i+=1
        k+=1

      else:
        lst[k] = right[j]
        j+=1
        k+=1

    while i < len(left):
      lst[k] = left[i]
      i+=1
      k+=1

    while j < len(right):
      lst[k] = right[j]
      j+=1
      k+=1
    return lst


'''
3,9    6,15
3 9    6  15
3  9    6   15


'''
    #merge
  # def merge(left, right, lst):
  #   i=j=k=0
  #   while i < len(left) and j < len(right):
  #     if left[i] <= right[j]:
  #       lst[k] = left[i]
  #       i+=1

  #     else:
  #       lst[k] = right[j]
  #       j +=1
  #     k+=1

  #   if i == len(left):
  #     for x in range(j, len(right)):
  #       lst[k] = right[x]
  #       k +=1
  #   else:
  #     for x in range(i, len(left)):
  #       lst[k] = left[x]
  #       k+=1




# if __name__ == '__main__':
#   nums = [3,2,7,6]
#   merge_sort(nums)
#   print(f'{nums}')
#   assert nums == [2,3,6,7]
