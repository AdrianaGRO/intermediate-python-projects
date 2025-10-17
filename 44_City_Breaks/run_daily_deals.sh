#!/bin/bash
# Simple daily deal runner

cd "/Users/adricati/Personal Development/intermediate-python-projects/44_City_Breaks"
echo "$(date): Running deal monitor..." >> deals.log
python3 simple_deal_monitor.py >> deals.log 2>&1