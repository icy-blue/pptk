cmake_minimum_required(VERSION 3.1)
project(pptk)

set(Python3_ROOT_DIR "/home/icy/miniconda3/envs/pptk/bin")
set(Python3_NumPy_INCLUDE_DIRS "/home/icy/miniconda3/envs/pptk/lib/python3.8/site-packages/numpy/core/include/numpy")
set(PYTHON3_INCLUDE_DIRS "/home/icy/miniconda3/envs/pptk/include/python3.8")
set(PYTHON_LIBRARY "/home/icy/miniconda3/envs/pptk/lib/python3.8")
set(Eigen_INCLUDE_DIR "/usr/include/eigen3")
set(TBB_INCLUDE_DIR "/home/icy/tbb44_20160803oss/include")
set(TBB_tbb_LIBRARY "/home/icy/tbb44_20160803oss/lib/intel64/gcc4.4/libtbb.so")
set(TBB_tbb_RUNTIME "")
set(TBB_tbbmalloc_LIBRARY "/home/icy/tbb44_20160803oss/lib/intel64/gcc4.4/libtbbmalloc.so")
set(TBB_tbbmalloc_RUNTIME "")
set(Qt5_DIR "/usr/include/x86_64-linux-gnu/qt5")
set(PPTK_PATCHELF "/usr/bin/patchelf")
include_directories(${Python3_NumPy_INCLUDE_DIRS})
include_directories(${PYTHON3_INCLUDE_DIRS})
include_directories(${Eigen_INCLUDE_DIR})
include_directories(${TBB_INCLUDE_DIR})
include_directories(${Qt5_DIR})

set(CMAKE_BUILD_TYPE Release)
set(CMAKE_MODULE_PATH
  "${CMAKE_CURRENT_SOURCE_DIR}/cmake" ${CMAKE_CURRENT_SOURCE_DIR})

find_package(PythonLibs REQUIRED)
find_package(OpenGL REQUIRED)
find_package(Numpy REQUIRED)
find_package(TBB REQUIRED)
find_package(Eigen REQUIRED)
find_package(Qt5 CONFIG REQUIRED COMPONENTS Widgets Network OpenGL Core)
find_package(OpenMP)

# get root Qt5 folder (i.e. contains bin, lib, plugins, etc.)
get_target_property(Qt5_DIR Qt5::qmake LOCATION)
get_filename_component(Qt5_DIR ${Qt5_DIR} DIRECTORY)
get_filename_component(Qt5_DIR ${Qt5_DIR} DIRECTORY)
set(Qt5_PLUGINS_DIR ${Qt5_DIR}/plugins)

# localize all dependencies (.dll, .so, or .dylib) in the following folder
set(PPTK_LIBS_DIR ${PROJECT_BINARY_DIR}/pptk/libs)

# use the following variable to store a list of .dll paths required by targets
# built in pptk; this is useful only for building on Windows platform
get_filename_component(TBB_RUNTIME_DIR ${TBB_tbb_RUNTIME} DIRECTORY)
set(PPTK_DLL_DIRS
  ${TBB_RUNTIME_DIR}
  ${Qt5_DIR}/bin
  CACHE INTERNAL "Additional folder paths for finding .dll's")

# use patchelf to modify binary RPATH when building pptk on Linux
if(UNIX AND NOT APPLE)
  find_program(PPTK_PATCHELF patchelf)
  if (NOT PPTK_PATCHELF)
    message(FATAL_ERROR
      "patchelf needed for localizing library dependencies; \
      please manually set the PPTK_PATCHELF variable.")
  endif()
endif()

# adds -std=gnu++11 flag when compiling with gcc
set(CMAKE_CXX_STANDARD 11)

include(UsefulMacros)

# following lines specifies the CMAKE_INSTALL_SYSTEM_RUNTIME_LIBS variable
set(CMAKE_INSTALL_SYSTEM_RUNTIME_LIBS_SKIP TRUE)
set(CMAKE_INSTALL_OPENMP_LIBRARIES TRUE)  # requires cmake 3.1
include(InstallRequiredSystemLibraries)

copy_file(setup.py)
copy_file(LICENSE)
add_subdirectory(pptk)
add_subdirectory(licenses)
