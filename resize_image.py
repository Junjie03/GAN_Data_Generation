import os
import zipfile

def zip_directory(folder_path, zip_path):
    with zipfile.ZipFile(zip_path, mode='w') as zipf:
        len_dir_path = len(folder_path)
        for root, _, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, file_path[len_dir_path:])
                
#zip_directory(r"C:\Users\kenne\Skymind\Data Generator\resized_only_testkit", r"C:\Users\kenne\Skymind\Data Generator\resized_only_testkit.zip")
#zipfile.ZipFile('only_testkit.zip', mode='w').write(r"C:\Users\kenne\Skymind\Data Generator\only_testkit")

from PIL import Image
def resize_image(ori,dest):
    image = Image.open(ori)
    new_image = image.resize((578, 1470))
    new_image.save(dest)

    #print(image.size) # Output: (1920, 1280)
    #print(new_image.size) # Output: (400, 400)

source_dir = r"C:\Users\kenne\Skymind\DataGenerator\stylegan_output\output_w_background"
dest_dir = r"C:\Users\kenne\Skymind\DataGenerator\stylegan_output\output_w_background_resized"

for root, _, files in os.walk(source_dir):
    for file in files:
        file_path = os.path.join(root, file)
        dest_path = os.path.join(dest_dir,file)
        resize_image(file_path,dest_path)