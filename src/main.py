import argparse
import logging
import sys

def main():
    parser = argparse.ArgumentParser(description="Robotic Arm Sorting System")
    parser.add_argument("--simulate", action="store_true", help="Run in simulation (dry-run) mode")
    parser.add_argument("--calibrate", action="store_true", help="Run system calibration")
    parser.add_argument("--execute", action="store_true", help="Run on physical hardware")
    
    args = parser.parse_args()
    
    logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

    if args.simulate:
        logging.info("Starting in SIMULATION mode.")
        from src.simulation.simulator import Simulator
        import time
        sim = Simulator()
        sim.connect()
        try:
            # Dummy test loop for dry-run
            sim.home()
            time.sleep(1)
            sim.move_to(100, 100, 50)
            time.sleep(1)
            sim.set_gripper(1)
            time.sleep(1)
        except KeyboardInterrupt:
            logging.info("Simulation interrupted.")
        finally:
            sim.disconnect()
    elif args.calibrate:
        logging.info("Starting CALIBRATION sequence.")
        # TODO: Launch calibration
    elif args.execute:
        logging.info("Starting PHYSICAL EXECUTION.")
        # TODO: Launch physical control loop
    else:
        parser.print_help()
        sys.exit(1)

if __name__ == "__main__":
    main()
