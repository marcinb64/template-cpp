# Project name

## TODOs

 - [ ] Update author name and year in LICENSE file
 - [ ] Update project metadata in conanfile.py
 - [ ] Update project name in CMakeLists.txt
 - [ ] Update this README file

## About

## Dependencies

 * Catch2 for unit testing
 * spdlog for logging

## Build

Example build commands, using conan profiles `linux-debug` and `linux-release`.

    conan install conanfile.py --build=missing --profile linux-debug
    conan install conanfile.py --build=missing --profile linux-release
    cmake --preset conan-debug
    cmake --build build/Debug

    conan create . --profile=linux-release
    conan create . --profile=linux-debug