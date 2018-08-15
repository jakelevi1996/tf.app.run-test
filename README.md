
# tf.app.run-test

Test repository for calling the tf.app.run wrapper (inside `train_model.py`) from a different script (in this case `run_experiment.py`)

Works, as long as all arguments passed to `tf.app.run` in the `argv` argument are strings (floats cause errors!)
