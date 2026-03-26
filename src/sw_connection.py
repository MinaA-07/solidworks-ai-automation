import win32com.client
import sys

def connect_to_solidworks():
    """
    Connects to a running SolidWorks instance.
    SolidWorks MUST be open before running this script.
    """
    try:
        sw_app = win32com.client.Dispatch("SldWorks.Application")
        sw_app.Visible = True
        version = sw_app.RevisionNumber
        print(f"Successfully connected to SolidWorks!")
        print(f"SolidWorks version: {version}")
        return sw_app
    except Exception as e:
        print(f"Failed to connect to SolidWorks.")
        print(f"Error: {e}")
        print("Make sure SolidWorks is open before running this script.")
        return None

if __name__ == "__main__":
    app = connect_to_solidworks()
    if app is None:
        sys.exit(1)