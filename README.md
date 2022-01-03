# Telegram Sticker Generator

A little helper to generate Stickers for the Telegram messenger

## Description

Stickers for Telegram must be 512 pixels on one side and 512 pixels or less on the other side. It is recommended that stickers have a white outline and a black transparent shadow.
To create such images the same steps have to be done over and over again, images have to been cut out, the outline must be added, a shadow also and finally the whole thing must be croped and scaled.
Because those steps are always the same this little python-scrips automates most of those.

## Usage

### Prequisites

* Python 3 (tested with 3.10)
* [PIL Package for python](https://python-pillow.org/)

If you use pip you can install PIL (or pillow) by

````
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade Pillow
`````

### Preparation

* Take the image that should become a telegram sticker
* Create a png-file with full transparency of everything you don't want to be the sticker
* save it to the same folder as the script and use this naming-sceme: `[NAME] step02 die cut.png` the script searches for filesnames which contain *"step02"*
* * "step02" because I assume the original image (with background and without transparency) might be "step01"
* do this for as many images as you want with different `[NAME]` the script will process one after the other (because this takes some time you might want to do so while your computer works alone)

### Action

Run the script:

````
python3 process_images.py
````

The script will generate several image files, especially the fifth step takes a while, please be patient! (Because I did not do this verry efficient).
The last step generates `[NAME] step08 final.png` and this is the image you can upload to telegrams Sticker-Bot.

## Details

These are the detailed steps the script does:

* Step 03: the image is cropped so all transparent pixels are cut off
* Step 04: the image is resized to 512 pixels to reduce the processing time of the further steps (it could also be something like 900px to raise the quality)
* Step 05: a white shadowcopy is generated which is slightly larger but the original at the same time
* Step 06: a black shadowcopy is generated, identical to the white one.
* Step 07: the layers from steps 4-6 are combined.
* Step 08: the whole image is again resized to 512 pixels.

These steps are processed for every image found with `step02` in its filename.

By looking at the generated images you might see misstakes or errors and might be able to fix them or use those to do some of the steps manually.
