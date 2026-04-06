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
        sketch_mgr.InsertSketch(False)
        print("Sketch Complete")

        feature_mgr.FeatureExtrusion(
            False,   # single ended
            False,   # flip side to cut
            False,   # flip direction
            0,       # type (blind)
            0,       # type dir2
            height,  # depth
            height,  # depth dir2
            False,   # draft
            False,   # draft outward
            False,   # draft dir2
            False,   # draft outward dir2
            0.0,     # draft angle
            0.0,     # draft angle dir2
            False,   # thin feature
            0.0,     # thin thickness 1
            0.0,     # thin thickness 2
            0,       # thin type
            True,    # merge result
            False,   # use feature scope
            True     # auto select
        )
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