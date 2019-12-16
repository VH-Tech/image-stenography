# image-stenography
Encrypt data using images

<h3>how it works?</h3>

Each letter of your text provided is encrypted to corresponding RGB values according to <code>key.json</code>

<b></i>*You may edit key.json if you want to change corresponding RGB values. You won't face any issues while decrypting as decryption is done using key.json file only.</i></b>
<h3>how to use?</h3>

<h4>Encryption</h4>
Use <code>sudo python3 hide.py -e YOUR_IMAGE_FILE</code> to encrypt data to your image.

<h4>Decryption</h4>
Use <code>sudo python3 hide.py -d YOUR_IMAGE_FILE</code> to decrypt data from your image.

https://asciinema.org/a/QSW3b4yqqZBWWS4x58zYp6ae2
