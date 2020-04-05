# SHA-256

import hashlib
 
string = input()
sha = hashlib.sha256(string.encode())
print(sha.hexdigest())