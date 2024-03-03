import cv2 as cv
import os


def crop_image_and_write(img, row, dest_directory):
    square_side = 60
    initial_x = 50
    initial_y = 42 + square_side * row

    for i in range(1, 21):
        y_range = (initial_y, initial_y + square_side)
        x_range = (initial_x + square_side * (i - 1), initial_x + square_side * i)
        cropped_img = img[y_range[0]:y_range[1],x_range[0]:x_range[1]]
        cv.imwrite(dest_directory + "/" + str(i) + ".jpg", cropped_img)
    return


def main():
    source_directory = "./input"
    dest_directory = "./output"
    imgs = {}
    for filename in os.listdir(source_directory):
        if filename.endswith(".jpg"):
            imgs[filename.split(".")[0]] = cv.imread(source_directory + "/" + filename)

    for imgname in imgs.keys():
        dude_dirname = dest_directory + "/" + imgname
        os.makedirs(dude_dirname, exist_ok=True)
        for i, vowel in enumerate("aeiou"):
            cropped_img_dirname = dude_dirname + "/" + vowel
            os.makedirs(cropped_img_dirname, exist_ok=True)
            crop_image_and_write(imgs[imgname], i, cropped_img_dirname)
    return

if __name__ == "__main__":
    main()
