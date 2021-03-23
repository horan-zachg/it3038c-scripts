#! /bin/bash
# This script is meant to be run on a windows computer even though it is written in BASH
echo "You are signed in as $(id -u -n)"
echo
echo "Your computer's name is $(uname -n)"
echo
echo "Your system type is $(uname -m)"