import os
import glob
import xml.etree.ElementTree as ET
import shutil
import json


def xml_to_yolo_bbox(bbox, w, h):
    x_center = ((bbox[0] + bbox[2]) / 2) / w
    y_center = ((bbox[1] + bbox[3]) / 2) / h
    width = (bbox[2] - bbox[0]) / w
    height = (bbox[3] - bbox[1]) / h
    return [x_center, y_center, width, height]


def yolo_to_xml_bbox(bbox, w, h):
    w_half_len = (bbox[2] * w) / 2
    h_half_len = (bbox[3] * h) / 2
    xmin = int((bbox[0] * w) - w_half_len)
    ymin = int((bbox[1] * h) - h_half_len)
    xmax = int((bbox[0] * w) + w_half_len)
    ymax = int((bbox[1] * h) + h_half_len)
    return [xmin, ymin, xmax, ymax]


def convert_annotations(input_dir, output_dir, image_dir):
    classes = []

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    files = glob.glob(os.path.join(input_dir, '*.xml'))
    for fil in files:
        basename = os.path.basename(fil)
        filename = os.path.splitext(basename)[0]
        image_path = os.path.join(image_dir, f'{filename}.png')
        if not os.path.exists(image_path):
            print(f'{filename}.png does not exist. Skipping.')
            continue

        result = []

        tree = ET.parse(fil)
        root = tree.getroot()
        width = int(root.find('size').find('width').text)
        height = int(root.find('size').find('height').text)

        for obj in root.findall('object'):
            label = obj.find('name').text

            if label not in classes:
                classes.append(label)

            index = classes.index(label)
            pil_bbox = [int(x.text) for x in obj.find('bndbox')]
            yolo_bbox = xml_to_yolo_bbox(pil_bbox, width, height)

            bbox_string = ' '.join([f"{coord:.6f}" for coord in yolo_bbox])
            result.append(f'{index} {bbox_string}')

        if result:
            with open(os.path.join(output_dir, f'{filename}.txt'), 'w') as f:
                f.write('\n'.join(result))

    # Save classes to classes.txt
    with open(os.path.join(output_dir, 'classes.txt'), 'w') as f:
        json.dump(classes, f)

    print("Conversion completed.")
    print(f"Total classes: {classes}")

if __name__ == "__main__":
    input_dir = '../datasets/annotations'
    output_dir = '../datasets/labels'
    image_dir = '../datasets/images'

    convert_annotations(input_dir, output_dir, image_dir)