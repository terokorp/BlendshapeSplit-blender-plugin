bl_info = {
    "name": "Blendshape Split",
    "description": "Splits blendshape to L and R shapes",
    "author": "Tero Korpela",
    "version": (1, 0),
    "blender": (2, 92, 0),
    "location": "Shape Key Specials",
    "wiki_url": "https://github.com/terokorp/",
    "tracker_url": "https://github.com/terokorp/",
    "support": "COMMUNITY",
    "category": "Object",
}

if "bpy" not in locals():
    import bpy
    is_reloading = False
else:
    is_reloading = True

if not is_reloading:
    from . import addon
    from . import preferences
else:
    import importlib
    importlib.reload(addon)
    importlib.reload(preferences)


def register():
    addon.register()
    preferences.register()
    
def unregister():
    addon.unregister()
    preferences.unregister()

if __name__ == "__main__":
    register()