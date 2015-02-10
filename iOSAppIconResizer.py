from PIL import Image
import sys

if len(sys.argv) == 1:
    fileName = raw_input("Enter file name and directory:\n");

else:
    fileName = sys.argv[1];

print(fileName);

foo = Image.open("anonymous.jpg");

print(foo.size);

foo = foo.resize((250, 250), Image.ANTIALIAS);

foo.save("anonymous resize.jpg", quality=97);

