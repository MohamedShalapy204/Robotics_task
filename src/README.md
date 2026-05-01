# Source Code Architecture

Welcome to the Robotics Arm Object Sorting project codebase. To maintain clarity across our 5 teams, the `src/` directory is organized by subsystem.

## 📁 Directory Structure & Responsibilities

### 1. `src/vision/` (Computer Vision Team)
- **Goal**: Detect balls and provide their coordinates.
- **Key Files**: `detector.py`, `calibration.py`.

### 2. `src/kinematics/` (Kinematics & Simulation Team)
- **Goal**: Calculate joint angles (IK) and maintain the virtual simulation.
- **Key Files**: `robot_arm_sim.py`, `planner.py`, `simulator.py`.

### 3. `src/embedded/` (Embedded Team)
- **Goal**: Handle communication between Python and the Arduino hardware.
- **Key Files**: `firmware.ino` (Arduino C++ code), `serial_handler.py`.

### 4. `src/power/` (Power Supply Team)
- **Goal**: Safety monitoring and power budget configuration.
- **Key Files**: `safety.py`, `specs.json`.

### 5. `src/structure/` (Structure Team)
- **Goal**: Define the physical dimensions and URDF model of the robot.
- **Key Files**: `arm_model.urdf`, `entities.py`.

### 6. `src/integration/` (Shared Integration)
- **Goal**: The "glue" that binds all subsystems together into a single running application.
- **Key Files**: `main_integration.py`, `settings.py`.

---

## 🛠 Rules for Development
1. **Stay in your lane**: Only modify files within your team's folder.
2. **Interface clearly**: If you need to change how your subsystem talks to another, discuss it in the `integration` meeting first.
3. **No direct hardware access**: All hardware communication must go through the `embedded/serial_handler.py`.
