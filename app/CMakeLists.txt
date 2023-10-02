set(MODULE_ID sandbox)

find_package(spdlog REQUIRED)

add_executable(${MODULE_ID}
  src/main.cpp)

target_link_libraries(${MODULE_ID}
  PRIVATE
    project_warnings
    project_options
    core
    spdlog::spdlog)
