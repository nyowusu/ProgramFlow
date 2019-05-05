# write a program to append the times table to our jabberwocky poem
# in sample.txt. We want the tables from 2 to 12.
#
# The first column of numbers should be right justified.

print("Appending the times table from 2 to 12 to Sample.txt")

with open("timesTable.txt", "w") as times_table:
    print("*"*100, file=times_table)
    for n in range(2, 25):
        for i in range(1, 13):
            print("{:2} times {:>2} is {:>3}".format(i, n, i*n), file=times_table)
        print("-"*25, file=times_table)

print("Appending times table completed...")
