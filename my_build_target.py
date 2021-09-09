import sublime
import sublime_plugin
import subprocess


class RunInCmdCommand(sublime_plugin.WindowCommand):
	def run(self, shell_cmd: str, **kwargs):
		cmd = sublime.expand_variables(shell_cmd, self.window.extract_variables())
		subprocess.call(f'start cmd /c \"{cmd} & pause\"', shell=True)