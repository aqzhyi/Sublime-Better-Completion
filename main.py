import sublime, sublime_plugin
import string


class PleasurazyAPICompletionsPackage(sublime_plugin.EventListener):

  def __init__(self):
    self.api = {}
    if not hasattr(self, 'settings'):
      self.settings = sublime.load_settings('sublime-API-Completions-Package.sublime-settings')

    # Caching completions
    for key in self.settings.get('completion_active_list'):
      self.api[key] = sublime.load_settings('API-completions-' + key + '.sublime-settings')

    # Caching extended completions
    for key in self.settings.get('completion_active_extend_list'):
      self.api[key] = sublime.load_settings('API-completions-' + key + '.sublime-settings')

  def on_query_completions(self, view, prefix, locations):
    self.completions = []

    for key in self.api:
      # If completion active
      if self.settings.get('completion_active_list').get(key) or self.settings.get('completion_active_extend_list').get(key):
        scope = self.api[key].get('scope')
        if scope and view.match_selector(locations[0], scope):
          self.completions += self.api[key].get('completions')

    if not self.completions:
      return []

    compDefault = [view.extract_completions(prefix)]
    compDefault = [(item + "\tDefault", item) for sublist in compDefault for item in sublist if len(item) > 3]
    compDefault = list(set(compDefault))
    completions = list(self.completions)
    completions.extend(compDefault)
    completions = [tuple(attr) for attr in self.completions]
    return (completions)
