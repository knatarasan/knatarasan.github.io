---
layout: post
title: "Robotic Arm"
tags: [wip]
---

{% if page.tags contains "wip" %}

<div style="background:#ffeeba; border-left:4px solid #f0ad4e; padding:1em; margin-bottom:2em;">
  🚧 This post is a Work In Progress — feel free to share feedback.
</div>
{% endif %}

- Got inspired from a friend about how AI would influence generic robotics. (13JUL2025)
- Spoken with Mukilan by deciding to start from robotic arm
- 02AUG2025 : seriously started 
### software
- stack 
  - started with ubuntu 22.04 | ros2 humble - rviz2 - moveit2 - gazebo - installed on lenova pc all up and working until moveit2
  - Moved to ubuntu 24.04 | ros2 jozzy (to go ubuntu 24.04, since rpi 5 needs 24.04)
  - migrated from ubuntu 22.04 to 24.04
### hardware
Buy (costs around 25K ) vs build ( possible to build below 7k)
- #### Fabrication
  - 3D printing (Tried  few prints from community library , staff was very helpful)
    - printers : FDM vs SLA
    - materials 
      - PLA - versatile
      - PETG - intermitant 
      - Nylon - strong
- #### Servo motors
  <p>They are heart of a robotic arm</p>
  08AUG2025 to 11AUG : Dynamixel


