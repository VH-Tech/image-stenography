import cv2
import json
import ast
import argparse

parser=argparse.ArgumentParser()
parser.add_argument("-e", "--encrypt", help="image to encrypt")
parser.add_argument("-d", "--decrypt", help="image to decrypt")
args = vars(parser.parse_args())


if args['encrypt']:

    img = cv2.imread(args['encrypt'])

    text = input("Enter text to hide: ").lower()

    (h, w) = img.shape[:2]

    row = 0
    col = 0

    with open('key.json') as json_file:
        data = json.load(json_file)
        for i in text:
            j = ast.literal_eval(data[i])
            img[row, col] = j

            if col + 1 < w:
                col += 1

            elif col + 1 == w:
                col = 0
                row += 1

    if col + 1 < w:
        img[row, col] = [255, 255, 255]

    elif col + 1 == w:
        img[row + 1, 0] = [255, 255, 255]

    cv2.imwrite("plane.png", img)
    print("Completed!")


elif args['decrypt']:
    img = cv2.imread(args['decrypt'])

    text = []

    (h, w) = img.shape[:2]

    row = 0
    col = 0


    def stringify(arr):
        out = "["
        for i in arr:
            out = out + str(i) + ","

        out = out[:-1] + "]"
        return out


    with open('key.json') as json_file:
        data = json.load(json_file)
        inv_data = {v: k for k, v in data.items()}

        while True:
            col = 0
            while col + 1 < w:
                array_string = stringify(img[row, col])
                if array_string == "[255,255,255]":
                    break
                info = inv_data[array_string]
                text.append(info)
                col += 1
            if array_string == "[255,255,255]" or row + 1 > h:
                break
            row += 1


    def listtostring(list):
        string = ""
        return string.join(list)


    print("Your decrypted text : " + listtostring(text))






