from quiver_engine.server import launch
import tensorflow as tf
model = tf.keras.applications.VGG16()
print(model.summary())

launch(model, input_folder=r'C:\Users\edoua\Desktop\img', port=7000)