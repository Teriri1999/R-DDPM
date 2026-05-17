import os
from PIL import Image


input_folder = r"J:\IRDM\TGRS\test\input2"
output_folder = r"J:\IRDM\TGRS\test\input"
os.makedirs(output_folder, exist_ok=True)


for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.tiff')):
        input_path = os.path.join(input_folder, filename)

        with Image.open(input_path) as img:
            if img.mode != 'RGB':
                img = img.convert('RGB')

            base_name = os.path.splitext(filename)[0]
            output_path = os.path.join(output_folder, base_name + '.png')

            img.save(output_path)

print("图像已成功转换为三通道并保存为 PNG。")
