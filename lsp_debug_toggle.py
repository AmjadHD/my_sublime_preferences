import sublime
import sublime_plugin


class ToggleDebugLspCommand(sublime_plugin.WindowCommand):

    debug = False

    def run(self):
        settings = sublime.load_settings("LSP.sublime-settings")
        if self.debug:
            settings.set("log_server", True)
            settings.set("log_debug", True)
            settings.set("log_stderr", True)
            settings.set("log_payloads", True)
            self.debug = False
            print("LSP debug mode: On")
        else:
            settings.set("log_server", False)
            settings.set("log_debug", False)
            settings.set("log_stderr", False)
            settings.set("log_payloads", False)
            self.debug = True
            print("LSP debug mode: Off")
        sublime.save_settings("LSP.sublime-settings")
