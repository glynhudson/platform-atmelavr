# Copyright 2014-present Ivan Kravets <me@ikravets.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Simba

Simba is an RTOS and build framework. It aims to make embedded
programming easy and portable.

http://simba-os.readthedocs.org

"""

from os.path import join

from SCons.Script import DefaultEnvironment, SConscript

env = DefaultEnvironment()

env.Replace(
    PLATFORMFW_DIR=env.DevPlatform().get_package_dir("framework-simba")
)

SConscript(
    [env.subst(join("$PLATFORMFW_DIR", "make", "platformio.sconscript"))])
