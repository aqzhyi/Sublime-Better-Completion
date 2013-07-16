import sublime, sublime_plugin
import string


class PleasurazyAPICompletionsPackage():
  def init(self):
    self.api = {}
    self.settings = sublime.load_settings('sublime-API-Completions-Package.sublime-settings')

    # Caching completions
    for key in self.settings.get('completion_active_list'):
      self.api[key] = sublime.load_settings('API-completions-' + key + '.sublime-settings')

    # Caching extended completions
    for key in self.settings.get('completion_active_extend_list'):
      self.api[key] = sublime.load_settings('API-completions-' + key + '.sublime-settings')

# In Sublime Text 3 things are loaded async, using plugin_loaded() callback before try accessing.
pleasurazy = PleasurazyAPICompletionsPackage()

if int(sublime.version()) < 3000:
  pleasurazy.init()
else:
  def plugin_loaded():
    global pleasurazy
    pleasurazy.init()



class PleasurazyAPICompletionsPackageEventListener(sublime_plugin.EventListener):
  global pleasurazy

  def on_query_completions(self, view, prefix, locations):
    self.completions = []

    for key in pleasurazy.api:
      # If completion active
      if pleasurazy.settings.get('completion_active_list').get(key) or pleasurazy.settings.get('completion_active_extend_list').get(key):
        scope = pleasurazy.api[key].get('scope')
        if scope and view.match_selector(locations[0], scope):
          self.completions += pleasurazy.api[key].get('completions')

    if not self.completions:
      return []

    compDefault = [view.extract_completions(prefix)]
    compDefault = [(item, item) for sublist in compDefault for item in sublist if len(item) > 3]
    compDefault = list(set(compDefault))
    completions = list(self.completions)
    completions = [tuple(attr) for attr in self.completions]
    completions.extend(compDefault)
    return (completions)
