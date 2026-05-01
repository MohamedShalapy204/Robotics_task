# 📐 Kinematics & Simulation Team (Team 2)

## 🎯 Objectives
- Implement **Inverse Kinematics (IK)** logic for the 4-DOF arm.
- Maintain a virtual representation using PyBullet or Matplotlib.
- Trajectory planning (moving smoothly between points).

## 📁 Required Deliverables
1. `engine.py`: The IK solver that takes `(x, y, z)` and returns `[J1, J2, J3, J4]` angles.
2. `simulator.py`: A visual tool to test movements before running on physical hardware.

## 🛠 Integration Contact
The Kinematics team receives `(x, y)` from the **Vision Team** and outputs `angles` to the **Embedded Team**.
