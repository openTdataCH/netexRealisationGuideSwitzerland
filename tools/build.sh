#!/usr/bin/env bash
# Build script for the github action.
# - can also be run and tested locally (Mac or Linux)
# - use "python -m build to build docs otherwise
set -Eeuo pipefail
IFS=$'\n\t'

# --- Configuration (override via environment variables) ---
PYTHON="${PYTHON_BIN:-python3}"      # or "python" if that's your default
VENV_DIR="${VENV_DIR:-.venv-build}"      # ephemeral venv only for build tools
OUTDIR="${OUTDIR:-dist}"                 # where artifacts go
EXTRA_BUILD_ARGS="${EXTRA_BUILD_ARGS:-}" # e.g. "--no-isolation" (not recommended)
TEST_INSTALL="${TEST_INSTALL:-1}"        # 1 to smoke-test installing the wheel
BASE_URL="${BASE_URL:-/netexRealisationGuideSwitzerland/main}" # The base url for Jekyll page generation

# --- Move to repo root ---
SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" &>/dev/null && pwd)"
REPO_ROOT="$(cd -- "$SCRIPT_DIR/.." &>/dev/null && pwd)"
cd "$REPO_ROOT"

echo "==> Building package in $REPO_ROOT"

# --- Pre-flight checks ---
if [[ ! -f pyproject.toml ]]; then
  echo "Error: pyproject.toml not found in repository root: $REPO_ROOT" >&2
  exit 1
fi

# --- Clean previous build outputs ---
# rm -rf "$OUTDIR" build .pytest_cache
mkdir -p "$OUTDIR"

# --- Create isolated venv for build tools ---
if [[ ! -d "$VENV_DIR" ]]; then
  echo "==> Creating build venv at $VENV_DIR"
  $PYTHON -m venv "$VENV_DIR"
fi

# shellcheck source=/dev/null
source "$VENV_DIR/bin/activate"
$PYTHON -m pip install --upgrade pip setuptools
$PYTHON -m pip install --upgrade build

# If you use setuptools-scm, ensure it's present for version derivation
if grep -qiE 'setuptools[-_]scm' pyproject.toml; then
  $PYTHON -m pip install --upgrade setuptools-scm
fi

# --- Make builds more reproducible (optional but harmless) ---
export PYTHONHASHSEED=0
export SOURCE_DATE_EPOCH="${SOURCE_DATE_EPOCH:-$(git log -1 --pretty=%ct 2>/dev/null || date +%s)}"

# --- Build sdist and wheel ---
echo "==> Running python -m build"
$PYTHON -m build --sdist --wheel --outdir "$OUTDIR" $EXTRA_BUILD_ARGS

# --- List outputs ---
echo "==> Produced artifacts:"
ls -lh "$OUTDIR"

deactivate
echo "==> Build complete."
