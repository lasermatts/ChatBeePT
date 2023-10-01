#!/bin/sh

V=$(cat /sys/firmware/beepy/battery_raw)

V=$(echo "obase=10; ibase=16; $V" | bc)
echo "$V * 3.3 * 2 / 4095" | bc -l | cut -c1-5
