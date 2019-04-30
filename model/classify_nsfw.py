import json

import tensorflow as tf

from image_utils import yahoo_load_image
from model import OpenNsfwModel

import ai_integration


model = OpenNsfwModel()

# the default session behavior is to consume the entire GPU RAM during inference!
config = tf.ConfigProto()
config.gpu_options.per_process_gpu_memory_fraction = 0.065

with tf.Session(config=config) as sess:
    model.build()

    sess.run(tf.global_variables_initializer())

    while True:
        with ai_integration.get_next_input(inputs_schema={
            "image": {
                "type": "image"
            }
        }) as inputs_dict:

            image = yahoo_load_image(inputs_dict['image'])

            predictions = sess.run(model.predictions, feed_dict={model.input: image})

            result_data = {
                "content-type": 'application/json',
                "data": json.dumps({"nsfw_score": float(predictions[0][1])}),
                "success": True,
                "error": None
            }

            ai_integration.send_result(result_data)
