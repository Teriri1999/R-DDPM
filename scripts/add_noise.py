import cv2
import numpy as np
import os

folder_path = "./IRDM/Sentinel-1 dataset/Sentinel-1"

image_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

for filename in image_files:
    img_path = os.path.join(folder_path, filename)
    image = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    mean_brightness = np.mean(image)
    threshold = 150
    mask = cv2.threshold(image, threshold, 255, cv2.THRESH_BINARY)[1]

    mean = 0
    sigma = 75

    row, col = image.shape
    gaussian = np.abs(np.random.normal(mean, sigma, (row, col)))
    noisy_image = np.copy(image)
    noisy_pixels = noisy_image[mask != 255] + gaussian[mask != 255].astype(np.uint8)
    noisy_image[mask != 255] = np.clip(noisy_pixels, 0, 255)

    new_mean_brightness = np.mean(noisy_image)
    brightness_difference = mean_brightness - new_mean_brightness
    brightness_difference = np.clip(brightness_difference, -127, 127)
    noisy_image = noisy_image.astype(np.int16)
    noisy_image += brightness_difference.astype(np.int16)
    noisy_image = np.clip(noisy_image, 0, 255).astype(np.uint8)

    output_path = os.path.join('Sentinel-1 dataset/train/input', filename)
    cv2.imwrite(output_path, noisy_image)
