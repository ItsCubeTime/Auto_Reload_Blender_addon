import bpy
from . import reload

from .addon_prefs import get_addon_preferences


class AUTORELOAD_OT_reload(bpy.types.Operator):
    bl_idname = "autoreload.reload"
    bl_label = "Reload Datas"
    bl_description = "Reload datas if modified."
    bl_options = {"REGISTER", "UNDO", "INTERNAL"}
    
    behavior : bpy.props.StringProperty()

    def execute(self, context):
        props = context.window_manager.autoreload_properties
        
        if self.behavior == "all":
            reload.reload_modified_objects()
            
        else:
            obj_to_reload = reload.get_files_size(self.behavior)
            
            if get_addon_preferences().debug:
                print("AUTORELOAD --- Objects to reload :")
                print(obj_to_reload)
                
            function = f"reload.reload_{self.behavior}(obj_to_reload)"
            exec(function)
        
        self.report({'INFO'}, f"{self.behavior} modified datas reloaded")
        
        return {"FINISHED"}

    
### REGISTER ---
def register():
    bpy.utils.register_class(AUTORELOAD_OT_reload)

def unregister():
    bpy.utils.unregister_class(AUTORELOAD_OT_reload)
            
