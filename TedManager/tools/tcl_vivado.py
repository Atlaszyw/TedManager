import os


def tcl_add_incdir(dir_path, output_folder):
    tcl_script = os.path.join(output_folder, "add_include_dirs.tcl")
    with open(tcl_script, "a") as f:
        f.write(f"add_files -norecurse -scan_for_includes {dir_path}\n")
