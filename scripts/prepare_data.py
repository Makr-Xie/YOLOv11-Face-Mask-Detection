import os
import shutil
import random

def prepare_data(labels_dir, images_dir, output_dir, train_size=0.7, test_size=0.15, val_size=0.15):
    assert train_size + test_size + val_size == 1, "Train, test, and validation sizes must sum to 1."

    all_files = [
        os.path.splitext(f)[0]
        for f in os.listdir(labels_dir)
        if f.endswith('.txt') and f != 'classes.txt'
    ]
    random.shuffle(all_files)

    total = len(all_files)
    train_end = int(total * train_size)
    test_end = train_end + int(total * test_size)

    train_files = all_files[:train_end]
    test_files = all_files[train_end:test_end]
    val_files = all_files[test_end:]

    subsets = {
        'train': train_files,
        'test': test_files,
        'val': val_files
    }

    for subset, files in subsets.items():
        subset_labels_dir = os.path.join(output_dir, subset, 'labels')
        subset_images_dir = os.path.join(output_dir, subset, 'images')
        os.makedirs(subset_labels_dir, exist_ok=True)
        os.makedirs(subset_images_dir, exist_ok=True)

        for file in files:
            src_label = os.path.join(labels_dir, f'{file}.txt')
            src_image = os.path.join(images_dir, f'{file}.png')
            dst_label = os.path.join(subset_labels_dir, f'{file}.txt')
            dst_image = os.path.join(subset_images_dir, f'{file}.png')

            shutil.copy(src_label, dst_label)
            shutil.copy(src_image, dst_image)

    print("Data splitting completed.")
    for subset in subsets:
        print(f"{subset.capitalize()} set: {len(subsets[subset])} samples.")

if __name__ == "__main__":
    labels_dir = '../datasets/labels'
    images_dir = '../datasets/images'
    output_dir = '../datasets/data_split'

    prepare_data(labels_dir, images_dir, output_dir)
