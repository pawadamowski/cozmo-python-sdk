#!/usr/bin/env python3

# Copyright (c) 2017 Anki, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License in the file LICENSE.txt or at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

'''TODO
'''

import time

import cozmo
from cozmo.objects import CustomObjectMarkers, CustomObjectTypes


def custom_objects(robot: cozmo.robot.Robot):

    custom_object = robot.world.define_custom_cube(CustomObjectTypes.CustomType02,
                                                  CustomObjectMarkers.Diamonds2,
                                                  100,
                                                  90, 90, True)

    custom_object = robot.world.define_custom_wall(CustomObjectTypes.CustomType00,
                                                  CustomObjectMarkers.Circles2,
                                                  100, 100,
                                                  90, 90, True)

    custom_object = robot.world.define_custom_box(CustomObjectTypes.CustomType01,
                                                  CustomObjectMarkers.Hexagons2, CustomObjectMarkers.Circles3,    # front back
                                                  CustomObjectMarkers.Circles4, CustomObjectMarkers.Circles5,     # top bottom
                                                  CustomObjectMarkers.Triangles2, CustomObjectMarkers.Triangles3, # left right
                                                  100, 100, 100,
                                                  90, 90, True)

    print("Press CTRL-C to quit")
    while True:
        time.sleep(.1)


cozmo.run_program(custom_objects, use_viewer=True, force_viewer_on_top=True)
