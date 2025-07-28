cmake_minimum_required(VERSION 3.10)
project(csc_spmv_with_openmp CXX)

# Set C++ standard (17)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Generate compilation database for IntelliSense for VSCode
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

# Create input directory in build
message(STATUS "Creating input directory in build... ${CMAKE_BINARY_DIR}/input")
file(MAKE_DIRECTORY ${CMAKE_BINARY_DIR}/input)

# Copy input files to build directory
file(COPY ${CMAKE_SOURCE_DIR}/data/input/
     DESTINATION ${CMAKE_BINARY_DIR}/input)

# Add sanitizer flags for debugging/memory checking with AddressSanitizer
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fsanitize=address -fno-omit-frame-pointer")
set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} -fsanitize=address")

# Apple Silicon support just because I was at IL and AP
# So I am not sure if this is needed, but it is here just in case
if(APPLE)
    # Tryo to install libomp using Homebrew if not already installed
    execute_process(
        COMMAND brew --prefix libomp
        OUTPUT_VARIABLE LIBOMP_PREFIX
        OUTPUT_STRIP_TRAILING_WHITESPACE
    )
    # If libomp is not found, set a default prefix
    if(NOT EXISTS "${LIBOMP_PREFIX}")
        message(STATUS "Installing libomp via Homebrew...")
        execute_process(COMMAND brew install libomp)
    endif()
    
    # Set OpenMP flags for clang
    set(OpenMP_CXX_FLAGS "-Xpreprocessor -fopenmp")
    set(OpenMP_CXX_LIB_NAMES "omp")
    set(OpenMP_omp_LIBRARY ${LIBOMP_PREFIX}/lib/libomp.dylib)
    include_directories(${LIBOMP_PREFIX}/include)
endif()

# Find OpenMP
find_package(OpenMP REQUIRED)

# Set output directories
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)


# Add executable
add_executable(
    csc_spmv.out src/csc_spmv.cpp)
target_link_libraries(csc_spmv.out PRIVATE OpenMP::OpenMP_CXX)

# Print compiler flags for debugging
message(STATUS "CXX Flags: ${CMAKE_CXX_FLAGS}")
message(STATUS "OpenMP Flags: ${OpenMP_CXX_FLAGS}")