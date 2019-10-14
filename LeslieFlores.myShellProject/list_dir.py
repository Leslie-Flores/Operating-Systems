# Leslie Flores - this is where the directory items are listed off

def list_dir(path):
    try:
        os.listdir(os.path.abspath(path))
    except Exception:
        print("ld: no files in directory found: {}".format(path))
