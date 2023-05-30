from PIL import Image
import os

img_src = './img/'
pdf_src = './pdf/'

unwanted_extensions = ['.DS_Store']  # for MacOS

images = sorted(os.listdir(img_src))

images = [image for image in images if not any(unwanted_ext in image for unwanted_ext in unwanted_extensions)]

if len(images) > 0:
    try:
        base = Image.open(os.path.join(img_src, images[0])).convert('RGB')
        img_list = []
        if len(images) > 1:
            for file in images[1:]:
                image = Image.open(os.path.join(img_src, file))
                img_list.append(image.convert('RGB'))
        base.save(os.path.join(pdf_src, 'combined.pdf'),
                  save_all=True, subsampling=0, quality=100, append_images=img_list)
        print('Images were successfully merged into PDF!')
    except Exception as e:
        print(f"Error occurred: {e}")
