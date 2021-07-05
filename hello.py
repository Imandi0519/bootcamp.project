import hashlib
result = hashlib.md5(b"Hello world").hexdigest()
print(result)


import hashlib
test_str = "Hello world"
result = hashlib.sha256(test_str.encode())
print(result.hexdigest())


import hashlib
test_str = "Hello world"
result = hashlib.sha512(test_str.encode())
print(result.hexdigest())


import hashlib
test_str = "Hello world"
result = hashlib.sha224(test_str.encode())
print(result.hexdigest())


import hashlib
result = hashlib.md5(b"Welcome").hexdigest()
print(result)


import hashlib
test_str = "Welcome"
result = hashlib.sha384(test_str.encode())
print(result.hexdigest())


import hashlib
test_str = "Welcome"
result = hashlib.sha512(test_str.encode())
print(result.hexdigest())


import hashlib
test_str = "Welcome"
result = hashlib.sha224(test_str.encode())
print(result.hexdigest())


import hashlib
result = hashlib.md5(b"Python programming").hexdigest()
print(result)


import hashlib
test_str = "Python programming"
result = hashlib.sha256(test_str.encode())
print(result.hexdigest())


import hashlib
test_str = "Python programming"
result = hashlib.sha1(test_str.encode())
print(result.hexdigest())


import hashlib
test_str = "Python programming"
result = hashlib.sha224(test_str.encode())
print(result.hexdigest())


import hashlib
result = hashlib.md5(b"This is my first Python program").hexdigest()
print(result)


import hashlib
test_str = "This is my first Python program"
result = hashlib.sha384(test_str.encode())
print(result.hexdigest())


import hashlib
test_str = "This is my first Python program"
result = hashlib.sha512(test_str.encode())
print(result.hexdigest())


import hashlib
test_str = "This is my first Python program"
result = hashlib.sha1(test_str.encode())
print(result.hexdigest())

