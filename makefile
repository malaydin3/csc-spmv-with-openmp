# Compiler
CXX = g++

# Compiler flags
CXXFLAGS = -Wall -O2 -fopenmp

# Target executable
TARGET = csc_spmv.out

# Source file
SRC = csc_spmv.cpp

# Rule to build the target
$(TARGET): $(SRC)
	$(CXX) $(CXXFLAGS) $(SRC) -o $(TARGET)

# Clean rule to remove the target
clean:
	rm -f $(TARGET)
