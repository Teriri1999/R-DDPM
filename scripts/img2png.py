import os
from PIL import Image

# 源文件夹路径和目标文件夹路径
source_folder = r"J:\AGSDNet-main\experimental_results\results_syn\img"
destination_folder = r"J:\AGSDNet-main\experimental_results\results_syn\imgs"

# 遍历文件夹中的文件
for filename in os.listdir(source_folder):
    filepath = os.path.join(source_folder, filename)
    if os.path.isfile(filepath):
        # 检查文件是否为图片（这里假设只处理常见的图片格式）
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            try:
                # 打开图片
                with Image.open(filepath) as img:
                    # 将图像转换为RGB格式并保存为PNG格式到目标文件夹
                    rgb_img = img.convert("RGB")
                    new_filepath = os.path.join(destination_folder, filename.split('.')[0] + '.png')
                    rgb_img.save(new_filepath, format='PNG')
                    print(f"Converted {filename} to RGB PNG and saved as {new_filepath}")
            except Exception as e:
                print(f"Error converting {filename}: {e}")
