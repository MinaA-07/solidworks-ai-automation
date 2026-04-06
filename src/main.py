import win32com.client
from src.llm_parser import parse_cad_command
from src.cad_actions import create_part

def main():
    sw_app = win32com.client.Dispatch("SldWorks.Application")
    print("Connected to Solidworks")
    user_input = input("Enter a CAD command")
    print(f"You entered: {user_input}")
    cad_data = parse_cad_command(user_input)
    if (cad_data == None):
        print("Could not understand command")
        return 
    else:
        print(f"Parsed:{cad_data}")
    create_part(sw_app, cad_data)
    print("Done! Check Solidworks")

if __name__ == "__main__":
    main()