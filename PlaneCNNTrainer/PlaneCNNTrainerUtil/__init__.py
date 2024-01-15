requirements = [
    "Pillow",
    "monai>=0.8",
    "pandas",
    "pytorch_lightning>=2.1.0",
    "scikit_learn",
    "tensorboard",
    "torch>=2.0.0",
    "torchmetrics>=1.2.1",
]


# noinspection PyUnresolvedReferences
def ensure_requirements():
    # Imports are ensured at the top-level, once, when the module is initialized. So this function is a no-op,
    # but will explicitly fail if any requirement is missing. Note that this function does _not_ check
    # version constraints; use `install_requirements()` for that.

    import torch
    import pytorch_lightning
    import pandas
    import torchmetrics
    import sklearn
    import PIL
    import monai


def install_requirements(upgrade=False):
    import slicer.util

    args = [*requirements]
    if upgrade:
        args.append("-U")

    slicer.util.pip_install(args)


try:
    ensure_requirements()
except ImportError:
    install_requirements()
