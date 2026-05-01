import argparse
import logging
import sys

# Example Imports (Teams will implement these)
# from src.vision.detector import ObjectDetector
# from src.kinematics.engine import IKSolver
# from src.embedded.bridge import SerialBridge

def main():
    parser = argparse.ArgumentParser(description="Robotic Arm Sorting System - Integration Entry")
    parser.add_argument("--simulate", action="store_true", help="Run in simulation mode")
    parser.add_argument("--execute", action="store_true", help="Run on physical hardware")
    
    args = parser.parse_args()
    
    logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

    if args.simulate:
        logging.info("Starting System in SIMULATION mode...")
        # TODO: Initialize Vision and Kinematics Simulation
    elif args.execute:
        logging.info("Starting System in PHYSICAL mode...")
        # TODO: Initialize Vision, Kinematics, and Embedded Bridge
    else:
        parser.print_help()
        sys.exit(1)

if __name__ == "__main__":
    main()
