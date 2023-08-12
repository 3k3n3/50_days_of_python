"""
Write a function called Python_snakes that takes a number
as an argument and creates the following shape, using the 
number’s range: (hint: Use the loops and emoji library. If you 
pass 7 as argument, your code should print the following:
     ⠦
    ⠦ ⠦
   ⠦ ⠦ ⠦
  ⠦ ⠦ ⠦ ⠦
 ⠦ ⠦ ⠦ ⠦ ⠦
⠦ ⠦ ⠦ ⠦ ⠦ ⠦
"""
import emoji


def python_snakes(num: int):
    snakes = []
    for x in range(1, num):
        line = (emoji.emojize(":snake:") * x).rjust(num - 1)
        snakes.append(line)

    return "\n".join(snakes)


print(python_snakes(7))
