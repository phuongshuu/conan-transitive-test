add_library(transitive-boost dummy.cc)
target_link_libraries(transitive-boost PUBLIC Boost::program_options)
