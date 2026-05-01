from .robot_arm_sim import RobotArmSim

class Simulator:
    def __init__(self):
        self.is_running = False
        self.current_pos = (0, 0, 0)
        self.gripper_state = 0
        self.sim = None

    def connect(self):
        self.is_running = True
        self.sim = RobotArmSim()
        print("[SIMULATOR] Environment initialized.")

    def disconnect(self):
        if self.sim:
            self.sim.close()
        self.is_running = False
        print("[SIMULATOR] Environment closed.")

    def move_to(self, x: float, y: float, z: float):
        if not self.is_running:
            return "ERR NOT RUNNING"
        self.current_pos = (x, y, z)
        print(f"[SIMULATOR] Moving to {x}, {y}, {z}")
        if self.sim:
            self.sim.move_to(x, y, z)
        return "OK"

    def set_gripper(self, state: int):
        self.gripper_state = state
        print(f"[SIMULATOR] Gripper set to {state}")
        return "OK"

    def home(self):
        self.move_to(0, 0, 0)
        print("[SIMULATOR] Homing complete.")
        return "OK"

    def emergency_stop(self):
        print("[SIMULATOR] EMERGENCY STOP TRIGGERED!")
        return "OK"
