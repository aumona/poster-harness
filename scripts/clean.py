from pathlib import Path
for extension in ("aux", "log", "out"):
    Path(f"output/pdf/main.{extension}").unlink(missing_ok=True)
