# 🤝 Integration Team (The Glue)

## 🎯 Objectives
- Connect all subsystems into a single executable application.
- Handle high-level logic (e.g., "If Vision sees Red, move Kinematics to Bin A").
- Manage system-wide configuration and logging.

## 📁 Required Deliverables
1. `main_integration.py`: The entry point for the entire project.
2. `config.py`: Shared settings and constants (link lengths, COM ports, baud rates).

## 🛠 Workflow
1. Import the `ObjectDetector` from `src/vision/`.
2. Import the `IKSolver` from `src/kinematics/`.
3. Import the `SerialBridge` from `src/embedded/`.
4. Run the main control loop.
