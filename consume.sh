#! /usr/bin/bash
source _venv/bin/activate
BUILD_FOLDER=$(pwd)/_build
mkdir -p ${BUILD_FOLDER}
conan install --output-folder=${BUILD_FOLDER} -pr:a=profile.txt -s:a build_type=Debug ./consumer/conanfile.py
cmake -S ./consumer/. -B ${BUILD_FOLDER} /consumer -DCMAKE_BUILD_TYPE=Debug -DCMAKE_TOOLCHAIN_FILE=${BUILD_FOLDER}/build/Debug/generators/conan_toolchain.cmake
