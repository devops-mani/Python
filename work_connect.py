import os
import subprocess
import sys
import time
import platform
import getpass
import logging

# Set up logging
logging.basicConfig(filename='script.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Help text to display if no or invalid arguments are provided
help_text = """You need to pass an argument:
    -c              to connect to the remote desktop
    -d              to disconnect from the remote session
    -cal            to open Calculator
    -paint          to open MS Paint
    -rdp            to open Remote Desktop"""

# Check if at least one argument is passed to the script
if len(sys.argv) < 2:
    print(help_text)
    sys.exit(1)

# Function to connect
def connect():
    try:
        # Placeholder for connecting to remote desktop
        logging.info("Connecting to remote desktop...")
        print("Connecting to remote desktop...")
        # Example: subprocess.Popen(["your_command_here"])
    except Exception as e:
        logging.error(f"Failed to connect: {e}")
        print(f"Failed to connect: {e}")
        sys.exit(1)

# Function to disconnect
def disconnect():
    try:
        # Placeholder for disconnecting from remote session
        logging.info("Disconnecting from remote session...")
        print("Disconnecting from remote session...")
        # Example: subprocess.Popen(["your_command_here"])
    except Exception as e:
        logging.error(f"Failed to disconnect: {e}")
        print(f"Failed to disconnect: {e}")
        sys.exit(1)

# Function to open Calculator
def open_calculator():
    try:
        subprocess.Popen(["calc.exe"])
    except Exception as e:
        logging.error(f"Failed to open Calculator: {e}")
        print(f"Failed to open Calculator: {e}")
        sys.exit(1)

# Function to open MS Paint
def open_paint():
    try:
        subprocess.Popen(["mspaint.exe"])
    except Exception as e:
        logging.error(f"Failed to open MS Paint: {e}")
        print(f"Failed to open MS Paint: {e}")
        sys.exit(1)

# Function to open Remote Desktop
def open_rdp():
    try:
        subprocess.Popen(["mstsc.exe"])
    except Exception as e:
        logging.error(f"Failed to open Remote Desktop: {e}")
        print(f"Failed to open Remote Desktop: {e}")
        sys.exit(1)

# Function to get user confirmation
def get_confirmation():
    try:
        confirmation = input("Are you sure you want to continue? (y/n): ").strip().lower()
        if confirmation != 'y':
            logging.info("Operation cancelled by user.")
            print("Operation cancelled by user.")
            sys.exit(0)
    except KeyboardInterrupt:
        logging.info("Operation cancelled by user.")
        print("\nOperation cancelled by user.")
        sys.exit(0)

# Process the command line arguments
if sys.argv[1].lower() == "-c":
    get_confirmation()
    connect()
elif sys.argv[1].lower() == "-d":
    get_confirmation()
    disconnect()
elif sys.argv[1].lower() == "-cal":
    open_calculator()
elif sys.argv[1].lower() == "-paint":
    open_paint()
elif sys.argv[1].lower() == "-rdp":
    open_rdp()
else:
    print(f"Unknown option - {help_text}")
    sys.exit(1)
