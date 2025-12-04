import base64
import os
from .models import Table

def encode_image_to_base64(image_path):
    with open(os.path.join(os.getcwd(), image_path), "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
    return f"data:image/jpeg;base64,{encoded_string}"


                  
      