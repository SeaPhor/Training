#!/usr/bin/python3
#
####    To generate the bigdata file I ran this command- "for i in `rpm -qa --last | awk '{print $1}'`; do rpm -qi $i >> bigdata-rpmlistinfo.txt; echo "" >> bigdata-rpmlistinfo.txt;  done"
data = {}

with open('bigdata-rpmlistinfo.txt') as f:
    rpm_size = ''
    rpm_group = ''
    for line in f:
####    RPM Names
#        split_line = line.strip().split()
####    ####    Is the '*' a proper python operator
#        if (split_line[0] == 'gnome*' or split_line[0] == 'chrome'*):
####    Or
####    ####    Is the '-' in a proper place?
#        split_line = line.strip().split(-)
#        if (split_line[0] == 'gnome' or split_line[0] == 'chrome'):
####    RPM Sizes
        split_line = line.strip().split(:)
        if (split_line[0] == 'Size'):
            data[split_line[1]] = []
            rpm_size = split_line[1]
####    RPM Group
        split_line = line.strip().split(:)
        if (split_line[0] == 'Group'):
            data[split_line[1]] = []
            rpm_group = split_line[1]
####    ####    Is the '~' a proper python operator?
            if (split_line[1] =~ 'Devel'):
                print 'Group is ' rpm_group
                data[rpm_group].append(split_line[1])

