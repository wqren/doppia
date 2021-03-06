# This is a CMake build file, for more information consult:
# http://en.wikipedia.org/wiki/CMake
# and
# http://www.cmake.org/Wiki/CMake
# http://www.cmake.org/cmake/help/syntax.html
# http://www.cmake.org/Wiki/CMake_Useful_Variables
# http://www.cmake.org/cmake/help/cmake-2-8-docs.html

# to compile the local code you can use: cmake ./ && make -j2

# ----------------------------------------------------------------------
# Base CMake setup

cmake_minimum_required (VERSION 2.6)

set(doppia_root "../../..")

set(CMAKE_MODULE_PATH $ENV{CMAKE_MODULE_PATH})
set(CMAKE_MODULE_PATH "./" ${doppia_root} ${CMAKE_MODULE_PATH})
set(CMAKE_MODULE_PATH "/home/rodrigob/work/code/doppia_references/cuda/FindCUDA/CMake/cuda" ${CMAKE_MODULE_PATH})
set(CMAKE_MODULE_PATH "/users/visics/rbenenso/code/references/cuda/FindCUDA/CMake/cuda" ${CMAKE_MODULE_PATH})

# ----------------------------------------------------------------------
# Setup the project

include(FindPkgConfig)
project (BoostedLearning)

# ----------------------------------------------------------------------
# Setup dependency to another doppia cmake project
add_subdirectory(../bootstrapping_lib ../bootstrapping_lib EXCLUDE_FROM_ALL) # include only what we need
add_subdirectory(${doppia_root}/libs/liblinear-1.8 ${doppia_root}/libs/liblinear-1.8 EXCLUDE_FROM_ALL) # include only what we need


# FIXME for some strange reason this setup only works at the second call.
# run cmake ./ && cmake ./ && make to get things compiled

# ----------------------------------------------------------------------
# Site specific configurations
# these configurations were already added when adding the bootstrapping_lib subdirectory
include(${doppia_root}/common_settings.cmake)

# ----------------------------------------------------------------------
# Setup required libraries
pkg_check_modules(libpng REQUIRED libpng)
pkg_check_modules(opencv REQUIRED opencv>=2.3)

# ----------------------------------------------------------------------
# Setup link and include directories

set(local_LIBRARY_DIRS
  "/usr/local/lib"
  "/users/visics/rbenenso/no_backup/usr/local/lib"
  "/usr/lib64"
  "/usr/lib64/atlas"
  "/usr/lib/sse2/atlas"
  ${local_CUDA_LIB_DIR}
)

set(local_INCLUDE_DIRS
  "/users/visics/rbenenso/no_backup/usr/local/include"
  "/usr/include/eigen2/"
   "/usr/local/include/eigen2"
   "/usr/local/cuda/include"
   ${CUDA_INCLUDE_DIRS}
)

link_directories(
  ${libpng_LIBRARY_DIRS}
  ${opencv_LIBRARY_DIRS}
  ${local_LIBRARY_DIRS}
)

include_directories(
  "./"
  "${doppia_root}/libs"
  "${doppia_root}/src"
  "${doppia_root}/src/applications/bootstrapping_lib"
  "${doppia_root}/src/objects_detection/integral_channels"
  "${doppia_root}/src/objects_detection/"
  ${libpng_INCLUDE_DIRS}
  ${opencv_INCLUDE_DIRS}
  ${local_INCLUDE_DIRS}
  "${doppia_root}/libs/cudatemplates/include"
  ${doppia_root}/libs/liblinear-1.8
)

# ----------------------------------------------------------------------
# Collect source files

set(doppia_src "${doppia_root}/src")

file(GLOB SrcCpp 
  "./*.*pp"
  #"${doppia_src}/*.cpp"
  "${doppia_src}/objects_detection/*.pb.c*"
   #"${doppia_src}/applications/*.cpp"
)

file(GLOB HelpersCpp
  #"${doppia_src}/helpers/*.cpp"
  #"${doppia_src}/helpers/data/*.c*"
  "${doppia_src}/helpers/any_to_string.cpp"
  "${doppia_src}/helpers/Log.cpp"
  "${doppia_src}/helpers/loggers.cpp"
  "${doppia_src}/helpers/replace_environment_variables.cpp"
)


# ----------------------------------------------------------------------
# Create the executable

add_executable(boosted_learning
  ${SrcCpp}
  ${HelpersCpp}
)

target_link_libraries(boosted_learning

   bootstrapping
   linear

   boost_program_options-mt
   boost_filesystem-mt boost_system-mt
   boost_thread-mt pthread
   protobuf
   SDL X11 Xext #Xrandr
   gomp
   ${libpng_LIBRARIES} jpeg
   ${opencv_LIBRARIES}

   #${google_perftools_LIBS}
)   

# ----------------------------------------------------------------------
