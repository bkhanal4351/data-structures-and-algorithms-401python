def when_in_rome(roman):
  roman = roman.upper()
  dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
  rome_to_int = 0
  for i in range(len(roman)):
    value = dic[roman[i]]
    if i + 1 < len(roman) and dic[roman[i+1]] > value:
      rome_to_int-= value
    else:
      rome_to_int+= value
  return rome_to_int
