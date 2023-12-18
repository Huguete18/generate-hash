import hashlib
import pyfiglet

ascii_banner = pyfiglet.figlet_format("Hash Generator")
print(ascii_banner)

def generate_hash(message, hash_type):
    hash_object = hashlib.new(hash_type)
    hash_object.update(message.encode())
    return hash_object.hexdigest()

print("Algorithms available: MD5 | SHA-1 | SHA-224 | SHA-256 | SHA-384 | SHA-512")
print("Choose the type of hash you want:")
print("1. MD5")
print("2. SHA-1")
print("3. SHA-224")
print("4. SHA-256")
print("5. SHA-384")
print("6. SHA-512")

option = int(input("Enter the number of your option: "))
hash_types = ["md5", "sha1", "sha224", "sha256", "sha384", "sha512"]

message = input("Enter the message to generate the hash: ")
hash_type = hash_types[option - 1]

print("Hash of the message:", generate_hash(message, hash_type))

