import sublime, sublime_plugin
import string


class PleasurazyAPICompletionsPackage():
  def init(self):
    self.api = {}
    self.settings = sublime.load_settings('sublime-API-Completions-Package.sublime-settings')

    # Caching completions
    for API_Keyword in self.settings.get('completion_active_list'):
      self.api[API_Keyword] = sublime.load_settings('API-completions-' + API_Keyword + '.sublime-settings')

    # Caching extended completions
    for API_Keyword in self.settings.get('completion_active_extend_list'):
      self.api[API_Keyword] = sublime.load_settings('API-completions-' + API_Keyword + '.sublime-settings')



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

    for API_Keyword in pleasurazy.api:
      # If completion active
      if pleasurazy.settings.get('completion_active_list').get(API_Keyword) or pleasurazy.settings.get('completion_active_extend_list').get(API_Keyword):
        scope = pleasurazy.api[API_Keyword].get('scope')
        if scope and view.match_selector(locations[0], scope):
          self.completions += pleasurazy.api[API_Keyword].get('completions')

    if not self.completions:
      return []

    compDefault = [view.extract_completions(prefix)]
    compDefault = [(item, item) for sublist in compDefault for item in sublist if len(item) > 3]
    compDefault = list(set(compDefault))
    completions = list(self.completions)
    completions = [tuple(attr) for attr in self.completions]
    completions.extend(compDefault)
    return (completions)
