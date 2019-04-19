cmake_minimum_required(VERSION 3.13)
project(HoneyGUI)

include(FindPkgConfig)
pkg_check_modules(GTKMM gtkmm-3.0 REQUIRED)
include_directories(${GTKMM_INCLUDE_DIRS})

set(CMAKE_CXX_STANDARD 14)

add_executable(HoneyGUI main.cpp guiBase.cpp guiBase.h controlDisplay.cpp controlDisplay.h configDisplay.cpp configDisplay.h pluginDisplay.cpp pluginDisplay.h)
target_link_libraries(${PROJECT_NAME} ${GTKMM_LIBRARIES})