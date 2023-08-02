import hashlib
from cryptography.fernet import Fernet
import fingerprintnormalization


def hash_data(data):
  sha256 = hashlib.sha256()
  sha256.update(str(data).encode('utf-8'))
  return sha256.digest()[:16]
  # Truncate to 128 bits (16 bytes)






fingerprint_image = fingerprintnormalization.normalized_image
key1 = hash_data(fingerprint_image)
print(str(key1))


'''
import hashlib

def generate_key_from_fingerprint(fingerprint_image):
  """Generates a key from a fingerprint image.

  Args:
    fingerprint_image: The fingerprint image.

  Returns:
    The generated key.
  """

  hash_digest = hashlib.sha256(fingerprint_image).digest()
  key = hash_digest[:32]
  return key

if __name__ == "__main__":
  fingerprint_image = open("fingerprint.png", "rb").read()
  key = generate_key_from_fingerprint(fingerprint_image)
  print(key)
'''