def solution():
  file = open("day2.txt", 'r')
  Lines = file.readlines()
  # cubes_in_bag = {"red": 12, "green": 13, "blue": 14}
  sum = 0

  for line in Lines:
    line = line.split(":")[1].strip() # removes 'Game No.:' and strips whitespaces
    rounds = line.split("; ") # splits a game record into its rounds as list of substrings around '; '
    red_count, blue_count, green_count = 0, 0, 0

    for single_round in rounds:
      split_round = single_round.replace(",", "").split()

      if "red" in split_round:
        red_index = split_round.index("red")
        red_value = int(split_round[red_index - 1])
        if red_value > red_count:
          red_count = red_value
      if "blue" in split_round:
        blue_index = split_round.index("blue")
        blue_value = int(split_round[blue_index - 1])
        if blue_value > blue_count:
          blue_count = blue_value
      if "green" in split_round:
        green_index = split_round.index("green")
        green_value = int(split_round[green_index - 1])
        if green_value > green_count:
          green_count = green_value

    power = red_count * blue_count * green_count
    sum += power

  print(f"final sum: {sum}\n")
    
solution()