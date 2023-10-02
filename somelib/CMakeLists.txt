set(MODULE_ID somelib)

add_library(${MODULE_ID} STATIC
    src/somelib.cpp)

target_include_directories(${MODULE_ID} PUBLIC 
    "$<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}>/src"
    "$<INSTALL_INTERFACE:${CMAKE_INSTALL_INCLUDEDIR}>")

target_link_libraries(${MODULE_ID} 
    PRIVATE
        project_warnings
        project_options)

file(GLOB SOMELIB_HEADER_FILES src/*.h)

install(TARGETS ${MODULE_ID})

install(FILES
    ${SOMELIB_HEADER_FILES}
    DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}/somelib)

if (BUILD_TESTING)
    find_package(Catch2 REQUIRED)

    add_executable(utest_${MODULE_ID}
        test/utest_somelib.cpp)

    target_include_directories(utest_${MODULE_ID} 
        PRIVATE
            "${CMAKE_CURRENT_SOURCE_DIR}>/src")

    target_link_libraries(
        utest_${MODULE_ID}
            PRIVATE
                project_warnings
                project_options
                ${MODULE_ID}
                Catch2::Catch2WithMain)

    include(Catch)
    catch_discover_tests(utest_${MODULE_ID} TEST_PREFIX "${MODULE_ID}@")
endif ()

