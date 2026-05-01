class PathPlanner:
    def __init__(self, robot_interface):
        self.robot = robot_interface

    def plan_and_execute_sort(self, obj_coords, bin_coords):
        # 1. Move to object above
        self.robot.move_to(obj_coords[0], obj_coords[1], obj_coords[2] + 50)
        # 2. Lower to object
        self.robot.move_to(obj_coords[0], obj_coords[1], obj_coords[2])
        # 3. Grasp
        self.robot.set_gripper(1)
        # 4. Lift
        self.robot.move_to(obj_coords[0], obj_coords[1], obj_coords[2] + 100)
        # 5. Move above bin
        self.robot.move_to(bin_coords[0], bin_coords[1], bin_coords[2] + 100)
        # 6. Release
        self.robot.set_gripper(0)
        # 7. Home
        self.robot.home()

    def run_homing_sequence(self):
        self.robot.home()
