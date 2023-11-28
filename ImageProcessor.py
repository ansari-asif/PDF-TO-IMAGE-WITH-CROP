from pdf2image import convert_from_path
from PIL import Image
import os 

class ImageProcessor:
    
    def __init__(self) -> None:
        self.target_height=1200
        self.target_width=900
    def crop_image(self,input_path, output_path, target_width, target_height):
        # Open the image file
        image = Image.open(input_path)
        # Get the dimensions of the original image
        original_width, original_height = image.size
        # Calculate the coordinates for cropping
        left = (original_width - target_width) / 2
        top = (original_height - target_height) / 2
        right = (original_width + target_width) / 2
        bottom = (original_height + target_height) / 2
        # Crop the image
        cropped_image = image.crop((left, top, right, bottom))
        # Save the cropped image
        cropped_image.save(output_path)
        print('image saved')

    def convert_pdf_to_image_with_cropping(self,pdf_path=None,save_dir_name=None):
        if pdf_path is not None or save_dir_name is not None:
            try:
                # comment: 
                print('processing image')
                images=convert_from_path(pdf_path)
                for i in range(len(images)):
                    images[i].save(f"{save_dir_name}/{i+1}.png")
                    input_path=f"{save_dir_name}/{i+1}.png"
                    self.crop_image(input_path,input_path,self.target_width,self.target_height)
                 
            except Exception as e:
                raise e
            # end try
        else:
            print('--------------------------------')
            print('Please enter pdf file path and save directory path')
            print('--------------------------------')
            
    def create_a_large_image(self,imgs_folder=None,img_name="LargeImage"):
        if imgs_folder is not None :
            files=os.listdir(imgs_folder)
            first_image = Image.open(f"{imgs_folder}/{files[0]}")
            width, height = first_image.size
            # print(width,height)
            combined_image = Image.new('RGB', (width, height * len(files)))
            for i,file in enumerate(files):
                img=Image.open(f"{imgs_folder}/{file}")
                combined_image.paste(img,(0,i*height))
            combined_image.save(f"./{img_name}.png")
        else:
            print('--------------------------------')
            print('Please enter images directory path')
            print('--------------------------------')
    
img_processor=ImageProcessor()
img_processor.convert_pdf_to_image_with_cropping('./coding_ninjas.pdf','./pdf2image/') #call this function to convert pdf to image with cropping
#img_processor.create_a_large_image('./pdf2image/') #call this func() after convert_pdf_to_image_with_cropping calling this function