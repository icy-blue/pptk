include(FindPackageHandleStandardArgs)

set(TBB_INCLUDE_DIR "/home/icy/tbb44_20160803oss/include")
set(TBB_tbb_LIBRARY "/home/icy/tbb44_20160803oss/lib/intel64/gcc4.4/libtbb.so")
set(TBB_tbb_RUNTIME "/home/icy/tbb44_20160803oss/lib/intel64/gcc4.4/libtbb.so")
set(TBB_tbbmalloc_LIBRARY "/home/icy/tbb44_20160803oss/lib/intel64/gcc4.4/libtbbmalloc.so")
set(TBB_tbbmalloc_RUNTIME "/home/icy/tbb44_20160803oss/lib/intel64/gcc4.4/libtbbmalloc.so")

find_package_handle_standard_args(TBB
  REQUIRED_VARS
    TBB_INCLUDE_DIR
    TBB_tbb_LIBRARY
    TBB_tbbmalloc_LIBRARY
    TBB_tbb_RUNTIME
    TBB_tbbmalloc_RUNTIME
)
