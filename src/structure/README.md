# 🏗️ Structure & Mechanics Team (Team 5)

## 🎯 Objectives
- Build and assemble the physical 4-DOF arm.
- Maintain the URDF model (dimensions, joint limits, link lengths).
- Physical calibration of servo offsets.

## 📁 Required Deliverables
1. `robot_description.urdf`: The source of truth for all link lengths and joint centers.
2. `offsets.json`: Calibration values to convert "0 degrees" to actual servo positions.

## 🛠 Integration Contact
The Structure team provides the `link_lengths` used by the **Kinematics Team** for its IK calculations.
