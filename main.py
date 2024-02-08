import bpy
import os
import time

# Set the autosave interval in seconds
AUTOSAVE_INTERVAL = 300  # 5 minutes

class AutoSaveAddon(bpy.types.Operator):
    bl_idname = "wm.auto_save"
    bl_label = "Auto Save"
    
    _timer = None

    def modal(self, context, event):
        if event.type == 'TIMER':
            bpy.ops.wm.save_mainfile(filepath=bpy.data.filepath)
        return {'PASS_THROUGH'}

    def execute(self, context):
        wm = context.window_manager
        self._timer = wm.event_timer_add(AUTOSAVE_INTERVAL, window=context.window)
        wm.modal_handler_add(self)
        return {'RUNNING_MODAL'}

def register():
    bpy.utils.register_class(AutoSaveAddon)

def unregister():
    bpy.utils.unregister_class(AutoSaveAddon)

if __name__ == "__main__":
    register()
