from os import path
import yaml
from subprocess import check_output
from repo_summary.mods_list import mods_list, ModsDict
from unittest import TestCase


FIXTURE_DIR = path.join(path.dirname(__file__), 'test_fixtures/mods_list')


class ModsDictTestCase(TestCase):
    def test_append_to(self):
        d = ModsDict()
        d.append_to('group1', 'comment 1')
        self.assertListEqual(d['group1'], ['comment 1'])

        d.append_to('group1', 'comment 2', 'comment 3')
        self.assertListEqual(d['group1'], ['comment 1', 'comment 2', 'comment 3'])

    def test_extend(self):
        d1 = ModsDict()
        d1.append_to('group1', 'comment 1.1')
        d1.append_to('group2', 'comment 2.1')

        d1.extend({
            'group1': ['comment 1.2'],
            'group2': ['comment 2.2', 'comment 2.3'],
            'group3': ['comment 3.1'],
        })

        self.assertListEqual(d1['group1'], ['comment 1.1', 'comment 1.2'])
        self.assertListEqual(d1['group2'], ['comment 2.1', 'comment 2.2', 'comment 2.3'])
        self.assertListEqual(d1['group3'], ['comment 3.1'])


class ModsListTestCase(TestCase):
    def test_mods_list(self):
        mods = mods_list(FIXTURE_DIR)

        list_of_mods = ModsDict()
        list_of_mods['ux'] = [
            'Greets the person in Arabic.',
            'Greets the person in Arabic.',
            'Greet the person.',
        ]

        list_of_mods['bash'] = [
            'Mimics the bash `true` command.',
        ]

        self.assertDictEqual(mods, list_of_mods)


class ModsListCommandLineTestCase(TestCase):
    def test_command_line(self):
        cmd_output = check_output('mods_list', cwd=FIXTURE_DIR).decode('utf-8')

        cmd_object = yaml.load(cmd_output)

        fixture_object = yaml.load(
            "bash:\n"
            "  -  Mimics the bash `true` command.\n"
            "ux: \n"
            "  - Greet the person.\n"
            "  - Greets the person in Arabic.\n"
        )

        # Check if the cmd_output is sorted
        self.assertLess(cmd_output.find('bash:'), cmd_output.find('ux:'), 'Should sort the groups')
        self.assertTrue(cmd_object['ux'][0].startswith('Greet the'), 'Should sort the comments list')

        self.assertDictEqual(fixture_object, cmd_object)
