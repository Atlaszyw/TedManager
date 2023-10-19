import os
import shutil


def _filelistpick(logger, filelist, outputsrcdir, outputincdir, relapath):
    with open(filelist, "r") as f:
        logger.debug("Read filelist done")
        for line in f:
            if relapath is not None:
                line = line.replace(relapath, ".")
            line = line.strip()
            logger.debug("read: %s", line)

            if line.startswith("//") or line.isspace():
                logger.debug("Processing Comment line: pass")
                continue

            elif line.startswith("-f"):
                _, sub_filelist = line.split()
                logger.debug("Processing abs path filelist sta: %s", sub_filelist)
                _filelistpick(
                    logger, sub_filelist, outputsrcdir, outputincdir, relapath
                )
                logger.debug("Processing abs path filelist end: %s", sub_filelist)

            elif line.startswith("-F"):
                pass
                # _, sub_filelist = line.split()

            elif line.startswith("+incdir+"):
                incdir_path = line[8:]
                logger.debug("Processing incdir: %s", incdir_path)
                relative_path = os.path.relpath(incdir_path, os.curdir)
                incdestdir_path = os.path.abspath(
                    os.path.join(outputincdir, relative_path)
                )
                if not os.path.exists(incdestdir_path):
                    shutil.copytree(
                        os.path.abspath(incdir_path),
                        incdestdir_path,
                    )
                    logger.debug("Processing incdir: %s", incdir_path)
                else:
                    logger.debug(
                        f"Processing incdir: {incdir_path}, folder already exists"
                    )
                # tcl_add_incdir(relative_path, output_folder)

            elif line.endswith((".v", ".sv", "vhdl")):
                rtl_filepath = line
                logger.debug("Processing rtl file: %s", rtl_filepath)

                output_path = os.path.join(outputsrcdir, rtl_filepath)
                if not os.path.exists(os.path.dirname(output_path)):
                    os.makedirs(os.path.dirname(output_path))
                shutil.copy2(rtl_filepath, output_path, follow_symlinks=False)

            elif line.endswith((".svh", ".vh")):
                rtlh_filepath = line
                logger.debug(f"Processing rtl header file: {rtlh_filepath}")

                output_path = os.path.join(
                    outputincdir, os.path.basename(rtlh_filepath)
                )
                shutil.copy2(rtlh_filepath, output_path, follow_symlinks=False)


def filelistpick(args, logger):
    os.makedirs(args.outputdir, exist_ok=True)
    outputincdir = args.outputdir + "/inc"
    outputsrcdir = args.outputdir + "/src"
    os.makedirs(outputincdir, exist_ok=True)
    os.makedirs(outputsrcdir, exist_ok=True)
    _filelistpick(logger, args.filelist, outputsrcdir, outputincdir, args.relapath)
