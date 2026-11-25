from pathlib import Path

TEXT = "One star. Arrived Monday, left Friday, and the chef still served my weekend raw in the middle."

out = Path("/output/entry.txt")
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(TEXT, encoding="utf-8")
