import os
import shutil
import random
import time
from datetime import datetime
from PIL import Image
import piexif

# Define the source and destination folders
source_folder = '/Users/user1/Documents/slideshow'
destination_folder = '/Users/user1/Documents/slideshowrandom'

# Create the destination folder if it doesn't exist
os.makedirs(destination_folder, exist_ok=True)

# Get the list of files from the source folder
files = os.listdir(source_folder)

# Shuffle the list of files to randomize the order
random.shuffle(files)

# Current system time (as a timestamp)
current_time = time.time()

# Iterate over the shuffled list and copy each file to the destination folder
for filename in files:
    # Construct full file path
    source_file = os.path.join(source_folder, filename)
    destination_file = os.path.join(destination_folder, filename)
    
    # Copy the file from source to destination
    shutil.copy(source_file, destination_file)
    
    # Set the access and modification times to the current system time
    os.utime(destination_file, (current_time, current_time))

    # Update the capture date and time metadata for image files
    if filename.lower().endswith(('.jpg', '.jpeg', '.tiff')):
        try:
            # Open the image and get its EXIF data
            image = Image.open(destination_file)
            exif_dict = piexif.load(image.info.get('exif', b""))

            # Format the current time as a string
            date_str = datetime.fromtimestamp(current_time).strftime("%Y:%m:%d %H:%M:%S")
            encoded_date_str = date_str.encode("utf-8")

            # Update the DateTimeOriginal and DateTimeDigitized fields
            exif_dict['Exif'][piexif.ExifIFD.DateTimeOriginal] = encoded_date_str
            exif_dict['Exif'][piexif.ExifIFD.DateTimeDigitized] = encoded_date_str

            # Save the updated EXIF data back to the image
            exif_bytes = piexif.dump(exif_dict)
            image.save(destination_file, exif=exif_bytes)
            image.close()
            
            print(f"Updated EXIF for {filename} to {date_str}")

        except Exception as e:
            print(f"Failed to update EXIF for {filename}: {e}")

    # Print the file being copied for verification
    print(f"Copied {filename} to {destination_folder} with current system time")
    
    # Increment the current time by 1 second for the next file
    current_time += 1

    # Wait for 1 second before copying the next file
    time.sleep(1)
