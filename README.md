# Python CI/CD Demo

A small Python expense calculator used for learning CI/CD.

## Run the program

```powershell
python calculator.py
```

Expected output:

```text
Total with tax: 118.00
```

## Run the tests

```powershell
python -m unittest
```

The workflow in `.github/workflows/ci.yml` runs the same tests automatically on GitHub after every push or pull request.
