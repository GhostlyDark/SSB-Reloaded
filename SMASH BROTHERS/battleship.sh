#!/usr/bin/env bash



# set -e: exit on errors
# set -x: verbose logging

set -ex



# Set variables

PORT="_build/SSB Reloaded (BattleShip)"



# Remove and recreate work directories

rm -drf "$PORT"
mkdir -p "$PORT"



# Convert hashes from GLideN64 to BattleShip

python3 battleship.py --mapping battleship.json --pack . --out "$PORT"



# Copy port exclusive textures
\cp -r "Ports/BattleShip/"* "$PORT"
