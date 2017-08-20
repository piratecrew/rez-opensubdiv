CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(ExternalProject)

rez_find_packages(PREFIX pkgs AUTO)

set(url_opensubdiv https://github.com/PixarAnimationStudios/OpenSubdiv/archive/v${OPENSUBDIV_MAJOR_VERSION}_${OPENSUBDIV_MINOR_VERSION}_${OPENSUBDIV_PATCH_VERSION}.zip)
set(opensubdiv_tag master)

if(${REZ_BUILD_INSTALL})
    set(install_cmd make install ${make_args})
else()
    set(install_cmd "")
endif()

set(CMAKE_ARGS
    -DNO_TBB=ON
    -DNO_EXAMPLES=ON
    -DNO_TUTORIALS=ON
    -DNO_REGRESSION=ON
    -DNO_DOC=ON
    -DNO_OMP=ON
    -DNO_CUDA=ON
    -DNO_OPENCL=ON
    -DNO_DX=ON
    -DNO_TESTS=ON
    -DZLIB_ROOT=$ENV{REZ_ZLIB_ROOT}
    -DGLEW_LOCATION=$ENV{REZ_GLEW_ROOT}
    -DPTEX_LOCATION=$ENV{REZ_PTEX_ROOT}
)

ExternalProject_add(
    opensubdiv
    URL ${url_opensubdiv}
    PREFIX opensubdiv
    CMAKE_ARGS -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX} ${CMAKE_ARGS}
    INSTALL_COMMAND "${install_cmd}"
    ALWAYS 1
)

install(
    FILES cmake/opensubdiv.cmake
    DESTINATION cmake
)

