import hashlib

def get_hash(file_name):

    h = hashlib.sha256()

    with open(file_name, "rb") as file:

        while chunk := file.read(1024):

            h.update(chunk)

    return h.hexdigest()


file1 = get_hash("pd1.pdf")
file2 = get_hash("pd2.pdf")


if file1 == file2:
    print("Files are identical")
else:
    print("Files are different")


print("\nHash of File 1:", file1)
print("Hash of File 2:", file2)
