"""
Root entrypoint for Streamlit Community Cloud deployment.
Forwards directly to verdant_balcony/app.py.
"""
import sys
import os

# Add verdant_balcony directory to sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
sub_dir = os.path.join(current_dir, "verdant_balcony")
if sub_dir not in sys.path:
    sys.path.insert(0, sub_dir)

# Execute verdant_balcony/app.py
target_app = os.path.join(sub_dir, "app.py")
with open(target_app, "r", encoding="utf-8") as f:
    code = f.read()

exec(compile(code, target_app, "exec"))
