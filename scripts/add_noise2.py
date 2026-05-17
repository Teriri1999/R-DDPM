import cv2
import numpy as np

def add_sar_style_noise(image, shape=0.5, scale=1):
    row, col, ch = image.shape

    # 生成与图像尺寸相匹配的伽马分布矩阵
    gamma_matrix = np.random.gamma(shape, scale, (row, col, ch))

    # 将图像转换为浮点型数据
    image = image.astype(float)

    # 将图像的每个像素乘以伽马分布矩阵
    noisy_image = image * gamma_matrix

    # 将像素值限制在0到255之间
    noisy_image = np.clip(noisy_image, 0, 255)

    # 将图像转换回uint8类型
    noisy_image = noisy_image.astype(np.uint8)
    return noisy_image

img_path = r"J:\IRDM\Sentinel-1 dataset\Sentinel-Gtruth\1_scaled_0_512.tiff"
img = cv2.imread(img_path)

# 调整shape和scale参数以控制噪声的形状和规模
noisy_img = add_sar_style_noise(img, shape=1, scale=1)

output_path = 'Sentinel-1 dataset/output/noisy_image_sar_style.tiff'
cv2.imwrite(output_path, noisy_img)

print(f"Noisy SAR-style image saved at {output_path}")

