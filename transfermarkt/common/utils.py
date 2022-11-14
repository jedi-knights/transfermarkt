def urljoin(base: str, path: str):
    if base is None:
        raise ValueError("Undefined base URL!")

    if path is None:
        raise ValueError("Undefined path!")

    if len(base) == 0:
        if len(path) == 0:
            return ""
        else:
            return path

    if base.endswith("/"):
        base = base[:-1]

    if path.startswith("/"):
        path = path[1:]

    return str(f"{base}/{path}")
