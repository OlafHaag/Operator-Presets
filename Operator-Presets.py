# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; version 3
#  of the License.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

bl_info = {
    "name": "OperatorPresets",
    "author": "Olaf Haag (Vaquero)",
    "version": (0, 1),
    "blender": (2, 7, 8),
    "location": "3D View > ToolShelf",
    "description": "Add panel with preset menu for active operator to the toolbar.",
    #"wiki_url": "https://github.com/OlafHaag/Operator-Presets/wiki",
    "tracker_url": "https://github.com/OlafHaag/Operator-Presets/issues/new",
    "warning": "Not working yet!",
    "category": "3D View"}

import bpy


class OperatorPresetsPanel(bpy.types.Panel):
    """Creates a Panel in the TOOL_PROPS region of the Tool Shelf"""
    bl_label = "Operator Presets"
    bl_idname = "OBJECT_PT_operator_preset"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOL_PROPS'


    def draw(self, context):
        layout = self.layout

        if bpy.context.active_operator:
            row = layout.row(align=True)
            row.menu("WM_MT_operator_presets", text=bpy.types.WM_MT_operator_presets.bl_label)
            row.operator("wm.operator_preset_add", text="", icon="ZOOMIN")
            row.operator("wm.operator_preset_add", text="", icon="ZOOMOUT").remove_active = True
        else:
            row = layout.row(align=True)
            row.label(text="No Active Operator")


def register():
    bpy.utils.register_class(OperatorPresetsPanel)


def unregister():
    bpy.utils.unregister_class(OperatorPresetsPanel)
    
    
if __name__ == "__main__":
    register()
