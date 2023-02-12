cmake_minimum_required(VERSION 3.12)
cmake_policy(SET CMP0077 NEW)

# Project definition
project(
    Sandbox
    VERSION 0.1
    LANGUAGES CXX)

# Build customization
set(CMAKE_BUILD_TYPE Debug)
set(WARNINGS_AS_ERRORS True)
set(ENABLE_CLANG_TIDY False)
set(ENABLE_SANITIZERS True)

# Project-specific settings
add_library(project_options INTERFACE)
target_compile_features(project_options INTERFACE cxx_std_20)

# Pseudo-library for adding compiler warning flags to targets
add_library(project_warnings INTERFACE)
include(CompilerWarnings.cmake)
set_project_warnings(project_warnings)

# Misc options
set(CMAKE_CXX_STANDARD_REQUIRED True)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

set(ENABLE_UTEST True)
enable_testing()

include(StaticAnalysis.cmake)

# Path to conan-installed libraries
list(APPEND CMAKE_MODULE_PATH ${CMAKE_BINARY_DIR}/conan)
list(APPEND CMAKE_PREFIX_PATH ${CMAKE_BINARY_DIR}/conan)

#
# Project structure
#
include_directories(.)

add_subdirectory(core)
add_subdirectory(app)
