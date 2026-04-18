#!/bin/zsh
set -euo pipefail

REPO_DIR="$HOME/SourceCode/TechPKM"
LOG_DIR="$REPO_DIR/scrips/logs"
LOG_FILE="$LOG_DIR/auto_git_pull.log"
mkdir -p "$LOG_DIR"

{
  echo "[$(date '+%Y-%m-%d %H:%M:%S %Z')] auto pull start"
  cd "$REPO_DIR"
  /usr/bin/git fetch --all --prune
  BRANCH=$(/usr/bin/git rev-parse --abbrev-ref HEAD)
  /usr/bin/git pull --ff-only origin "$BRANCH"
  echo "[$(date '+%Y-%m-%d %H:%M:%S %Z')] auto pull done"
} >> "$LOG_FILE" 2>&1
