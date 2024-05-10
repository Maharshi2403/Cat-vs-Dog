import os
import zipfile
import requests
import os




# URL of the file to download
url = "https://download.microsoft.com/download/3/E/1/3E1C3F21-ECDB-4869-8368-6DEBA77B919F/kagglecatsanddogs_5340.zip"

# Local path where the file will be saved

local_file_path = "cats-and-dogs.zip"

# Download the file
response = requests.get(url, allow_redirects=True)
with open(local_file_path, 'wb') as file:
    file.write(response.content)

# Check if the file was downloaded successfully
if os.path.exists(local_file_path):
    print("File downloaded successfully.")
else:
    print("Failed to download the file.")

local_zip = 'cats-and-dogs.zip'
zip_ref = zipfile.ZipFile(local_zip, 'r')
zip_ref.extractall()
zip_ref.close()


source_path = 'PetImages'

source_path_dogs = os.path.join(source_path, 'Dog')
source_path_cats = os.path.join(source_path, 'Cat')

# Deletes all non-image files (there are two .db files bundled into the dataset)
import os

source_path_dogs = source_path + "\Dog"
source_path_cats = source_path + "\Cat"

for root, dirs, files in os.walk(source_path_dogs):
    for file in files:
        if file.endswith(".jpg") == False:
            file_path = os.path.join(root, file)
            os.remove(file_path)
            print(f"Deleted: {file_path}")

for root, dirs, files in os.walk(source_path_cats):
    for file in files:
        if file.endswith(".jpg") == False:
            file_path = os.path.join(root, file)
            os.remove(file_path)
            print(f"Deleted: {file_path}")

# os.listdir returns a list containing all files under the given path
print(f"There are {len(os.listdir(source_path_dogs))} images of dogs.")
print(f"There are {len(os.listdir(source_path_cats))} images of cats.")