import re 

def find_digit_matches(line):
  val = []
  for match in re.finditer(r'\d+', line):
    val.append((match.group(), match.start()))
  return val
  
def get_lines(Lines, idx):
  line1 = Lines[idx].removesuffix("\n")
  line2 = Lines[idx+1].removesuffix("\n")
  line3 = Lines[idx+2].removesuffix("\n")
  return (line1, line2, line3)

def get_digits(lines):
  digits = []
  for i in range(3):
    digits.append(find_digit_matches(lines[i]))
  return digits

def check_for_symbol(l_sym, r_sym, nl_sym, al_sym):
  symbols = ['@', '&', '*', '#', '$', '/', '%', '+', '=', '-']
  for symbol in symbols:
    if symbol in l_sym or symbol in r_sym or symbol in nl_sym or symbol in al_sym:
      return True
  return False

def check_neighbours(results:list, Lines_idx:int, Lines:list, lines: tuple, digits: list):
  left_symbol, right_symbol, nxt_line_symbol, abv_line_symbol = '', '', '', ''
  
  # handling first line
  if Lines_idx == 0 and digits[0]:
    for i in range(len(digits[0])):
      flag = False
      if digits[0][i]:
        number_index = digits[0][i][1]
        end_idx  = number_index + len(digits[0][i][0])
        # get left
        if number_index:
          left_symbol = lines[0][number_index-1]
        # get right
        if end_idx < len(lines[0]):
          right_symbol = lines[0][end_idx]
        # get next line
        nxt_line_symbol = lines[1][number_index:end_idx+1]
        if number_index:
          nxt_line_symbol = lines[1][number_index-1:end_idx+1]

        flag = check_for_symbol(left_symbol, right_symbol, nxt_line_symbol, '')
        if flag:
          results.append(int(digits[0][i][0]))

  # handling last line
  if Lines_idx+2 == len(Lines)-1 and digits[2]:
    for k in range(len(digits[2])):
      flag = False
      if digits[2][k]:
        number_index = digits[2][k][1]
        end_idx  = number_index + len(digits[2][k][0])
        # get left
        if number_index:
          left_symbol = lines[2][number_index-1]
        # get right
        if end_idx < len(lines[2]):
          right_symbol = lines[2][end_idx]
        # get above line
        abv_line_symbol = lines[1][number_index:end_idx+1]
        if number_index:
          abv_line_symbol = lines[1][number_index-1:end_idx+1]

        flag = check_for_symbol(left_symbol, right_symbol, '', abv_line_symbol)
        if flag:
          results.append(int(digits[2][k][0]))

  # handling middle lines
  if digits[1]:
    for i in range(len(digits[1])):
      flag = False
      if digits[1][i]:
        number_index = digits[1][i][1]
        end_idx  = number_index + len(digits[1][i][0])
        # get left
        if number_index:
          left_symbol = lines[1][number_index-1]
        # get right
        if end_idx < len(lines[1]):
          right_symbol = lines[1][end_idx]
        # get next line
        nxt_line_symbol = lines[2][number_index:end_idx+1]
        if number_index:
          nxt_line_symbol = lines[2][number_index-1:end_idx+1]
        # get above line
        abv_line_symbol = lines[0][number_index:end_idx+1]
        if number_index:
          abv_line_symbol = lines[0][number_index-1:end_idx+1]

        flag = check_for_symbol(left_symbol, right_symbol, nxt_line_symbol, abv_line_symbol)
        if flag:
          results.append(int(digits[1][i][0]))

  return results

def day3part1(Lines):
  engine_part_nums = []
  for i in range(len(Lines)):
    if i+3 > len(Lines): break

    lines = get_lines(Lines, i) # extracts three lines from Lines
    digits = get_digits(lines) # extracts (numbers, idx) from each line. If there is no match returns []
    engine_part_nums.append(check_neighbours(engine_part_nums, i, Lines, lines, digits))
  
  engine_part_nums = [item for item in engine_part_nums if isinstance(item, int)]
  return engine_part_nums

def find_gear_ratios(gear_ratios: list, Lines_idx: int, Lines: list, lines: tuple, digits: list):
  gear = '*'
  print(f"gear_ratios: {gear_ratios}")
  print(f"Lines_idx: {Lines_idx}")
  print(f"lines: {lines}")
  print(f"digits: {digits}")
  
  # handle first line
  if Lines_idx == 0 and gear in lines[0]:
    print(f"first line: {lines[0]}")
    idx = lines[0].index(gear)
    print(f"gear_idx: {idx}")
    
    
  # handle last line
  if Lines_idx+2 == len(Lines)-1 and gear in lines[2]:
    print(f"last line: {lines[2]}")
  # handle middle lines
  

