import bpy
import addon_utils
import webbrowser
from bpy.types import Operator, AddonPreferences
from bpy.props import StringProperty, IntProperty, BoolProperty

package_name = ''
for mod in addon_utils.modules():
    if mod.bl_info['name'] == 'Blendshape Split':
        package_name = mod.__name__
        
class MyAddonPreferences(AddonPreferences):
    bl_idname = package_name
    
    lsuffix: StringProperty(
        name="Left blendshape suffix",
        default=".L"
    )
    rsuffix: StringProperty(
        name="Right blendshape suffix",
        default=".R"
    )

    def draw(self, context):
        layout = self.layout
        layout.label(text="Blendshape naming sceme")
        layout.prop(self, "lsuffix")
        layout.prop(self, "rsuffix")

        layout.label(text="Donate")
        col = layout.column(align=True)
        row = col.row(align=True)
        row.scale_y = 2
        row.operator(DonateButton.bl_idname, text="Thanks")

class DonateButton(bpy.types.Operator):
    bl_idname = 'blendshape_split.donatebutton'
    bl_label = "Thanks"
    bl_description = "Open webbrowser"
    bl_options = {'INTERNAL'}
    
    def execute(self, context):
        webbrowser.open_new('https://ko-fi.com/thasan')
        return {'FINISHED'}
        
def register():
    bpy.utils.register_class(MyAddonPreferences)
    bpy.utils.register_class(DonateButton)

def unregister():
    bpy.utils.unregister_class(MyAddonPreferences)
    bpy.utils.unregister_class(DonateButton)
