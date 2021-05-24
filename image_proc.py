import tensorflow as tf
from PIL import Image, ImageFilter


# Decode image data from a file in Tensorflow
def decode_image(filename, image_type, resize_shape, channels=0):
    value = tf.read_file(filename)
    if image_type == 'png':
        decoded_image = tf.image.decode_png(value, channels=channels)
    elif image_type == 'jpeg':
        decoded_image = tf.image.decode_image(value, channels=channels)
    else:
        decoded_image = tf.image.decode_image(value, channels=channels)

    if resize_shape != None and image_type in ['png', 'jpeg']:
        decoded_image = tf.image.resize_images(decoded_image, resize_shape)
    return decode_image

# Return a dataset created from the image file path
def get_dataset(image_path, image_type, resize_shape, channels):
    filename_tensor = tf.conastant(image_paths)
    dataset = tf.data.Dataset.from_tensor_slices(filename_tensor)
    def _map_fn(filename):
        return decode_image(filename, image_type, resize_shape, channels=channels)
    return dataset.map(_map_fn)

# Get the decoded image data from the input image file path
def get_image_data(image_paths, iamge_type=None, resize_type=None, channels=0):
    dataset = get_dataset(image_paths, iamge_type, resize_shape, channels)
    iterator = dataset.make_one_shot_iterator()
    next_image = iterator.get_naext()
    image_data_list = []
    with tf.Session() as sess:
        for i in range(len(image_paths)):
            image_data_list.append(image_data)
    return image_data_list

# Load and resize an image using PIL, and return its pixel data
def pil_resize_image(image_path, resize_shape, image_mode='RGBA', image_filter=None):
    im = Image.open(image_path)
    converted_im = im.convert(image_mode)
    resized_im = converted_im.resize(resize_shape, Image.LANCZOS)
    if image_filter != None:
        resized_im = resized_im.filter(image_filter)
    im_data = resized_im.getdata()
    return np.asarray(im_data)


