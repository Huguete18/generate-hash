> [!NOTE]
> In the event of improper use of the provided code, I disclaim all responsibility.

> [!IMPORTANT]
> Allow me to remind you that this code is compatible with and can be utilized on both Windows and Linux operating systems.

> [!WARNING]
> This code is intended solely for pedagogical and educational purposes.

This code is a hash generator. Here’s what each part does:
import hashlib, import pyfiglet: Imports the necessary modules. hashlib is for hash generation and pyfiglet is for ASCII text generation.
ascii_banner = pyfiglet.figlet_format("Hash Generator"): Generates an ASCII text banner with the words “Hash Generator”.
def generate_hash(message, hash_type): Defines a function that takes a message and a hash type as input.
hash_object = hashlib.new(hash_type): Creates a new hash object of the specified type.
hash_object.update(message.encode()): Updates the hash object with the encoded message.
return hash_object.hexdigest(): Returns the hash of the message in hexadecimal format.
print("Algorithms available: MD5 | SHA-1 | SHA-224 | SHA-256 | SHA-384 | SHA-512"): Prints the available hash algorithms.
option = int(input("Enter the number of your option: ")): Asks the user to enter the number of the hash option they want to use.
hash_types = ["md5", "sha1", "sha224", "sha256", "sha384", "sha512"]: Defines the available hash types.
message = input("Enter the message to generate the hash: "): Asks the user to enter the message to generate the hash.
hash_type = hash_types[option - 1]: Selects the hash type based on the user’s option.
print("Hash of the message:", generate_hash(message, hash_type)): Prints the hash of the message using the generate_hash function.
