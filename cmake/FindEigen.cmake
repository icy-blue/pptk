include(FindPackageHandleStandardArgs)

set(Eigen_INCLUDE_DIR "/usr/include/eigen3")

find_package_handle_standard_args(Eigen REQUIRED_VARS Eigen_INCLUDE_DIR)
