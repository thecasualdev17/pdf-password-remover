# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),  
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [0.1.0] - 2025-05-29
### Added
- Initial release of PDF Password Remover CLI tool
- Remove password from a single PDF file
- Batch process all PDFs in a directory
- Optional GUI file/directory picker using Tkinter
- Output unlocked PDFs to a specified directory
- Interactive prompts for missing arguments
- MIT License, README, and project documentation

## [0.2.0] - 2025-06-01
### Added
- Improved error handling in PDF password removal
- Output directory creation and validation
- Support for batch processing with custom output directory
- Updated dependencies in `pyproject.toml`

## [0.3.0] - 2025-05-30
### Added
- Added support for tkinterdnd2 for enhanced file/directory picker with drag-and-drop (macOS compatibility improvements)
- Fallback to manual input if tkinterdnd2 and Tkinter are unavailable
- Added `tkinterdnd2` and `tk` to dependencies in `pyproject.toml`
- Improved `pick_path` function to use tkinterdnd2 if available, otherwise fallback to Tkinter or manual input

---
