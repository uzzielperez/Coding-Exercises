a = input("Enter text: ")
def split_and_join(line):
    # write your code here
    a = line.split()
    joint_a = "-".join(a)
    return joint_a

print(split_and_join(a))
