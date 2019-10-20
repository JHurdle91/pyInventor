from win32com.client import Dispatch, GetActiveObject, gencache

try:
    invApp = GetActiveObject('Inventor.Application')
except:
    invApp = Dispatch('Inventor.Application')
    invApp.Visible = True

mod = gencache.EnsureModule('{D98A091D-3A0F-4C3E-B36E-61F62068D488}', 0, 1, 0)
invApp = mod.Application(invApp)
