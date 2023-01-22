#!/bin/sh


os_ver=$(lsb_release -rs)
echo "${os_ver}"
if [ "${os_ver}" = "22.04" ]; then
    echo "22"
else
    echo "18"
fi