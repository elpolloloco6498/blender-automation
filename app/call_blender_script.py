import os

render_path = os.path.abspath("generation/renders")
template_path = os.path.abspath("generation/templates/scene1.blend")
text = "Testing"

os.system(f'blender.exe --python automation_blender.py -- --render_path "{render_path}" --template_path "{template_path}" --text "{text}"')
print("Blender finished execution")
