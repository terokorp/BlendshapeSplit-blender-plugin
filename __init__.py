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

from . import addon

def register():
    addon.register()

def unregister():
    addon.unregister()

if __name__ == "__main__":
    register()