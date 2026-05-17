import cv2
import numpy as np
import os

# 定义文件夹路径
folder_path = r"J:\IRDM\Sentinel-1 dataset\Sentinel-1"  # 文件夹路径

# 获取文件夹中所有文件
image_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

# 遍历文件夹中的每张图片并添加噪声
for filename in image_files:
    img_path = os.path.join(folder_path, filename)
    image = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)  # 以灰度模式读取图像

    # 计算原始图像的平均亮度
    mean_brightness = np.mean(image)

    # 定义阈值，将非白色区域作为掩模
    threshold = 150  # 举例，可根据实际情况调整
    mask = cv2.threshold(image, threshold, 255, cv2.THRESH_BINARY)[1]

    # 添加白色高斯噪声到非白色区域
    mean = 0
    sigma = 75  # 调整这个值以改变噪声水平

    row, col = image.shape
    gaussian = np.abs(np.random.normal(mean, sigma, (row, col)))  # 使用绝对值确保只有正值
    noisy_image = np.copy(image)
    noisy_pixels = noisy_image[mask != 255] + gaussian[mask != 255].astype(np.uint8)
    noisy_image[mask != 255] = np.clip(noisy_pixels, 0, 255)

    # 调整图像的亮度，使其保持原始平均亮度
    new_mean_brightness = np.mean(noisy_image)
    brightness_difference = mean_brightness - new_mean_brightness
    brightness_difference = np.clip(brightness_difference, -127, 127)  # 将值限制在 int8 范围内
    noisy_image = noisy_image.astype(np.int16)  # 将图像类型转换为 int16
    noisy_image += brightness_difference.astype(np.int16)  # 应用亮度调整
    noisy_image = np.clip(noisy_image, 0, 255).astype(np.uint8)  # 将图像像素值限制在 0 到 255 之间，并转回 uint8

    # 保存处理后的图像
    output_path = os.path.join('Sentinel-1 dataset/train/input', filename)  # 保存到新文件夹，加上前缀 "noisy_"
    cv2.imwrite(output_path, noisy_image)  # 保存带有噪声的图像


# # 读取图像
# img_path = r"J:\IRDM\Sentinel-1 dataset\Sentinel-Gtruth\1_scaled_0_512.tiff"
# image = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)  # 以灰度模式读取图像
#
# # 计算原始图像的平均亮度
# mean_brightness = np.mean(image)
#
# # 定义阈值，将非白色区域作为掩模
# threshold = 150  # 举例，可根据实际情况调整
# mask = cv2.threshold(image, threshold, 255, cv2.THRESH_BINARY)[1]
#
# # 添加白色高斯噪声到非白色区域
# mean = 0
# sigma = 30  # 调整这个值以改变噪声水平
#
# row, col = image.shape
# gaussian = np.abs(np.random.normal(mean, sigma, (row, col)))  # 使用绝对值确保只有正值
# noisy_image = np.copy(image)
# noisy_pixels = noisy_image[mask != 255] + gaussian[mask != 255].astype(np.uint8)
# noisy_image[mask != 255] = np.clip(noisy_pixels, 0, 255)
#
# # 调整图像的亮度，使其保持原始平均亮度
# new_mean_brightness = np.mean(noisy_image)
# brightness_difference = mean_brightness - new_mean_brightness
# brightness_difference = np.clip(brightness_difference, -127, 127)  # 将值限制在 int8 范围内
# noisy_image = noisy_image.astype(np.int16)  # 将图像类型转换为 int16
# noisy_image += brightness_difference.astype(np.int16)  # 应用亮度调整
# noisy_image = np.clip(noisy_image, 0, 255).astype(np.uint8)  # 将图像像素值限制在 0 到 255 之间，并转回 uint8
#
# output_path = 'Sentinel-1 dataset/output/noisy_image_sar_gray_gamma.tiff'
# cv2.imwrite(output_path, noisy_image)  # 保存带有噪声的图像









