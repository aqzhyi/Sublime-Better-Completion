import sublime, sublime_plugin
import string


class PleasurazyAPICompletionsPackage():
  def init(self):
    self.api = {}
    self.settings = sublime.load_settings('sublime-better-completion-setting.sublime-settings')
    self.API_Setup = self.settings.get('completion_active_list')

    # Caching completions
    if self.API_Setup:
      for API_Keyword in self.API_Setup:
        self.api[API_Keyword] = sublime.load_settings('sublime-better-completion-api-' + API_Keyword + '.sublime-settings')

    # Caching extended completions(deprecated)
    if self.settings.get('completion_active_extend_list'):
      for API_Keyword in self.settings.get('completion_active_extend_list'):
        self.api[API_Keyword] = sublime.load_settings('sublime-better-completion-api-' + API_Keyword + '.sublime-settings')



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
      if (pleasurazy.API_Setup and pleasurazy.API_Setup.get(API_Keyword)) or (pleasurazy.settings.get('completion_active_extend_list') and pleasurazy.settings.get('completion_active_extend_list').get(API_Keyword)):
        scope = pleasurazy.api[API_Keyword].get('scope')
        if scope and view.match_selector(locations[0], scope):
          self.completions += pleasurazy.api[API_Keyword].get('completions')

    if not self.completions:
      return []

    # extend word-completions to auto-completions
    compDefault = [view.extract_completions(prefix)]
    compDefault = [(item, item) for sublist in compDefault for item in sublist if len(item) > 3]
    compDefault = list(set(compDefault))
    completions = list(self.completions)
    completions = [tuple(attr) for attr in self.completions]
    completions.extend(compDefault)
    return (completions)