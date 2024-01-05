import sys
import bpy
import argparse
import os


class ArgumentParserForBlender(argparse.ArgumentParser):
    """
    This class is identical to its superclass, except for the parse_args
    method (see docstring). It resolves the ambiguity generated when calling
    Blender from the CLI with a python script, and both Blender and the script
    have arguments. E.g., the following call will make Blender crash because
    it will try to process the script's -a and -b flags:

    To bypass this issue this class uses the fact that Blender will ignore all
    arguments given after a double-dash ('--'). The approach is that all
    arguments before '--' go to Blender, arguments after go to the script.
    The following calls work fine:
    """

    def _get_argv_after_doubledash(self):
        """
        Given the sys.argv as a list of strings, this method returns the
        sublist right after the '--' element (if present, otherwise returns
        an empty list).
        """
        try:
            idx = sys.argv.index("--")
            return sys.argv[idx+1:] # the list after '--'
        except ValueError as e: # '--' not in the list:
            return []

    # overrides superclass
    def parse_args(self):
        """
        This method is expected to behave identically as in the superclass,
        except that the sys.argv list will be pre-processed using
        _get_argv_after_doubledash before. See the docstring of the class for
        usage examples and details.
        """
        return super().parse_args(args=self._get_argv_after_doubledash())


# Parse additional arguments using argparse
# render_path, template_path, text
parser = ArgumentParserForBlender()
parser.add_argument("--render_path", type=str, help="Additional argument for your script")
parser.add_argument("--template_path", type=str, help="Additional argument for your script")
parser.add_argument("--text", type=str, help="Additional argument for your script")
args = parser.parse_args()
print(args)

render_path = args.render_path
template_path = args.template_path
text = args.text

# Open the Blender file
bpy.ops.wm.open_mainfile(filepath=template_path)

# modify text
text_scene = bpy.context.scene.objects['text']
text_scene.data.body = text

print("RENDERING IMAGE...")

scene = bpy.context.scene
scene.frame_start = 1  # Set the start frame of the animation
scene.frame_end = 60  # Set the end frame of the animation
scene.render.image_settings.file_format = "PNG"
# scene.render.filepath = "./renders/test_"
scene.render.filepath = os.path.join(render_path, "test.png")
bpy.ops.render.render(write_still=1)
# bpy.ops.render.render(animation=True, write_still=False)

exit()
#
# # bpy.ops.object.text_add(enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
# # text = bpy.context.scene.objects['Text']
# # text.rotation_euler[0] = 1.5708
# # text.data.align_x = 'CENTER'
# # # rename text
# # text.data.body = "This is a test"
# # # change font
# #
# # # extrude text
# # text.data.extrude = 0.2