import ctypes  # An included library with Python install.


def mbox(title, text, style):
    #  Styles:
    #  0 : OK
    #  1 : OK | Cancel
    #  2 : Abort | Retry | Ignore
    #  3 : Yes | No | Cancel
    #  4 : Yes | No    #Yes = 6, No = 7
    #  5 : Retry | No
    #  6 : Cancel | Try Again | Continue
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)


def get_partnumber(filename_and_path):
    filename_with_ext = filename_and_path.split("\\")[-1]
    trimmed_partnumber = filename_with_ext.split("_")[0]
    return trimmed_partnumber
