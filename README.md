# Repo Summary Tools
A collection of tools to generate summary about the code including:
 - [ ] Cherry-picks
 - [x] Structured list of modifications
 - [ ] List of hacks


## List all Edraak Modifications
This lists all modifications in a certain **git** repo, grouped by their group.

Assume that you have a file that has the following:
```
def true():
    """
    Do nothing, successfully.

    Edraak (bash): Mimics the bash `true` command.
    """
    pass

def false():
    """
    Edraak (bash): Does nothing unsuccessfully.
    """
    throw Exception('Ooops')
```

Execute the following commands:
```
$ pip install git+https://github.com/Edraak/repo-summary.git
$ cd path/to/repo/root
$ mods_list
```

The `mods_list` command will print the following output:
```
bash:
  - "Does nothing unsuccessfully."
  - "Mimics the bash `true` command."
```

There can be multiple groups and multiple comments per group.
