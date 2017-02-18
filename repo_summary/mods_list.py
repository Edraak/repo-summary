#!/usr/bin/env python

import re
from os import path, walk, getcwd
from subprocess import check_output
from collections import OrderedDict


REGEXP_COMMENT = r'Edraak \((?P<group>[^\)]+)\):(?P<comment>.+)'


class ModsDict(OrderedDict):
    def append_to(self, group, *mod_comment):
        if group not in self:
            self[group] = []

        self[group].extend(mod_comment)

    def extend(self, other_dict):
        for key, values in other_dict.items():
            self.append_to(key, *values)

    def get_uniq_sorted(self):
        keys = sorted(self.keys())

        for key in keys:
            # Sorted and unique
            vals = sorted(set(self[key]))
            yield key, vals


def mods_list_from_string(s):
    list_of_mods = ModsDict()

    for line in s.splitlines():
        m = re.search(REGEXP_COMMENT, line, re.IGNORECASE)

        if m:
            match = m.groupdict()
            list_of_mods.append_to(match['group'], match['comment'].strip())

    return list_of_mods


def mods_list(directory):
    output = check_output(['git', 'grep', '-e', 'Edraak (', '--', directory])
    return mods_list_from_string(output.decode('utf-8'))


def main():
    l = mods_list(getcwd())

    for key, vals in l.get_uniq_sorted():
        print('{}:'.format(key))

        for val in vals:
            print('  - "{}"'.format(val))

        print('')
