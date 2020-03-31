import sys
from validator import Validator

cli_argument_list = sys.argv
source_filename = cli_argument_list[1]
no_of_allies = 0

with open(source_filename) as source:
    result = "SPACE "
    for line in source:
        content_in_line = line.strip().split(' ')

        if len(content_in_line) == 2:
            [ kingdom, message ] = content_in_line

            validator = Validator(kingdom, message)
            if validator.process():
                no_of_allies = no_of_allies + 1
                result = result + f"{kingdom} "

    if no_of_allies >= 3:
        print(result)
    else:
        print("NONE")
