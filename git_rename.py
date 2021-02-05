import os.path as osp
import subprocess

import sublime
import sublime_plugin


class GitRenameCommand(sublime_plugin.WindowCommand):
    def run(self, paths):
        file = paths[0]
        dir, name = osp.split(file)
        v = self.window.show_input_panel(
            "New Name/Location",
            name,
            lambda location: subprocess.call(
                ["git", "mv", file, location],
                shell=True,
                cwd=dir
            ),
            None,
            None
        )

        v.sel().clear()
        v.sel().add(sublime.Region(0, len(name)))

    def is_enabled(self, paths):
        return len(paths) == 1 and osp.isfile(paths[0])

    def is_visible(self, paths):
        return osp.exists(osp.join(osp.dirname(paths[0]), ".git"))
