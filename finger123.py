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

