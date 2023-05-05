import os
import shutil
from sklearn.model_selection import train_test_split

# define directory paths
root_dir = "/Users/gimsubin/Desktop/2023/2023-1/real_capstone/capstone-2023-31/data/dataset/face_dataset"
train_dir = os.path.join(root_dir,"train")
test_dir = os.path.join(root_dir,"test")


# loop over each class
dirlist=["heart","oblong","oval","round","square"]
# create training and test directories
if not os.path.exists(train_dir):
    os.makedirs(train_dir)
if not os.path.exists(test_dir):
    os.makedirs(test_dir)

for cls in dirlist:
    cls_path = os.path.join(root_dir, cls)
    print(cls_path)
    if os.path.isdir(cls_path):
        # get list of image paths for the current class
        images = []
        for img_name in os.listdir(cls_path):
            if img_name.endswith(".jpg"):
                img_path = os.path.join(cls_path, img_name)
                images.append(img_path)
        print(len(images))
		# split images into train and test sets
        train_images, test_images = train_test_split(images, train_size=0.8, test_size=0.2, random_state=42)
        
        # create subdirectories for the current class in the training and test directories
        train_cls_dir = os.path.join(train_dir, cls)
        test_cls_dir = os.path.join(test_dir, cls)
        if not os.path.exists(train_cls_dir):
            os.makedirs(train_cls_dir)
        if not os.path.exists(test_cls_dir):
            os.makedirs(test_cls_dir)
        
        # copy images to the corresponding subdirectories
        for img_path in train_images:
            img_name = os.path.basename(img_path)
            new_path = os.path.join(train_cls_dir, img_name)
            shutil.copy(img_path, new_path)
        
        for img_path in test_images:
            img_name = os.path.basename(img_path)
            new_path = os.path.join(test_cls_dir, img_name)
            shutil.copy(img_path, new_path)
