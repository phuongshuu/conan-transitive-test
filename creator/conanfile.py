# vim: set ft=python:
from conan.tools.cmake import CMake, CMakeToolchain, CMakeDeps, cmake_layout
from conan.tools.files import save, copy, rm
import shutil
import os
import re
from conan import ConanFile


class ConanTransitiveBoost(ConanFile):
    name = "transitive-boost"
    package_type = "library"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {
        "shared": False}
    exports_sources = ["src/*"]

    def layout(self):
        cmake_layout(self)

    def requirements(self):
        self.requires("boost/1.85.0")

    def source(self):
        cmake_contents = """
cmake_minimum_required(VERSION 3.21)

set(CMAKE_CXX_STANDARD 23)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

project(transitive-boost)
find_package(Boost COMPONENTS program_options REQUIRED)
add_subdirectory(src)

"""
        save(self, path=os.path.join(self.source_folder,
             "CMakeLists.txt"), content=cmake_contents)

    def generate(self):
        tc = CMakeToolchain(self)
        tc.generate()

        deps = CMakeDeps(self)
        deps.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        copy(self, "*.h", src=os.path.join(self.build_folder, "src"),
             dst=os.path.join(self.package_folder, "include"))
        copy(self, "*.h", src=os.path.join(self.source_folder, "src"),
             dst=os.path.join(self.package_folder, "include"))
        copy(self, "*.so", src=self.build_folder,
             dst=os.path.join(self.package_folder, "lib"), keep_path=False)
        copy(self, "*.a", src=self.build_folder,
             dst=os.path.join(self.package_folder, "lib"), keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["transitive-boost"]
        self.cpp_info.includedirs = ["include"]
