# Leslie Flores - this is where the directory changes either back or forth

def change_dir(path):
    try:
        os.chdir(os.path.abspath(path))
    except Exception:
        print("cd: no such file or directory found: {}".format(path))
