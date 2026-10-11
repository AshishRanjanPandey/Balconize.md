import subprocess
import sys
import os

if __name__ == "__main__":
    app_path = os.path.join(os.path.dirname(__file__), "verdant_balcony", "app.py")
    cmd = [sys.executable, "-m", "streamlit", "run", app_path]
    print(f"🌱 Launching Balconize: {' '.join(cmd)}")
    subprocess.run(cmd)
