# import hashlib
# a='hello'
# hash_object = hashlib.sha256(b'Hello World')
# hex_dig = hash_object.hexdigest()
# print(hex_dig)
# print(hashlib.sha256)
# print(hashlib.algorithms_guaranteed)

import hashlib
mystring = input('Enter String to hash: ')
mystring1 = input('Enter String to hash: ')
# Assumes the default UTF-8
hash_object = hashlib.md5(mystring.encode())
print(hash_object.hexdigest())

