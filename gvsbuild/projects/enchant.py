#  Copyright (C) 2016 The Gvsbuild Authors
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, see <http://www.gnu.org/licenses/>.

from pathlib import Path

from gvsbuild.utils.base_expanders import Tarball
from gvsbuild.utils.base_project import Project, project_add
from gvsbuild.utils.utils import convert_to_msys


@project_add
class Enchant(Tarball, Project):
    def __init__(self):
        Project.__init__(
            self,
            "enchant",
            version="2.8.19",
            repository="https://github.com/rrthomas/enchant",
            archive_url="https://github.com/rrthomas/enchant/releases/download/v{version}/enchant-{version}.tar.gz",
            hash="8e7f6cb0c3b79be3146eb3ab93650484adbc59dae5f2c1958fde557080ba678c",
            dependencies=["glib", "msys2", "pkgconf"],
        )

    def build(self):
        msys_path = Project.get_tool_path("msys2")
        bash = str(Path(msys_path) / "bash")
        prefix = convert_to_msys(self.builder.gtk_dir)
        host = "x86_64-w64-mingw32" if self.builder.x64 else "i686-w64-mingw32"

        self.exec_vs(
            [
                bash,
                "./configure",
                f"--prefix={prefix}",
                f"--host={host}",
                "--disable-static",
                "--without-aspell",
                "--without-hspell",
                "--without-hunspell",
                "--without-nuspell",
                "--without-voikko",
                "--without-zemberek",
                "--with-winspell",
                "CC=cl",
                "CXX=cl",
            ],
            add_path=msys_path,
        )
        self.exec_vs(["make", "install"], add_path=msys_path)
        self.install(r".\COPYING.LIB share\doc\enchant")
