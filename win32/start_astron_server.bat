@echo off
title The Professor's Little Toontown - Astron Server
cd ../astron
astrond --loglevel info config/astrond.yml
pause
