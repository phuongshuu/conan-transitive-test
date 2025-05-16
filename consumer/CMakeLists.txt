cmake_minimum_required(VERSION 3.21)
project(consumer)

set(CMAKE_CXX_STANDARD 23)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

find_package(transitive-boost REQUIRED)

add_executable(exec main.cc)
target_link_libraries(exec PUBLIC transitive-boost::transitive-boost)
