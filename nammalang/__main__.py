import sys
from .interpreter import run_file

def main():
    if len(sys.argv) < 2:
        print("[❌] Please provide a .nml file to run.")
        sys.exit(1)
    run_file(sys.argv[1])

if __name__ == "__main__":
    main()
