# picoctf_writeup

A personal collection of picoCTF writeups, notes, and solve scripts. The repository is organized by challenge category so that each problem can be reviewed independently.

## Repository Structure

```text
picoctf_writeup/
├── crypto/                 # Cryptography challenges
├── forensics/              # Digital forensics challenges
├── general_skill/          # General skill / basic Linux / scripting challenges
├── pwn/                    # Binary exploitation challenges
├── reverse/                # Reverse engineering challenges
├── web/                    # Web exploitation challenges
└── README.md
```

## Categories

| Category | Description |
|---|---|
| `crypto` | Classical cryptography, encoding, modular arithmetic, and related problems. |
| `forensics` | File analysis, metadata inspection, memory/file recovery, and hidden-data challenges. |
| `general_skill` | Basic command-line usage, scripting, decoding, and general CTF fundamentals. |
| `pwn` | Binary exploitation, memory corruption, stack behavior, and exploit scripts. |
| `reverse` | Program analysis, decompilation, debugging, and logic reconstruction. |
| `web` | Web security challenges, including request manipulation and common web vulnerabilities. |

## Usage

Clone the repository:

```bash
git clone https://github.com/Ian684/picoctf_writeup.git
cd picoctf_writeup
```

Browse a category and open the corresponding writeup or script:

```bash
cd crypto
ls
```

If a challenge includes a Python solve script, run it with:

```bash
python3 solve.py
```

Some scripts may require the original challenge files, remote service information, or additional Python packages depending on the problem.

## Notes

- This repository is intended for learning and review.
- Writeups may include personal solving processes, trial-and-error notes, or alternative solutions.
- Challenge files are not always included; refer to the original picoCTF challenge when needed.

## Disclaimer

All content is for educational and CTF practice purposes only. Do not use any technique from this repository against systems without explicit authorization.
