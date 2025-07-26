#!/bin/bash
#
# This script is simulating an installation of nginx on an input vm
#

vm_name=$1


if [[ ! -z $vm_name ]]; then
    echo "Installing Nginx on: '$vm_name'"
    sleep 2
    echo "Installation finished successfuly."
else
    echo "Please pass vm_name as an argument."
    exit 1
fi
