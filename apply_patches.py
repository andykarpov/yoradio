from os.path import join, isfile

Import("env")

LIBDEPS_DIR = env['PROJECT_LIBDEPS_DIR']

patches = [
    [join("patches", "1-adafruit-gfx-glcdfont.patch"), join(LIBDEPS_DIR, "esp32dev", "Adafruit GFX Library", "glcdfont.c")],
]

for patch in patches:

    patch_file = patch[0]
    original_file = patch[1]
    patchflag_path = original_file + ".patching-done"

    # patch file only if we didn't do it before
    if not isfile(patchflag_path):
        assert isfile(original_file) and isfile(patch_file)
        env.Execute("patch \"%s\" < %s" % (original_file, patch_file))
        def _touch(path):
            with open(path, "w") as fp:
                fp.write("")
        env.Execute(lambda *args, **kwargs: _touch(patchflag_path))
