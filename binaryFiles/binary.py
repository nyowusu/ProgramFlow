# # writing binary to files
#
# print("Writing binary to a file: started.")
#
# with open("binary", "bw") as bin_write_file:
#     for n in range(17):
#         bin_write_file.write(bytes([n]))
#
# print("Writing binary to a file: ended.")
#
# print("="*40)
# print("Reading binary from a file: started.")
#
# with open("binary", "br") as bin_read_file:
#     for line in bin_read_file:
#         print(line)
#         # lines = bin_read_file.readline()
#
# print("Reading binary from a file: ended.")

# =================================================
# writing the values of a variable into files and reading them back
# =================================================

a = 65534
b = 65535
c = 65536
x = 39983022

with open("variableBinary", "bw") as var_bin:
    var_bin.write(a.to_bytes(2, 'big'))
    var_bin.write(b.to_bytes(2, 'big'))
    var_bin.write(c.to_bytes(4, 'big'))
    var_bin.write(x.to_bytes(4, 'big'))
    var_bin.write(x.to_bytes(4, 'little'))

with open("variableBinary", "br") as from_var_bin:
    e = int.from_bytes(from_var_bin.read(2), "big")
    f = int.from_bytes(from_var_bin.read(2), "big")
    g = int.from_bytes(from_var_bin.read(4), "big")
    h = int.from_bytes(from_var_bin.read(4), "big")
    i = int.from_bytes(from_var_bin.read(4), "little")

print(e)
print(f)
print(g)
print(h)
print(i)
