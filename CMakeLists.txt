cmake_minimum_required(VERSION 3.13.4)

project(SlicerSurfaceLearner)

#-----------------------------------------------------------------------------
# Extension meta-information
set(EXTENSION_HOMEPAGE "https://github.com/mturja-vf-ic-bd/SlicerSurfaceLearner")
set(EXTENSION_CATEGORY "SurfaceLearner")
set(EXTENSION_CONTRIBUTORS "Md Asadullah Turja (UNC)")
set(EXTENSION_DESCRIPTION "SurfaceLearner provides a way to apply convolutional neural network based classifiers on surface meshes (e.g. brain surface)")
set(EXTENSION_ICONURL "https://raw.githubusercontent.com/mturja-vf-ic-bd/SlicerSurfaceLearner/main/SlicerSurfaceLearner.png")
set(EXTENSION_SCREENSHOTURLS "https://raw.githubusercontent.com/mturja-vf-ic-bd/SlicerSurfaceLearner/main/Screenshots/SurfaceLearnerWorkflow.png https://raw.githubusercontent.com/mturja-vf-ic-bd/SlicerSurfaceLearner/main/Screenshots/SurfaceLearnerOverviewImage.png")
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
