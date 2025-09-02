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
- Experimented diff material on flame tests
 <iframe width="320" height="240"
   src="https://www.youtube.com/embed/xclQgvrHxgs" title="youtube video" frameborder="0"
   allow="accelerometer;autoplay;clipboard-write; encrypted-media; gyroscope;picture-in-picture" allowfullscreen>
</iframe>

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

#### 23AUG2025
- Was playing around CAD on fusion 360

#### 24AUG2025
- Assembling of Arm v1 (end to end)
  - was teaching how to solder to my buddy
  - Mechanical assembly became similar, attach servo horn add screws
  - Managing cables between arduino and servos are a bit tricky.
  - Schematic diagram of Servos with Arduino was useful
  - 5V supply receiver was easy to inserted in
  - Arduino can be screwed in easily.
  - A junction point to connect 5 diff servos was a bit tricky on soldering.
  - Like 70% of assembling work completed, deffinitely got good idea on ARM assembly.

#### 25AUG2025
  - Done with the complex multi servo board soldering ![img](https://roboticchef.github.io/assets/images/2025-08-26/multi_servo_junction_1.jpg )
  - Tried a smoke test on integrated hardware

### 26AUG2025
  - Got the blog set up.

### 27AGU2025
  - Full assembly had been completed, took little over time as I try re-soldering a broken connection with thin wire (not a best practice soldering) 
  - Felt exicted after the test, the arm was made from STLs --> print and fully assembled.

### 28AUG2025
  - Printed parts for franka style arm and received supplies on Dynamixel version
  - Wired components of Dyanamixel motor
    <div class="mermaid">
    flowchart LR
    Ub[Ubuntu] --> U2[U2D2]
    U2 --> X28[XL-330-M288T]
    PW[Power Hub 5V] --> U2
    </div>
    - Tested using Dynamixel Wizard
  <iframe width="420" height="340"
   src="https://youtube.com/embed/Zqv_ZWRVS3g" title="youtube video" frameborder="0"
   allow="accelerometer;autoplay;clipboard-write; encrypted-media; gyroscope;picture-in-picture" allowfullscreen>
</iframe>


### 29AUG2025
  - Compared all types of  Dynamixel motors ([Check this link](https://www.generationrobots.com/blog/en/how-to-choose-the-right-dynamixel-servomotor/?srsltid=AfmBOoreEwQXZ8Bzst8QaPHZIeNRUmCoAXRwl590S7pWJS68PKojT1sB)), realized predominant diff between XL ( low cost ) and XM ( medium range) motors are only torque. So thearitically once you build an arm with XL motors with same set up with minimal config change you should able to move to XM series.
  

### 30AUG2025
 - Trying to understand Force, Torque and its relations. 
  ![image info]({{ site.image_base }}/2025-07-06/dynamixel-actuator-servo-schematics.jpg)

### 31AUG2025
  - Explored wiring for Daisy chaining in Dynamixel , [this link](https://www.robotis.us/robotis-ir-pr-blog/the-ultimate-dynamixel-daisy-chaining-guide/?srsltid=AfmBOorReUg9bSZIWDpdDNwT5AzACWsFEexM5VvXoQpHtAZUiL4PoQWF) gave nice pointers for configuration

### 01SEP2025
  - Deep dive on Torque, explored how the "REQUIRED TORQUE" changes with distance from neutral axis. When you imagine a roatatable shaft from its cross section (a circle), the center is neutral axis. The REQUIRED TORQUE keep increases when you move away from the center.
    - Torque = r . F
      - i.e Torques is multiply of r (distance from fulcrum ) and Force ( can be imagined in lb)
  - With these explorations envisioning a robotic arm with servo motors with reducing torque from the base. Planning to explore further.
  - Figured out how to assemble and build a basic Franka style arm with the motors in hand.
  - Refer this [Dynamixel link](https://emanual.robotis.com/docs/en/dxl/x/) for a consolidated list