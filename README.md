# PySide2 Taskbar Icon Fix Post-KB5051987 Update

This repository addresses the issue where PySide2 applications fail to display the correct taskbar icon after installing the Windows 11 KB5051987 update.

## Problem

After applying the KB5051987 update, PySide2 applications may show the default icon in the taskbar instead of the specified application icon.

## Solution

The solution involves explicitly setting the window icon using Windows API calls within the application code.

## Repository Contents

- `src/main.py`: Sample PySide2 application implementing the fix.
- `docs/ISSUE_DETAILS.md`: [Detailed explanation of the issue](docs/ISSUE_DETAILS.md).
- `docs/SOLUTION_EXPLANATION.md`: [Step-by-step guide to the solution](docs/SOLUTION_EXPLANATION.md).

## Getting Started

1. **Clone the repository**:
   ```bash
   git clone https://github.com/bornalgo/pyside2-taskbar-icon-fix.git
   ```

2. **Navigate to the source directory**:
   ```bash
   cd pyside2-taskbar-icon-fix/src
   ```

3. **Install dependencies**:
   Ensure you have PySide2 installed:
   ```bash
   pip install PySide2
   ```

4. **Run the application**:
   ```bash
   python main.py
   ```

## License

This project is licensed under the [MIT License](LICENSE).