def day3part2(Lines):
  gear_ratios = []
  for i in range(len(Lines)):
    if i+3 > len(Lines): break
    lines = get_lines(Lines, i) # extracts three lines from Lines
    digits = get_digits(lines) # extracts (numbers, idx) from each line. If there is no match returns []
    gear_ratios.append(find_gear_ratios(gear_ratios, i, Lines, lines, digits))
  return gear_ratios

def solution():
  file = open("input.txt", 'r')
  Lines = file.readlines()
  # final_result = day3part1(Lines)
  final_result = day3part2(Lines)
  print(f"final_result: {final_result}")
  # print(f"final_result_sum: {sum(final_result)}")

solution()










'''
get three lines from Lines:
// new idea, pass through a string once, if number found, check for symbols in vicinity, should not have any duplicates




// old idea to look for symbols and get the digits around them, can result in duplicates, refer new idea at the top
partition each line with the symbol
len(partition[0]) = index of symbol (sym_index)

for line1 : 
  line1 : sym_index_line1 - 1 _ sym_index_line1 _ sym_index_line1 + 1
  line2 : sym_index_line1 - 1 _ sym_index_line1 _ sym_index_line1 + 1

for line2 :
  line1 : sym_index_line2 - 1 _ sym_index_line2 _ sym_index_line2 + 1
  line2 : sym_index_line2 - 1 _ sym_index_line2 _ sym_index_line2 + 1
  line3 : sym_index_line2 - 1 _ sym_index_line2 _ sym_index_line2 + 1

for line3 :
  line2 : sym_index_line3 - 1 _ sym_index_line3 _ sym_index_line3 + 1
  line3 : sym_index_line3 - 1 _ sym_index_line3 _ sym_index_line3 + 1

for symbol in symbols:
      if symbol in line1:
        line1_partitioned = line1.partition(symbol)
        print(f"found_symbol_line1: {line1_partitioned}")
        sym_index = len(line1_partitioned[0])
        print(f"symbol: {line1[sym_index]}")
      if symbol in line2:
        line2_partitioned = line2.partition(symbol)
        print(f"found_symbol_line2: {line2_partitioned}")
        sym_index = len(line2_partitioned[0])
        print(f"symbol: {line2[sym_index]}")
      if symbol in line3:
        line3_partitioned = line3.partition(symbol)
        print(f"found_symbol_line_3: {line3_partitioned}")
        sym_index = len(line3_partitioned[0])
        print(f"symbol: {line3[sym_index]}")

'''

'''
old code i tried before, while trying to wrap my head around what I needed to do
for i in range(len(Lines)):
    if i+3 > len(Lines): return
    line1 = Lines[i].removesuffix("\n")
    line2 = Lines[i+1].removesuffix("\n")
    line3 = Lines[i+2].removesuffix("\n")
    print(f"\ni: {i} \nline1: {line1}\nline2: {line2}\nline3: {line3}\n")

    digits_line1 = find_digit_matches(line1)
    digits_line2 = find_digit_matches(line2)
    digits_line3 = find_digit_matches(line3)

    engine_part_nums = []
    if digits_line1:
      number_limits_line1 = []
      for num_tuple in digits_line1:
        number_limits_line1.append(((num_tuple[1], len(num_tuple[0])+num_tuple[1])))

      if number_limits_line1:
        for num_limit in number_limits_line1:
          print(f"num_limit: {num_limit}")
          for symbol in symbols:
            if symbol in line1[num_limit[0]-1:num_limit[1]+2]:
              print(f"number: {line1[num_limit[0]:num_limit[1]]}") 
            elif symbol in line2[num_limit[0]-1:num_limit[1]+2]:
              print(f"{symbol}")


      print(f"number_limits_line1: {number_limits_line1}")
    
    if digits_line2:
      number_limits_line2 = []
      for num_tuple in digits_line2:
        number_limits_line2.append(((num_tuple[1], len(num_tuple[0])+num_tuple[1])))
      print(f"number_limits_line2: {number_limits_line2}")
    
    if digits_line3:
      number_limits_line3 = []
      for num_tuple in digits_line3:
        number_limits_line3.append(((num_tuple[1], len(num_tuple[0])+num_tuple[1])))
      print(f"number_limits_line3: {number_limits_line3}")
      
    print(f"digits_line1: {digits_line1}")
    print(f"digits_line2: {digits_line2}")
    print(f"digits_line3: {digits_line3}")
'''