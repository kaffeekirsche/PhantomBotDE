# Copyright (C) 2016-2023 phantombot.github.io/PhantomBot
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import copy
import os

def parse_file(lines):
    newlines = []
    for line in lines:
        if not line.strip().removeprefix("<!-- ").startswith("Generated by javadoc"):
            newlines.append(line)
    return newlines

for subdir, dirs, files in os.walk("./dist/javadoc"):
    for fname in files:
        fpath = subdir + os.sep + fname
        with open(fpath, encoding="utf8") as jd_file:
            lines = parse_file([line.rstrip('\n') for line in jd_file])
        with open(fpath, "w", encoding="utf8") as jd_file:
            jd_file.writelines(lines)
