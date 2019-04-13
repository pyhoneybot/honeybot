cmake_minimum_required(VERSION 3.13)
project(HoneyGUI)

include(FindPkgConfig)
pkg_check_modules(GTKMM gtkmm-3.0 REQUIRED)
include_directories(${GTKMM_INCLUDE_DIRS})

set(CMAKE_CXX_STANDARD 14)

add_executable(HoneyGUI main.cpp guiBase.cpp guiBase.h optionList.cpp optionList.h optionDisplay.cpp optionDisplay.h)
target_link_libraries(${PROJECT_NAME} ${GTKMM_LIBRARIES})