import win32com.client
import time


def create_part(sw_app, cad_data):
    template = "C:\\ProgramData\\SOLIDWORKS\\SOLIDWORKS 2025\\templates\\Part.prtdot"
    sw_app.NewDocument(template, 0, 0, 0)
    time.sleep(4)
    model = sw_app.ActiveDoc

    if model is None:
        print("Failed to get active document")
        return

    print("SolidWorks part created!!")

    sketch_mgr = model.SketchManager
    feature_mgr = model.FeatureManager
    print("Ready to Sketch!!")

    shape = cad_data["shape"]
    height = cad_data["height"]
    print(f"Building {shape} with height {height}")

    if shape == "cylinder":
        radius = cad_data["diameter"] / 2
        sketch_mgr.InsertSketch(True)
        sketch_mgr.CreateCircle(0, 0, 0, radius, 0, 0)
        model.EditSketchOrSingleSketchFeature()
        time.sleep(1)
        print("Sketch Complete")

        extrusion = feature_mgr.FeatureExtrusion(
            False,
            False,
            False,
            0,
            0,
            height,
            height,
            False,
            False,
            False,
            False,
            0.0,
            0.0,
            False,
            0.0,
            0.0,
            0,
            True,
            False,
            True
        )

        if extrusion is None:
            print("Extrusion failed - returned None")
        else:
            print("Extrusion succeeded!")

        print("Cylinder Complete")
    else:
        print(f"Shape {shape} not supported yet")


if __name__ == "__main__":
    sw_app = win32com.client.Dispatch("SldWorks.Application")
    test_data = {
        'shape': 'cylinder',
        'diameter': 0.05,
        'height': 0.1
    }
    create_part(sw_app, test_data)