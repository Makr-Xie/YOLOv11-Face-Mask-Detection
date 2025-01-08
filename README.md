# YOLOv11-Face-Mask-Detection

## Model Details

- **Model Location:** `runs/detect/train3`
  
  > **Note:** There is an issue with the label assignments. The `without_mask` label is incorrectly assigned to `with_mask` detections, and vice versa. This will be corrected in a future update.


## How to use

Open the `detect.py` file and modify the `test_image_path` variable to point to your JPEG image.

Then 

```python
   test_image_path = 'path/to/your/image.jpg'


