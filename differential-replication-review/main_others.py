# main.py
import subprocess

def main():
    print("Executing polar_plots.py...")
    subprocess.run(["python", "other_graphs/polar_plots.py"])

    print("\Executing decision_tree.py...")
    subprocess.run(["python", "other_graphs/decision_tree.py"])

if __name__ == "__main__":
    main()
