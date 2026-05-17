from PIL import Image
import os

# 定义文件夹路径
folder_path = r"J:\IRDM\Sentinel-1 dataset\test\input1"  # 文件夹路径

# 获取文件夹中所有文件
image_files = [f for f in os.listdir(folder_path) if f.endswith('.tiff')]

# 遍历文件夹中的每张图片并转换为JPEG格式
for filename in image_files:
    img_path = os.path.join(folder_path, filename)
    img = Image.open(img_path)

    # 保存为JPEG格式，默认质量
    jpg_path = os.path.join("J:/IRDM/Sentinel-1 dataset/test/input", os.path.splitext(filename)[0] + '.jpg')
    img.convert('RGB').save(jpg_path, 'JPEG')
