import os
import shutil
import random
from shutil import copyfile
# Define root directory
root_dir = 'CatsvsDogs'

# Empty directory to prevent FileExistsError is the function is run several times
if os.path.exists(root_dir):
  shutil.rmtree(root_dir)

 
def create_train_val_dirs(root_path):
  """
  Creates directories for the train and test sets

  Args:
    root_path (string) - the base directory path to create subdirectories from

  Returns:
    None
  """
 
  train_path = os.path.join(root_path, 'training')
  test_path = os.path.join(root_path, 'validation')

  train_cats_path = os.path.join(train_path, 'cats')
  train_dogs_path = os.path.join(train_path, 'dogs')

  test_cats_path = os.path.join(test_path, 'cats')
  test_dogs_path = os.path.join(test_path, 'dogs')

  catvdog = os.mkdir(root_path)
  train_dir = os.mkdir(train_path)
  test_dir = os.mkdir(test_path)
  train_cats = os.mkdir(train_cats_path)
  train_dogs = os.mkdir(train_dogs_path)
  test_cats = os.mkdir(test_cats_path)
  test_dogs = os.mkdir(test_dogs_path)
  

  pass


  


try:
  create_train_val_dirs(root_path=root_dir)
except FileExistsError:
  print("You should not be seeing this since the upper directory is removed beforehand")


for rootdir, dirs, files in os.walk(root_dir):
    for subdir in dirs:
        print(os.path.join(rootdir, subdir))



def split_data(SOURCE_DIR, TRAINING_DIR, VALIDATION_DIR, SPLIT_SIZE):
  

  total_images = len(os.listdir(SOURCE_DIR))
  training_images_size = int(total_images * SPLIT_SIZE)

  training_imgs = random.sample(os.listdir(SOURCE_DIR), training_images_size)

  for image in training_imgs:
    if os.path.getsize(os.path.join(SOURCE_DIR, image)) > 0:
      copyfile(SOURCE_DIR + image, TRAINING_DIR + image)
    else:
      print(f"{image} is zero length, so ignoring.")

  test_imgs = list(set(os.listdir(SOURCE_DIR)) - set(training_imgs))

  for image in test_imgs:
    if os.path.getsize(os.path.join(SOURCE_DIR, image)) > 0:
      copyfile(SOURCE_DIR + image, VALIDATION_DIR + image)
    else:
      print(f"{image} is zero length, so ignoring.")


  pass

  # grader-required-cell

# Test your split_data function

# Define paths
CAT_SOURCE_DIR = "PetImages/Cat/"
DOG_SOURCE_DIR = "PetImages/Dog/"

TRAINING_DIR = "CatsvsDogs/training/"
VALIDATION_DIR = "CatsvsDogs/validation/"

TRAINING_CATS_DIR = os.path.join(TRAINING_DIR, "cats/")
VALIDATION_CATS_DIR = os.path.join(VALIDATION_DIR, "cats/")

TRAINING_DOGS_DIR = os.path.join(TRAINING_DIR, "dogs/")
VALIDATION_DOGS_DIR = os.path.join(VALIDATION_DIR, "dogs/")

# Empty directories in case you run this cell multiple times
if len(os.listdir(TRAINING_CATS_DIR)) > 0:
  for file in os.scandir(TRAINING_CATS_DIR):
    os.remove(file.path)
if len(os.listdir(TRAINING_DOGS_DIR)) > 0:
  for file in os.scandir(TRAINING_DOGS_DIR):
    os.remove(file.path)
if len(os.listdir(VALIDATION_CATS_DIR)) > 0:
  for file in os.scandir(VALIDATION_CATS_DIR):
    os.remove(file.path)
if len(os.listdir(VALIDATION_DOGS_DIR)) > 0:
  for file in os.scandir(VALIDATION_DOGS_DIR):
    os.remove(file.path)

# Define proportion of images used for training
split_size = .9

# Run the function
# NOTE: Messages about zero length images should be printed out
split_data(CAT_SOURCE_DIR, TRAINING_CATS_DIR, VALIDATION_CATS_DIR, split_size)
split_data(DOG_SOURCE_DIR, TRAINING_DOGS_DIR, VALIDATION_DOGS_DIR, split_size)

# Check that the number of images matches the expected output

# Your function should perform copies rather than moving images so original directories should contain unchanged images
print(f"\n\nOriginal cat's directory has {len(os.listdir(CAT_SOURCE_DIR))} images")
print(f"Original dog's directory has {len(os.listdir(DOG_SOURCE_DIR))} images\n")

# Training and validation splits
print(f"There are {len(os.listdir(TRAINING_CATS_DIR))} images of cats for training")
print(f"There are {len(os.listdir(TRAINING_DOGS_DIR))} images of dogs for training")
print(f"There are {len(os.listdir(VALIDATION_CATS_DIR))} images of cats for validation")
print(f"There are {len(os.listdir(VALIDATION_DOGS_DIR))} images of dogs for validation")