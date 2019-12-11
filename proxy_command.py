import sublime
import sublime_plugin

# https://stackoverflow.com/questions/55990607/how-to-assign-a-scope-to-a-sublime-text-3-context-menu

class ProxyCommand(sublime_plugin.TextCommand):
    def run(self, edit, command_name, scope_selector, **kwargs):
        self.view.run_command(command_name, kwargs)

    def is_visible(self, command_name, scope_selector, **kwargs):
        return self.view.match_selector(self.view.sel()[0].begin(), scope_selector)

