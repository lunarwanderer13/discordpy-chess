#!/usr/bin/env bash

cd "$(dirname "$0")" || exit 1

nohup ./discordpy-chess.sh >/dev/null 2>&1 &

