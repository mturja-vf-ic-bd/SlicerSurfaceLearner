#-----------------------------------------------------------------------------
set(MODULE_NAME PlaneCNNTrainer)

#-----------------------------------------------------------------------------
set(MODULE_PYTHON_SCRIPTS
  ${MODULE_NAME}.py
    DeepLearnerLib/data_utils/__init__.py
    DeepLearnerLib/data_utils/CustomDataset.py
    DeepLearnerLib/data_utils/GeomCnnDataset.py
    DeepLearnerLib/data_utils/utils.py
    DeepLearnerLib/models/__init__.py
    DeepLearnerLib/models/cnn_model.py
    DeepLearnerLib/pl_modules/__init__.py
    DeepLearnerLib/pl_modules/classifier_modules.py
    DeepLearnerLib/prediction/__init__.py
    DeepLearnerLib/prediction/predict.py
    DeepLearnerLib/training/__init__.py
    DeepLearnerLib/training/EfficientNetTrainer.py
    DeepLearnerLib/__init__.py
    DeepLearnerLib/Asynchrony.py
    DeepLearnerLib/CONSTANTS.py
    PlaneCNNTrainerUtil/__init__.py
    PlaneCNNTrainerUtil/CheckableComboBox.py
  )

set(MODULE_PYTHON_RESOURCES
  Resources/Icons/${MODULE_NAME}.png
  Resources/UI/${MODULE_NAME}.ui
  )

#-----------------------------------------------------------------------------
slicerMacroBuildScriptedModule(
  NAME ${MODULE_NAME}
  SCRIPTS ${MODULE_PYTHON_SCRIPTS}
  RESOURCES ${MODULE_PYTHON_RESOURCES}
  WITH_GENERIC_TESTS
  )

#-----------------------------------------------------------------------------
if(BUILD_TESTING)

  # Register the unittest subclass in the main script as a ctest.
  # Note that the test will also be available at runtime.
  slicer_add_python_unittest(SCRIPT ${MODULE_NAME}.py)

  # Additional build-time testing
  add_subdirectory(Testing)
endif()
