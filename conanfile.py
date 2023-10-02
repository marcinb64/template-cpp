from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout


class HelloConan(ConanFile):
    name = "somelib"
    version = "0.1"

    # Optional metadata
    license = "MIT"
    author = "<author>"
    #url = "http://site.com"
    description = "Some lib"
    topics = ("foo", "bar")
    
    # Binary configuration
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}

    # Sources are located in the same place as this recipe, copy them to the recipe
    exports_sources = "CMakeLists.txt", "*.cmake", "core/*", "app/*", "somelib/*"
    generators = "CMakeDeps"

    def requirements(self):
        self.requires("catch2/3.1.0")
        self.requires("spdlog/1.10.0")

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def layout(self):
        cmake_layout(self)

    def generate(self):
        tc = CMakeToolchain(self)
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build(target="somelib")

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["somelib"]
