# 1. Enumerates the headers in a markdown file
Enumerate headers in markdown file.

## 1.1 Usage:
Run from the command line
```bash
markdown-enum inputFile.md 1 outputFile.md
```
The script will parse `someFile.md`, add an enumeration to each header and output
the result to the file named `outputFile.md`.
All previously existing headers will be overriden. 

If you want to ignore some levels (title for example), you can replace `1` by the minimal level. For example:

```bash
markdown-enum inputFile.md 2 inputFile.md
```

## 1.2 Install:
Requires python 3.

```bash
pip install enumerate-markdown
```

