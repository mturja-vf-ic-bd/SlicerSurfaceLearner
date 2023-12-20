#-----------------------------------------------------------------------------
set(MODULE_NAME SurfacePlaneMapper)

#-----------------------------------------------------------------------------
set(MODULE_PYTHON_SCRIPTS
  ${MODULE_NAME}.py
    geometry_image/Sphere_Template/__init__.py
    geometry_image/tools/__init__.py
    geometry_image/tools/perform_sgim_sampling.py
    geometry_image/tools/run.py
    geometry_image/tools/vtk_tools.py
    SurfacePlaneMapperUtil/__init__.py
    SurfacePlaneMapperUtil/Asynchrony.py
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
