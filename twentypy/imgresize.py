# project: image resizer
# created: 12/15/2023

from PIL import Image

def resize_image(size1, size2):

  # opens image
  image = Image.open("")

  # prints current image's dimensions
  print(f"Current size: {image.size}")

  # resizes image w/ parameters and saves it
  resized_image = image.resize((size1, size2))
  resized_image.save("")

  # prints new image's dimensions
  print(f"New size: {resized_image.size}")

# asks for new width and height
size1 = int(input("Enter width: "))
size2 = int(input("Enter height: "))

if __name__ == "__main__":
  resize_image((size1), (size2))