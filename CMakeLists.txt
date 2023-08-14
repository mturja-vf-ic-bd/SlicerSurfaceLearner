cmake_minimum_required(VERSION 3.13.4)

project(SlicerSurfaceLearner)

#-----------------------------------------------------------------------------
# Extension meta-information
set(EXTENSION_HOMEPAGE "https://www.slicer.org/wiki/Documentation/Nightly/Extensions/SlicerSurfaceLearner")
set(EXTENSION_CATEGORY "Examples")
set(EXTENSION_CONTRIBUTORS "Md Asadullah Turja (UNC Chapel Hill)")
set(EXTENSION_DESCRIPTION "A Slicer extension to apply convolutional neural network on surface data.")
set(EXTENSION_ICONURL "http://www.example.com/Slicer/Extensions/SlicerSurfaceLearner.png")
set(EXTENSION_SCREENSHOTURLS "http://www.example.com/Slicer/Extensions/SlicerSurfaceLearner/Screenshots/SurfaceLearnerWorkflow.png")
set(EXTENSION_DEPENDS "NA") # Specified as a list or "NA" if no dependencies

#-----------------------------------------------------------------------------
# Extension dependencies
find_package(Slicer REQUIRED)
include(${Slicer_USE_FILE})

#-----------------------------------------------------------------------------
# Extension modules
add_subdirectory(SurfacePlaneMapper)
add_subdirectory(PlaneCNNTrainer)
add_subdirectory(PlaneCNN)
## NEXT_MODULE

#-----------------------------------------------------------------------------
include(${Slicer_EXTENSION_GENERATE_CONFIG})
include(${Slicer_EXTENSION_CPACK})
