function (add_sanitizers project_name)
    option(ENABLE_SANITIZERS "Enable sanitizers" Off)

    if (ENABLE_SANITIZERS)
        target_compile_options(${project_name} INTERFACE "$<$<CONFIG:Debug>:-fsanitize=address>")
        target_link_options(${project_name} INTERFACE "$<$<CONFIG:Debug>:-fsanitize=address>")
    endif ()
endfunction ()
