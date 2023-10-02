# Project name

## TODOs

 - [ ] [Choose license](https://choosealicense.com) and update LICENSE file
 - [ ] Update project metadata in conanfile.py
 - [ ] Update project name in CMakeLists.txt
 - [ ] Update this README file
 - [ ] Customize .clang-tidy and .clang-format as needed

## About

## Dependencies

Example dependencies

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

Example conan profile: `linux-debug`

    [settings]
    arch=x86_64
    build_type=Debug
    compiler=gcc
    compiler.cppstd=20
    compiler.libcxx=libstdc++11
    compiler.version=12
    os=Linux

Example conan profile: `linux-release`

    [settings]
    arch=x86_64
    build_type=Release
    compiler=gcc
    compiler.cppstd=20
    compiler.libcxx=libstdc++11
    compiler.version=12
    os=Linux
