# Issue Details: Taskbar Icon Not Displaying Correctly in PySide2 Applications

## Background

Following the Windows 11 KB5051987 update, released on February 11, 2025, several developers reported that PySide2 applications no longer display the correct icon in the taskbar. Instead, the default application icon appears. This issue is specific to applications using PySide2 and does not seem to affect other frameworks in the same way.

## Changelog Highlights from KB5051987

- **Taskbar Improvements:** Enhanced previews and animations when hovering over apps.
- **Windows Studio Effects:** System tray icon appears when apps utilize Windows Studio Effects on devices with Neural Processing Units (NPUs).
- **File Explorer Enhancements:**
  - "New Folder" option in the right-click menu for the left pane.
  - Resolved issues with search repetition, incorrect date/time properties after copying files, and icon updates when switching themes.
- **Input and Display Fixes:**
  - Addressed cursor disappearance over text fields in certain applications.
  - Fixed transparency issues with pointer trails.
  - Resolved cursor stuttering even under low system resource usage.
- **Audio and USB Device Fixes:**
  - Resolved issues with USB audio devices, especially those using DAC drivers based on USB 1.0.
  - Fixed "This device cannot start" (Code 10) errors with certain external audio devices.
  - Ensured proper recognition of USB cameras post-January 2025 security update.

## Cause

The KB5051987 update made changes to how Windows handles taskbar icons and window previews. These modifications may have affected applications that rely on frameworks like PySide2, which traditionally set window icons using Qt methods. The update could have altered the internal handling of window properties, leading to discrepancies between the window icon and the taskbar icon.

## References

- [Windows 11 KB5051987 Update Release Notes](https://support.microsoft.com/en-us/topic/february-11-2025-kb5051987-os-build-26100-3194-63fb007d-3f52-4b47-85ea-28414a24be2d)

