# MNIST Extractor

## How to install
```bash
$ git clone https://github.com/Gryfenfer97/MNIST-Extractor.git
$ cd MNIST-Extractor
$ mkdir sets
```

## How to use

put the image file **and** the label file in the folder `set`.

```bash
$ python main.py "sets/t10k-images-idx3-ubyte" "sets/t10k-labels-idx1-ubyte" 130
```
to extract the first 130 images

They will be available in the output folder