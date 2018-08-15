import tensorflow as tf
import train_model
import sys

arg_list = [
    sys.argv[0],
    "--name", "New name",
    "--learning_rate", 0.5
]

tf.app.run(main=train_model.main, argv=arg_list)
