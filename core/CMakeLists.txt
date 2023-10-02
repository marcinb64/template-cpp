set(MODULE_ID core)

add_library(${MODULE_ID} STATIC
    src/core.cpp)

target_include_directories(${MODULE_ID} PUBLIC
    src)

target_link_libraries(${MODULE_ID} 
    PRIVATE
        project_warnings
        project_options)

if (BUILD_TESTING)
    find_package(Catch2 REQUIRED)

    add_executable(utest_${MODULE_ID} 
        test/utest_core.cpp)

    target_link_libraries(utest_${MODULE_ID}
        PRIVATE 
            project_warnings
            project_options
            Catch2::Catch2WithMain
            ${MODULE_ID})

    include(Catch)
    catch_discover_tests(utest_${MODULE_ID} TEST_PREFIX "${MODULE_ID}@")
endif ()
