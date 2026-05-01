import pybullet as p
import pybullet_data
import time

class RobotArmSim:
    def __init__(self):
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0, 0, -10)
        self.planeId = p.loadURDF("plane.urdf")
        # In a real scenario, we'd load the specific robot URDF. 
        # Using a generic robot for the simulation stub.
        self.robotId = p.loadURDF("kuka_iiwa/model.urdf", [0, 0, 0])
        
    def move_to(self, x, y, z):
        # Calculate Inverse Kinematics
        joint_poses = p.calculateInverseKinematics(self.robotId, 6, [x/1000.0, y/1000.0, z/1000.0])
        for i in range(len(joint_poses)):
            p.setJointMotorControl2(bodyIndex=self.robotId, 
                                    jointIndex=i, 
                                    controlMode=p.POSITION_CONTROL, 
                                    targetPosition=joint_poses[i])
        p.stepSimulation()
        time.sleep(0.01)

    def close(self):
        p.disconnect()
