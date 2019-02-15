import pyocr
import pyocr.builders
import argparse
from PIL import Image

#parser = argparse.ArgumentParser(description='tesseract ocr test')
#parser.add_argument('image', help='image path')
#args = parser.parse_args()

tools = pyocr.get_available_tools()

if len(tools) == 0:
    print("No OCR tool found")
    sys.exit(1)
# The tools are returned in the recommended order of usage
tool = tools[0]

res = tool.image_to_string(Image.open("SnapCrab_NoName_2019-2-16_2-43-51_No-00.png"),
                           lang="jpn",
                           builder=pyocr.builders.TextBuilder(tesseract_layout=6))
print(res);