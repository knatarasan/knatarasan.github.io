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

### 13JUL2025
- Got inspired from a friend about how AI would influence generic robotics.
- Spoken with Mukilan by deciding to start from robotic arm
### 02AUG2025 
- seriously started 
### 03AUG2025

#### software
- stack 
  - started with ubuntu 22.04 | ros2 humble - rviz2 - moveit2 - gazebo - installed on lenova pc all up and working until moveit2
  - Moved to ubuntu 24.04 | ros2 jozzy (to go ubuntu 24.04, since rpi 5 needs 24.04)
  - migrated from ubuntu 22.04 to 24.04
#### hardware
Buy (costs around 25K ) vs build ( possible to build below 7k)
- ##### Fabrication
  - 3D printing (Tried  few prints from community library , staff was very helpful)
    - printers : FDM vs SLA
    - materials 
      - PLA - versatile
      - PETG - intermitant 
      - Nylon - strong

### 08AUG2025 
#### SERVO MOTORS
- They are heart of a robotic arm
- Dynamixel is the leading supplier of stronger precise robotic arm

### 11AUG2025


- #### Servo motors

#### 14AUG2025
- SOLDERING
  - After few mistakes, followed a nice tutorial and got hold of it.![alt text]({{ site.image_base }}/2025-07-06/solder_practice_1.jpeg)
  - ![image info]({{ site.image_base }}/2025-07-06/solder_INA3221.jpeg)
  - Lessons learnt :  
    - Soldering is mini welding you melt metal and pour very small in quantity though. Use safety glass , there is a possibility of molten metal spill somewhere. Use right soldering tip. 
    - Don’t keep lead on soldering iron,instead heat the wire to be soldered and keep lead there and  let it to melt and nicely settle.
- BASIC ELECTRONICS
  - Yes it is  v=I R, P= I^2 R
  - Learnt internals of a potentiometer by burning it, was playing around with a circuit , 6v -> 10K (var res ) --> motor (6v rated) --> .3A
    - When I increased resistance to 4K , current is bellow 0.05A , so tried increasing volt to 10V then 20V. still current is low, now reduced res to below 1K , saw fume from var res.
  - Got an idea between current and Torque on Motor
  - - ![image info]({{site.image_base}}/2025-07-06/servo-motor-paly-around.jpeg)

#### 15AUG2025
- Set up 3D Prusa core get the sample printing done

#### 16AUG2025
- Tried with Nylon and failed print
- Studied papers on imimation Learning and ALOHA 

#### 18AUG2025
- 3D printing completed for v1.
- ![image info]({{site.image_base}}/2025-07-06/3d-printed-arm-parts.jpeg)
- Need different screws explored different screw types, needed m3 12mm and few shaft screws. Found Dave hardware has all the required screws.

#### 19AUG2025
- Got right screws, completed clipper assembly and tested.
  - Has to configure clipper servo between 90 to 0 degree. ( controlled from the code)
  - Yet the servo takes .35A when it is at 90 deg position. ( has to be troubleshoot)
- Assembled arm and wrist servo screwed in after little hack on servo horn
#### 20AUG2025
- Tried test print on ABS , not able to raise chamber temp beyond 35, later found to close ventilation lid
#### 21AUG2025
- Prepared Lenova T14s on Ubuntu and tried installing ROS2
- Discussed with mechanical engg friends about  Solidworks and Pro-E, spoken with CAD designers
#### 22AUG2025
- Successfully printed ABS, previous failure print is due to in sufficient chamber temperature
- Performed various tests

| Material | Break Test | Falme test | Printability |
| -------- | ---------- | ---------- | ------------ |
| PLA      | Weak       | Medium     | Easy         |
| ABS      | Medium     | Weak       | Medium       |
| Nylon    | Strong     | Strong     | hard         |

