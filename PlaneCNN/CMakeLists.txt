#-----------------------------------------------------------------------------
set(MODULE_NAME PlaneCNN)

#-----------------------------------------------------------------------------
set(MODULE_PYTHON_SCRIPTS
  ${MODULE_NAME}.py
    PlaneCNNUtil/__init__.py
    PlaneCNNUtil/CheckableComboBox.py
    InferenceLib/data_utils/__init__.py
    InferenceLib/data_utils/CustomDataset.py
    InferenceLib/data_utils/GeomCnnDataset.py
    InferenceLib/data_utils/utils.py
    InferenceLib/__init__.py
    InferenceLib/Asynchrony.py
    InferenceLib/CONSTANTS.py
    InferenceLib/logic.py
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
