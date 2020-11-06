import codecs
import struct
import sys


def read_labels(filename, n):
	labels = []
	with open(filename, mode='rb') as file:
		magic_number = file.read(4)
		number_of_items = file.read(4)

		magic_number = struct.unpack('>i', magic_number)[0]
		number_of_items = struct.unpack('>i', number_of_items)[0]

		for _ in range(n):
			label = file.read(1)
			label = struct.unpack('>b', label)[0]
			labels.append(label)
	return labels

def read_images(filename, n):
	images = []
	with open(filename, mode='rb') as file:
		magic_number = file.read(4)
		number_of_images = file.read(4)
		rows = file.read(4)
		columns = file.read(4)

		magic_number = struct.unpack('>i', magic_number)[0]
		number_of_images = struct.unpack('>i', number_of_images)[0]
		rows = struct.unpack('>i', rows)[0]
		columns = struct.unpack('>i', columns)[0]

		print("there is ", number_of_images, " images")

		for i in range(n):
			final = "P1\n"
			final += "{0} {1}\n".format(columns, rows)
			for _ in range(rows):
				for _ in range(columns):
					pixel = file.read(1)
					pixel = struct.unpack('>b', pixel)[0]
					if pixel != 0:
						pixel = 1
					final += "{} ".format(pixel)
				final += '\n'
			images.append(final)
		return images

def write_images(images, folder):
	index = 0
	for image, label in images.items():
		with open("{}/number_{}-index_{}.ppm".format(folder, label, index), mode='w') as file:
			file.write(image)
		index+=1
	print("The images were written")



n = 10

if len(sys.argv) <= 1:
	images_path = "sets/t10k-images-idx3-ubyte"
	labels_path = "sets/t10k-labels-idx1-ubyte"
elif len(sys.argv) == 2:
	print("You forgot the label file")
	sys.exit()
elif len(sys.argv) == 3:
	images_path = sys.argv[1]
	labels_path = sys.argv[2]
else:
	images_path = sys.argv[1]
	labels_path = sys.argv[2]
	n = int(sys.argv[3])


images = read_images(images_path, n)
labels = read_labels(labels_path, n)


hash_map = dict(zip(images, labels))


write_images(hash_map, "output")
