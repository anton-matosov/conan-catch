"""Conan recipe for Catch
"""
from conans import ConanFile
from conans.tools import download
from conans.tools import check_md5


class CatchConan(ConanFile):
    """Download Catch Cpp, build and create package
    """
    name = "Catch"
    version = "1.9.5"
    generators = "cmake"
    url = "https://github.com/uilianries/conan-catch"
    author = "Uilian Ries <uilianries@gmail.com>"
    license = "Boost"
    description = "A modern, C++-native, header-only, framework for unit-tests, TDD and BDD"

    def source(self):
        header_name = "catch.hpp"
        download("https://github.com/philsquared/Catch/releases/download/v%s/%s" % (self.version, header_name), header_name)
        check_md5(header_name, "de513bbe3cfff90b186c85273aab13ec")

    def package(self):
        self.copy(pattern="catch.hpp", dst="include")
