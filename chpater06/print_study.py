print("test", "test1")
print("test", "test1", sep=", ")
print("abcd" + "efg")
print("abcd", 123, sep="")
print("%s %d" %('test', 10))

a = 0.123456789
print("{0:.2f}, {0:.5f}".format(a))

print("{0:2d}, {0:05d}, {1:>5d}, {1:<5d}, {2:.3f}, {3:,}, {2:.1%}, {3:.2e}".format(3, 12, 0.12345, 7456000))

print("{0:#x}, {0:#o}, {0:#b}, {0:x}, {0:o}, {0:b}".format(10))
