import sys
from math import ceil
from Modules.Module1 import mbox, get_partnumber
from Modules.get_inventor import invApp, mod


COMMAND_NAME = 'Save DXF'

doc = mod.PartDocument(invApp.ActiveDocument)

if doc.DocumentSubType.DocumentSubTypeID != "{9C464203-9BAE-11D3-8BAD-0060B0CE6BB4}":
    mbox(COMMAND_NAME, 'This can only be run on a Sheet Metal document. Exiting...', 0)
    sys.exit('This can only be run on a Sheet Metal document.')

description = doc.PropertySets.Item("Design Tracking Properties").Item('Description')
filename = doc.FullFileName
partnumber = get_partnumber(filename)

smcd = mod.SheetMetalComponentDefinition(doc.ComponentDefinition)
if not smcd.HasFlatPattern:
    try:
        smcd.Unfold()
        smcd.FlatPattern.ExitEdit()
    except:
        mbox(COMMAND_NAME, 'Could not unfold part. Create flat pattern and try again. Exiting...', 0)
        sys.exit('Could not unfold part. Create flat pattern and try again.')

DXF_OPTIONS = ('FLAT PATTERN DXF?AcadVersion=2004'
        '&OuterProfileLayer=IV_INTERIOR_PROFILES'
        '&InvisibleLayers='
	        'IV_TANGENT;'
	        'IV_FEATURE_PROFILES_DOWN;'
	        'IV_BEND;'
	        'IV_BEND_DOWN;'
	        'IV_TOOL_CENTER;'
	        'IV_TOOL_CENTER_DOWN;'
	        'IV_ARC_CENTERS;'
	        'IV_FEATURE_PROFILES;'
	        'IV_FEATURE_PROFILES_DOWN;'
	        'IV_ALTREP_FRONT;'
	        'IV_ALTREP_BACK;'
	        'IV_ROLL_TANGENT;'
	        'IV_ROLL'
        '&SimplifySplines=True'
        '&BendLayerColor=255;255;0')

DXF_PATH = r'.\DXF Files'
dxf_filename = f'{DXF_PATH}\\{partnumber}.dxf'

try:
    smcd.DataIO.WriteDataToFile(DXF_OPTIONS, dxf_filename)
except:
    mbox(COMMAND_NAME, 'Failed to save DXF.', 0)
    sys.exit('Failed to save DXF.')

mbox("Batch DXF", "DXF saved to DXF Archive: \n\n" + DXF_PATH, 0)
