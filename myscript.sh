#!/bin/bash
#Этот скрипт создан для запуска в терминале mac os, поэтому некоторые команды могут отличаться от команд для os linux (например, здесь нет команды tree)
touch ./info.txt
{ echo "Hello, " | tr -d '\n'; whoami; } >> info.txt
echo >> info.txt
{ echo "Time: " | tr -d '\n'; date; } >> info.txt
{ echo "OS: " | tr -d '\n'; uname; } >> info.txt
df -lh $HOME | awk 'NR==2{print ("Memory: ", $3, "(used), ", $4, "(free)")}' >> info.txt
{ echo "Количество папок в домашней директории: " | tr -d '\n'; ls -l $HOME | grep -c ^d; } >> info.txt
{ echo "Количество файлов в домашней директории: " | tr -d '\n'; find $HOME -type f | wc -l ; } >> info.txt