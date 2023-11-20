# This file defines a set constants related to file paths / hyperparamters for training DL models
import pathlib
import os

PREFIX = pathlib.Path.home()

DEFAULT_FILE_PATHS = {
    "BASE_DIR": os.path.join(PREFIX, "SlicerSurfaceLearner"),
    "TRAIN_DATA_DIR": os.path.join(PREFIX, "surface_data_train"),
    "TEST_DATA_DIR": os.path.join(PREFIX, "surface_data_test"),
    "FEATURE_DIRS": ["eacsf"],
    "FILE_SUFFIX": ["_flat", "_flat"],
    "TIME_POINTS": ["V06"],
    "FILE_EXT": ".png"
}
