import zlib

original_string = "hello world!hello world!hello world!hello world!"
compressed_string = zlib.compress(original_string.encode())
print("Compressed string:", compressed_string)

decompressed_string = zlib.decompress(compressed_string).decode()
print("Decompressed string:", decompressed_string)