#find_package(SDL2 REQUIRED)
#find_package(SDL2_ttf REQUIRED)
#find_package(SDL2_image REQUIRED)
find_package(spdlog REQUIRED)

add_executable(sandbox
  main.cpp
  )

target_link_libraries(sandbox PRIVATE
  project_warnings
  project_options
  core
  spdlog::spdlog
  #  SDL2::SDL2
  #SDL2_ttf::SDL2_ttf
  #SDL2_image::SDL2_image
  )
