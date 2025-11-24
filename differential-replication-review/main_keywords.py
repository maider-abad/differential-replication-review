# main.py
import subprocess

def main():
    print("Executing keywords_graph.py...")
    subprocess.run(["python", "src_keywords/keywords_graph.py"])

    print("\Executing keywords_analysis.py...")
    subprocess.run(["python", "src_keywords/keywords_analysis.py"])

if __name__ == "__main__":
    main()
