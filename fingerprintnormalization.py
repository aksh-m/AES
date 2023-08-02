import cv2
import os
def normalize_fingerprint_image(image):
  """Normalizes a fingerprint image.
  """
 # Convert the image to grayscale.
  grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  # Apply a Gaussian blur to the image.
  blurred_image = cv2.GaussianBlur(grayscale_image, (5, 5), 0)
  # Apply thresholding to the image.
  thresholded_image = cv2.threshold(blurred_image, 127, 255, cv2.THRESH_BINARY)[1]
  # Return the normalized fingerprint image.
  return thresholded_image
def store_image(image, filename):
    """Stores an image in a file."""
    file_path = os.path.join(".", filename)
    # Save the image to the file.
    cv2.imwrite(file_path, image)

  # Load the fingerprint image.
image = cv2.imread("fingerprint.png")

  # Normalize the fingerprint image.
normalized_image = normalize_fingerprint_image(image)
store_image(normalized_image, "stored_image.jpg")
  # Display the normalized fingerprint image.
