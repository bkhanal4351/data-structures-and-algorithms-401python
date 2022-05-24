# lst = [2,1,3,5,4]

def insertion_sort(lst):
  for i in range(1, len(lst)):
    value = lst[i]
    #first iteration
    #i =1
    #value =1
    j = i-1
    #j=0

    #[2,1,3,5,4]
    #list[j] = 2
    # value = 1

    while j>=0 and value < lst[j]:
      lst[j+1] = lst[j] # list[1] = list[0]
      #[2,2,3,5,4]
      j -= 1 # j = -1
    lst[j+1] = value # j here becomes -1+1 = 0 and the value is 1
    #[1,2,3,5,4]

  return lst







