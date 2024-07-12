file = open("day1.txt", 'r')
Lines = file.readlines()
named_digits = {
  "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
  "six": 6, "seven": 7, "eight": 8, "nine": 9
}

def find_first_digit(line):
  for i in range(len(line)):
    if line[i].isdigit():
      first_digit = int(line[i])
      return (first_digit, i)
  return (-1, -1)

def find_last_digit(line):
  last_digit = 0
  for i in range(len(line)):
    if line[i].isdigit():
      (last_digit, j)  = (int(line[i]), i)
  if last_digit == 0: 
    return (-1, -1)
  return (last_digit, j)

def find_first_named_digit(line : str):
  value = 0
  if len(line) < 3: return (-1, -1)
  for i in range(len(line)):
    for key in list(named_digits.keys()):
      if key in line[i:i+5]:
        value = named_digits[key]
        return (value, line.index(str(key), i))
  if value == 0: return (-1, -1)

def find_last_named_digit(line : str):
  value = 0
  if len(line) < 3: return (-1, -1)
  for i in range(len(line)):
    for key in list(named_digits.keys()):
      if key in line[i:i+5]:
        value = named_digits[key]
    
  if value == 0: return (-1, -1)
  for key, value_dict in named_digits.items():
    if value_dict == value:
      key_from_value = key
  return (value, line.rfind(key_from_value))

def find_digit(line, sum: int):
  first_digit_tuple = find_first_digit(line)
  first_named_digit_tuple = find_first_named_digit(line)
  last_digit_tuple = find_last_digit(line)
  last_named_digit_tuple = find_last_named_digit(line)

  list = [first_named_digit_tuple, first_digit_tuple, last_named_digit_tuple, last_digit_tuple]

  if first_digit_tuple[1] == -1:
    first_val = first_named_digit_tuple[0]
  if first_named_digit_tuple[1] == -1:
    first_val = first_digit_tuple[0]
  
  if last_digit_tuple[1] == -1:
    last_val = last_named_digit_tuple[0]
  if last_named_digit_tuple[1] == -1:
    last_val = last_digit_tuple[0]

  if first_digit_tuple[1] > -1 and first_named_digit_tuple[1] > -1:
    min_index, min_value = min(enumerate(list), key = lambda n: n[1][1])
    first_val = min_value[0]

    max_index, max_value = max(enumerate(list), key = lambda n: n[1][1])
    last_val = max_value[0]
    
  sum += int((int(first_val) * 10)) + int(last_val)
  print(f"sum: {sum}")
  return sum

def solution():
  result = 0
  for line in Lines:
    line = line.strip()
    result = find_digit(line, result)
  print(f"result: {result}")

solution()