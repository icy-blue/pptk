include(FindPackageHandleStandardArgs)

set(Numpy_INCLUDE_DIR "/home/icy/miniconda3/envs/pptk/lib/python3.8/site-packages/numpy/core/include" CACHE PATH "Path of folder containing arrayobject.h")

find_package_handle_standard_args(Numpy REQUIRED_VARS Numpy_INCLUDE_DIR)
