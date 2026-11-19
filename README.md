<p align="center"><img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f172a,100:0f766e&height=170&section=header&text=License%20Header%20Audit&fontColor=ffffff&fontSize=34" alt="License Header Audit banner"/></p>
<p align="center"><img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=19&duration=2800&pause=900&center=true&vCenter=true&width=620&lines=Check%20source%20license%20headers%3BFind%20missing%20SPDX%20identifiers%3BRead-only%20repository%20audit" alt="Typing title"/></p>
<p align="center"><img src="https://img.shields.io/github/license/CyberLoop-dev/license-header-audit?style=flat-square" alt="License"/> <img src="https://img.shields.io/github/languages/top/CyberLoop-dev/license-header-audit?style=flat-square" alt="Language"/> <img src="https://img.shields.io/github/stars/CyberLoop-dev/license-header-audit?style=flat-square" alt="Stars"/> <img src="https://img.shields.io/github/last-commit/CyberLoop-dev/license-header-audit?style=flat-square" alt="Last commit"/></p>
<p align="center"><img src="assets/mark.svg" width="520" alt="License Header Audit illustration"/></p>

## 🧭 Overview
License Header Audit checks the opening lines of source files for an SPDX license identifier. It reports missing headers without changing files, so teams can review policy gaps before adding notices.

## ✨ Features
- ⚖️ Scan common source-code extensions
- 🔎 Check only the first configurable number of lines
- 🧾 Emit concise text or JSON findings
- 🛡️ Read-only by design; no source files are modified

## 🖥️ Demo
No hosted demo is provided. Run the tool locally using the quick-start command.

## 🚀 Quick Start
Requires Python 3.10 or newer.

```bash
python main.py ./ --lines 8
```

Run the test suite with:

```bash
python -m unittest discover -s tests -v
```

## 🧰 Tech Stack
- Python standard library
- `argparse` CLI and `unittest`
- Read-only inspection by default

## 🗂️ Folder Structure
```text
.
├── .github/workflows/ci.yml
├── assets/mark.svg
├── tests/test_main.py
├── main.py
├── pyproject.toml
└── README.md
```

## 🗺️ Roadmap
- [ ] Add more edge-case fixtures
- [ ] Improve machine-readable output
- [ ] Keep the core workflow dependency-free

## 🤝 Contributing
Issues and focused pull requests are welcome. Add regression tests for parser and reporting changes.

## 📄 License
MIT License. See [LICENSE](LICENSE).

<p align="center"><img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f766e,100:0f172a&height=100&section=footer" alt="Animated wave footer"/></p>
