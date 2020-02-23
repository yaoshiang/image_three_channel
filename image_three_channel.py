import argparse
import os
from pathlib import Path
from PIL import Image
import numpy as np

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--srcdir", type=str, default=".", help="Directory of source images. Images are modified in place. ")
    # parser.add_argument("--destdir", type=str, help="Directory of destination images. Unspecified destdir changes images in place.")
    args = parser.parse_args()

    # print("srcdir:" + args.srcdir)
    # print("destdir:" + (args.destdir if args.destdir is not None else "<none>"))

    # for filename in os.listdir(args.srcdir):
    #     if filename.endswith('.png'):
    #         print(filename)

    srcdir = Path(args.srcdir)

    for p in srcdir.iterdir():
        print(p)
        image = Image.open(p)

        npimage = np.asarray(Image.open(p))
        # print(npimage.shape)

        if 2 == len(npimage.shape) or 4 == npimage.shape[2]:
            # This is a reduced, one channel image (B&W or monochrome).
            newimage = image.convert("RGB")
            newimage.save(p)




if __name__ == "__main__":
    main()