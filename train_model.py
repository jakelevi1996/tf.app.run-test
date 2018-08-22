import tensorflow as tf

tf.app.flags.DEFINE_float("learning_rate", 0.001, "[0.001] Learning rate")
tf.app.flags.DEFINE_string("name", "standard", "[standard] Name of the model")

FLAGS = tf.app.flags.FLAGS

def train():
    print("Model name: ", FLAGS.name)
    print("Learning rate: ", FLAGS.learning_rate)


def main(_):
    # For easier testing/better API, maybe FLAG attributes should be accessed
    # here and passed as arguments to train() ??
    train()


if __name__ == "__main__":
    tf.app.run()
