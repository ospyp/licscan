# LicScan

A python package to check the licenses of your dependencies. Automate your license compliance! Fast, free, and open-sourced!

## Install

```
pip install licscan
```

## Usage

Use the default list of licenses:

```bash
licscan -f requirements.txt
```

Or a custom list:

```bash
licscan -f requirements.txt -a MIT ISC Apache
```

## License

NOSCL-C-2.0, a permissive copyleft license.