import ctypes
from ctypes import wintypes

user32 = ctypes.windll.user32

# Win32 API tanımları
EnumWindowsProc = ctypes.WINFUNCTYPE(
    wintypes.BOOL,
    wintypes.HWND,
    wintypes.LPARAM
)

user32.EnumWindows.argtypes = [EnumWindowsProc, wintypes.LPARAM]
user32.EnumWindows.restype = wintypes.BOOL

user32.IsWindowVisible.argtypes = [wintypes.HWND]
user32.IsWindowVisible.restype = wintypes.BOOL

user32.GetWindowTextLengthW.argtypes = [wintypes.HWND]
user32.GetWindowTextLengthW.restype = ctypes.c_int

user32.GetWindowTextW.argtypes = [
    wintypes.HWND,
    wintypes.LPWSTR,
    ctypes.c_int
]
user32.GetWindowTextW.restype = ctypes.c_int

user32.GetWindowDisplayAffinity.argtypes = [
    wintypes.HWND,
    ctypes.POINTER(wintypes.DWORD)
]
user32.GetWindowDisplayAffinity.restype = wintypes.BOOL


AFFINITY_NAMES = {
    0x00000000: "WDA_NONE",
    0x00000001: "WDA_MONITOR",
    0x00000011: "WDA_EXCLUDEFROMCAPTURE",
}


def get_window_title(hwnd):
    length = user32.GetWindowTextLengthW(hwnd)

    if length == 0:
        return ""

    buffer = ctypes.create_unicode_buffer(length + 1)
    user32.GetWindowTextW(hwnd, buffer, length + 1)

    return buffer.value


windows = []


@EnumWindowsProc
def enum_callback(hwnd, lparam):
    if not user32.IsWindowVisible(hwnd):
        return True

    title = get_window_title(hwnd)

    if not title:
        return True

    affinity = wintypes.DWORD()

    success = user32.GetWindowDisplayAffinity(
        hwnd,
        ctypes.byref(affinity)
    )

    if success:
        value = affinity.value
        name = AFFINITY_NAMES.get(
            value,
            f"UNKNOWN (0x{value:08X})"
        )
    else:
        value = None
        name = "GetWindowDisplayAffinity FAILED"

    windows.append((hwnd, title, value, name))

    return True


user32.EnumWindows(enum_callback, 0)


for hwnd, title, value, name in windows:
    print(f"HWND: {hwnd}")
    print(f"TITLE: {title}")
    print(f"AFFINITY: {name}")
    print("-" * 60)