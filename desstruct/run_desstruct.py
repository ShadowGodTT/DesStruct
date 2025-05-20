import sys
import os
from pathlib import Path

# Add the current directory to Python path
current_dir = Path(__file__).parent
sys.path.append(str(current_dir))

# Import the app
from app import main

if __name__ == "__main__":
    # Set working directory to the executable's directory
    os.chdir(current_dir)
    main() 