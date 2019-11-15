import tensorflow as tf
import keras

from keras.metrics import categorical_accuracy, top_k_categorical_accuracy

def top_3_accuracy(y_true, y_pred):
    return top_k_categorical_accuracy(y_true, y_pred, k=3)


def top_2_accuracy(y_true, y_pred):
    return top_k_categorical_accuracy(y_true, y_pred, k=2)

converter = tf.lite.TFLiteConverter.from_keras_model_file('model.h5',custom_objects=
                                                                    {'top_2_accuracy':top_2_accuracy,'top_3_accuracy':top_3_accuracy})

model = converter.convert()

file = open( 'model.tflite' , 'wb' )

file.write( model )