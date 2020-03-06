import os.path

import sublime
import sublime_plugin


class DeleteOpenFileCommand(sublime_plugin.WindowCommand):
    def run(self):
        view = self.window.active_view()
        if view is None:
            file_name = self.window.extract_variables().get('file')
        else:
            file_name = view.file_name()
        if file_name is None or not os.path.exists(file_name):
            return
        if sublime.ok_cancel_dialog("Delete %s?" % file_name, "Delete"):
            if not view.close():
                return
            import Default.send2trash as send2trash
            send2trash.send2trash(file_name)
