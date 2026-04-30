import os

size = int(input("Enter file size (MB): "))
filename = os.path.join(os.getcwd(), "tiki.txt")

target = size * 1024 * 1024

with open(filename, "wb") as f:
    chunk = b"A" * 1024 * 1024
    for _ in range(size):
        f.write(chunk)

print(f"{filename} generated (~{size} MB)")