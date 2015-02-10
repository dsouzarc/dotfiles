from PIL import Image

foo = Image.open("anonymous.jpg");

print(foo.size);

foo = foo.resize((250, 250), Image.ANTIALIAS);

foo.save("anonymous resize.jpg", quality=97);

