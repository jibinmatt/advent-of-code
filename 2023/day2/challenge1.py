def solution():
  file = open("day2.txt", 'r')
  Lines = file.readlines()
  # cubes_in_bag = {"red": 12, "green": 13, "blue": 14}
  sum = 0

  for line in Lines:
    game_index = line.split()[1].split(":")[0] # gets game_index from line
    line = line.split(":")[1].strip() # removes 'Game No.:' and strips whitespaces
    rounds = line.split("; ") # splits a game record into its rounds as list of substrings around '; '
    flag = True
    
    for single_round in rounds:
      red_count, blue_count, green_count = 0, 0, 0
      split_round = single_round.replace(",", "").split()

      if "red" in split_round:
        red_index = split_round.index("red")
        red_value = int(split_round[red_index - 1])
        red_count += red_value
      if "blue" in split_round:
        blue_index = split_round.index("blue")
        blue_value = int(split_round[blue_index - 1])
        blue_count += blue_value
      if "green" in split_round:
        green_index = split_round.index("green")
        green_value = int(split_round[green_index - 1])
        green_count += green_value

      if red_count > 12 or green_count > 13 or blue_count > 14:
        flag = False

    if flag:
      sum += int(game_index)

  print(f"final sum: {sum}\n")

solution()