import os

def load_env(path: str = ".env") -> None:
    """
    Lightweight .env loader: parses KEY=VALUE lines,
    ignores blanks and “#” comments, and sets os.environ.
    Handles spaces around the '=' and strips quotes from values.
    """
    try:
        with open(path, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#") or "=" not in line:
                    continue
                key, val = line.split("=", 1)
                key = key.strip()
                val = val.strip().strip("'\"")
                os.environ.setdefault(key, val)
    except FileNotFoundError:
        print(f"Warning: .env file not found at {path}. Your application may not work as expected.")
