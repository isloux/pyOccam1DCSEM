cmake_minimum_required(VERSION 3.10)
project(occam1dcsem VERSION 7.3 LANGUAGES Fortran CXX)

find_package(MKL REQUIRED)

# Add the shared library
add_library(occam1dcsem SHARED
    src/FilterModules.f90
    src/Dipole1D.f90
    src/CallDipole1D.f90
)

# Link against MKL libraries
target_link_libraries(occam1dcsem PUBLIC ${MKL_LIBRARIES})

# Set library version
set_target_properties(occam1dcsem PROPERTIES
    VERSION "0.0.1"
    SOVERSION "0"
)
