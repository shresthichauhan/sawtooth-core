# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.5

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /project/sawtooth-core/sdk/examples/xo_cxx

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /project/sawtooth-core/sdk/examples/xo_cxx/build

# Include any dependencies generated for this target.
include CMakeFiles/xo_tp_cxx.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/xo_tp_cxx.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/xo_tp_cxx.dir/flags.make

CMakeFiles/xo_tp_cxx.dir/xo_transaction_processor.cpp.o: CMakeFiles/xo_tp_cxx.dir/flags.make
CMakeFiles/xo_tp_cxx.dir/xo_transaction_processor.cpp.o: ../xo_transaction_processor.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/project/sawtooth-core/sdk/examples/xo_cxx/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/xo_tp_cxx.dir/xo_transaction_processor.cpp.o"
	/usr/bin/c++   $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/xo_tp_cxx.dir/xo_transaction_processor.cpp.o -c /project/sawtooth-core/sdk/examples/xo_cxx/xo_transaction_processor.cpp

CMakeFiles/xo_tp_cxx.dir/xo_transaction_processor.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/xo_tp_cxx.dir/xo_transaction_processor.cpp.i"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /project/sawtooth-core/sdk/examples/xo_cxx/xo_transaction_processor.cpp > CMakeFiles/xo_tp_cxx.dir/xo_transaction_processor.cpp.i

CMakeFiles/xo_tp_cxx.dir/xo_transaction_processor.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/xo_tp_cxx.dir/xo_transaction_processor.cpp.s"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /project/sawtooth-core/sdk/examples/xo_cxx/xo_transaction_processor.cpp -o CMakeFiles/xo_tp_cxx.dir/xo_transaction_processor.cpp.s

CMakeFiles/xo_tp_cxx.dir/xo_transaction_processor.cpp.o.requires:

.PHONY : CMakeFiles/xo_tp_cxx.dir/xo_transaction_processor.cpp.o.requires

CMakeFiles/xo_tp_cxx.dir/xo_transaction_processor.cpp.o.provides: CMakeFiles/xo_tp_cxx.dir/xo_transaction_processor.cpp.o.requires
	$(MAKE) -f CMakeFiles/xo_tp_cxx.dir/build.make CMakeFiles/xo_tp_cxx.dir/xo_transaction_processor.cpp.o.provides.build
.PHONY : CMakeFiles/xo_tp_cxx.dir/xo_transaction_processor.cpp.o.provides

CMakeFiles/xo_tp_cxx.dir/xo_transaction_processor.cpp.o.provides.build: CMakeFiles/xo_tp_cxx.dir/xo_transaction_processor.cpp.o


CMakeFiles/xo_tp_cxx.dir/address_mapper.cpp.o: CMakeFiles/xo_tp_cxx.dir/flags.make
CMakeFiles/xo_tp_cxx.dir/address_mapper.cpp.o: ../address_mapper.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/project/sawtooth-core/sdk/examples/xo_cxx/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object CMakeFiles/xo_tp_cxx.dir/address_mapper.cpp.o"
	/usr/bin/c++   $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/xo_tp_cxx.dir/address_mapper.cpp.o -c /project/sawtooth-core/sdk/examples/xo_cxx/address_mapper.cpp

CMakeFiles/xo_tp_cxx.dir/address_mapper.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/xo_tp_cxx.dir/address_mapper.cpp.i"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /project/sawtooth-core/sdk/examples/xo_cxx/address_mapper.cpp > CMakeFiles/xo_tp_cxx.dir/address_mapper.cpp.i

CMakeFiles/xo_tp_cxx.dir/address_mapper.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/xo_tp_cxx.dir/address_mapper.cpp.s"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /project/sawtooth-core/sdk/examples/xo_cxx/address_mapper.cpp -o CMakeFiles/xo_tp_cxx.dir/address_mapper.cpp.s

CMakeFiles/xo_tp_cxx.dir/address_mapper.cpp.o.requires:

.PHONY : CMakeFiles/xo_tp_cxx.dir/address_mapper.cpp.o.requires

CMakeFiles/xo_tp_cxx.dir/address_mapper.cpp.o.provides: CMakeFiles/xo_tp_cxx.dir/address_mapper.cpp.o.requires
	$(MAKE) -f CMakeFiles/xo_tp_cxx.dir/build.make CMakeFiles/xo_tp_cxx.dir/address_mapper.cpp.o.provides.build
.PHONY : CMakeFiles/xo_tp_cxx.dir/address_mapper.cpp.o.provides

CMakeFiles/xo_tp_cxx.dir/address_mapper.cpp.o.provides.build: CMakeFiles/xo_tp_cxx.dir/address_mapper.cpp.o


# Object files for target xo_tp_cxx
xo_tp_cxx_OBJECTS = \
"CMakeFiles/xo_tp_cxx.dir/xo_transaction_processor.cpp.o" \
"CMakeFiles/xo_tp_cxx.dir/address_mapper.cpp.o"

# External object files for target xo_tp_cxx
xo_tp_cxx_EXTERNAL_OBJECTS =

bin/xo_tp_cxx: CMakeFiles/xo_tp_cxx.dir/xo_transaction_processor.cpp.o
bin/xo_tp_cxx: CMakeFiles/xo_tp_cxx.dir/address_mapper.cpp.o
bin/xo_tp_cxx: CMakeFiles/xo_tp_cxx.dir/build.make
bin/xo_tp_cxx: CMakeFiles/xo_tp_cxx.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/project/sawtooth-core/sdk/examples/xo_cxx/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Linking CXX executable bin/xo_tp_cxx"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/xo_tp_cxx.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/xo_tp_cxx.dir/build: bin/xo_tp_cxx

.PHONY : CMakeFiles/xo_tp_cxx.dir/build

CMakeFiles/xo_tp_cxx.dir/requires: CMakeFiles/xo_tp_cxx.dir/xo_transaction_processor.cpp.o.requires
CMakeFiles/xo_tp_cxx.dir/requires: CMakeFiles/xo_tp_cxx.dir/address_mapper.cpp.o.requires

.PHONY : CMakeFiles/xo_tp_cxx.dir/requires

CMakeFiles/xo_tp_cxx.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/xo_tp_cxx.dir/cmake_clean.cmake
.PHONY : CMakeFiles/xo_tp_cxx.dir/clean

CMakeFiles/xo_tp_cxx.dir/depend:
	cd /project/sawtooth-core/sdk/examples/xo_cxx/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /project/sawtooth-core/sdk/examples/xo_cxx /project/sawtooth-core/sdk/examples/xo_cxx /project/sawtooth-core/sdk/examples/xo_cxx/build /project/sawtooth-core/sdk/examples/xo_cxx/build /project/sawtooth-core/sdk/examples/xo_cxx/build/CMakeFiles/xo_tp_cxx.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/xo_tp_cxx.dir/depend

