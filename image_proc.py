import tensorflow as tf

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


