#!/bin/bash

read -p "Enter code: " participant
pthr="/media/pablo/Kirk/REDLATMA/raw"
pthheu="/media/pablo/Kirk/REDLATMA/heuristic2023.py"
pthbids="/media/pablo/Kirk/REDLATMA/bids/"

heudiconv -d $pthr/{subject}/*/* -s $participant -f $pthheu -b -o $pthbids

echo "done $participant"