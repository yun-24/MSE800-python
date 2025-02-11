"""
Make this a function:
Input values: num_for_loops, lines, filename
Output value: num_while_loops
(NB: "Output" doesn't mean "stuff we print")
"""


def main():
    """
    Main function. Read file. Count required attributes
    :return:
    """

    filename = input("Enter program filename: ")
    count_in_file(filename)


"""
count loops in file
"""


def count_in_file(filename):
    lines = open(filename).readlines()

    num_for_loops = count_loops(lines, "for")
    print("Program {} contain {} for loops".format(filename, num_for_loops))

    num_while_loops = count_loops(lines, "while")
    print("Program {} contain {} for loops".format(filename, num_while_loops))

    num_if_loops = count_loops(lines, "if")
    print("Program {} contain {} for loops".format(filename, num_if_loops))


"""
count loops in lines

param: lines
param: label
"""


def count_loops(lines, label):
    num_loops = 0
    for line in lines:
        if line.strip().startswith(label):
            num_loops += 1
    return num_loops;


if __name__ == "__main__":
    main()
