# AES
Fingerprint based AES encryption tool using Python 3.7

This tool gets the fingerprint data normalizes the image using cv2 package by applying guassian blur and thresholding
The hash function sha256 is applied on the fingerprint data and a hexadecimal value is obtained.
The hashed data is truncated to 128 bits and is used as the key for AES Encryption.

