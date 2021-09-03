import bpy
import bmesh

class BlendshapeSplitOperator(bpy.types.Operator):
    """BlendshapeSplit Script"""                # Use this as a tooltip for menu items and buttons.
    bl_idname = "object.blendshape_split"       # Unique identifier for buttons and menu items to reference.
    bl_label = "Blendshape Split"               # Display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}           # Enable undo for the operator.


    def execute(self, context): 
        obj = context.active_object
        source = obj.active_shape_key.name
        source_idx = obj.active_shape_key_index
        basis_name = context.active_object.data.shape_keys.key_blocks[0].name

        if(source_idx == 0):
            return {'CANCELLED'}
        print(source_idx)
        
        bpy.ops.object.mode_set(mode = 'OBJECT')
        shape_l = context.active_object.shape_key_add(name=source+"_L", from_mix=False)
        shape_l_idx = obj.data.shape_keys.key_blocks.find(shape_l.name)
        shape_r = context.active_object.shape_key_add(name=source+"_R", from_mix=False)
        shape_r_idx = obj.data.shape_keys.key_blocks.find(shape_r.name)

        bpy.ops.object.mode_set(mode = 'EDIT')

        # Left side
        obj.active_shape_key_index = 0
        bm = bmesh.from_edit_mesh(obj.data)
        for i, v in enumerate(bm.verts):
            co_final = obj.matrix_parent_inverse @ v.co
            v.select_set(co_final.x < 0)
        bm.select_mode |= {'VERT'}
        bm.select_flush_mode()
        obj.active_shape_key_index = shape_l_idx
        bpy.ops.mesh.blend_from_shape(shape=source, blend=1, add=False)


        # Right side
        obj.active_shape_key_index = 0
        bm = bmesh.from_edit_mesh(obj.data)
        for i, v in enumerate(bm.verts):
            co_final = obj.matrix_parent_inverse @ v.co
            v.select_set(co_final.x > 0)
        bm.select_mode |= {'VERT'}
        bm.select_flush_mode()
        obj.active_shape_key_index = shape_r_idx
        bpy.ops.mesh.blend_from_shape(shape=source, blend=1, add=False)


        bpy.ops.object.mode_set(mode = 'OBJECT')
        obj.active_shape_key_index = source_idx
        return {'FINISHED'}


def menu_func(self, context):
    self.layout.operator(BlendshapeSplitOperator.bl_idname)
    
def register():
    bpy.utils.register_class(BlendshapeSplitOperator)
    bpy.types.MESH_MT_shape_key_context_menu.append(menu_func)

def unregister():
    bpy.utils.unregister_class(BlendshapeSplitOperator)
    bpy.types.MESH_MT_shape_key_context_menu.remove(menu_func)