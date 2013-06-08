import sublime, sublime_plugin

# The autoitbuild command is called as target by AutoIt.sublime-build
class autoitbuild(sublime_plugin.WindowCommand):

	def run(self):
		filepath = self.window.active_view().file_name()
		ahkpath = sublime.load_settings("AutoIt.sublime-settings").get("AutoItEXEPath")
		cmd = [ahkpath, "/ErrorStdOut", filepath]
		self.window.run_command("exec", {"cmd": cmd})
