"""Path safety helpers to prevent path traversal attacks."""

import os


def safe_join(base_dir: str, *parts: str) -> str:
    """Join paths and verify the result stays within base_dir.

    Raises ValueError if the resolved path escapes base_dir.
    """
    base_real = os.path.realpath(base_dir)
    result = os.path.realpath(os.path.join(base_real, *parts))
    if result != base_real and not result.startswith(base_real + os.sep):
        raise ValueError(
            f"Path traversal detected: '{os.path.join(*parts)}' resolves to "
            f"'{result}' which is outside '{base_real}'"
        )
    return result
