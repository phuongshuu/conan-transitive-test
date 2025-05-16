import os
from conan import ConanFile
from conan.tools.cmake import CMakeDeps, CMakeToolchain, cmake_layout
from conan.tools.files import copy


class ConanSetup(ConanFile):
    settings = "os", "compiler", "arch", "build_type"
    def requirements(self):
        self.requires("transitive-boost/1.0.0@test/test")

    def layout(self):
        cmake_layout(self)

    def generate(self):
        deps = CMakeDeps(self)
        deps.generate()
        tc = CMakeToolchain(self)
        tc.generate()
