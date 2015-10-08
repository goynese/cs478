import os
import sys
import hashlib
import string
import random


def gethex(user):
	bits=32

	return hashlib.md5(user).hexdigest()[:8]

230820142214

def main():

	for j in range(65000):
		admin = hashlib.md5("admin." + str(random.uniform(100000000000, 900000000000)) ).hexdigest()[0:8:1]
		for i in range(100000):

			test1 = (''.join(random.choice(string.ascii_lowercase) for i in range(4)))

			if admin == hashlib.md5(test1).hexdigest()[0:8:1]:
				print test1


if __name__ == "__main__":
    main()