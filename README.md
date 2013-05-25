## JavaScript API

## Features

![](https://raw.github.com/Pleasurazy/Sublime-JavsScript-API-Completions/master/README/demo1.jpg)

![](https://raw.github.com/Pleasurazy/Sublime-JavsScript-API-Completions/master/README/demo2.jpg)

![](https://raw.github.com/Pleasurazy/Sublime-JavsScript-API-Completions/master/README/demo3.jpg)

![](https://raw.github.com/Pleasurazy/Sublime-JavsScript-API-Completions/master/README/demo4.jpg)

![](https://raw.github.com/Pleasurazy/Sublime-JavsScript-API-Completions/master/README/demo5.jpg)

## Installation

Download files and place it at sublime package path like `/Sublime Text 2/Data/Packages/User`.

files:
* Download [JavaScript api]
* Download [jQuery api]

[JavaScript api]: https://github.com/Pleasurazy/Sublime-JavsScript-API-Completions/blob/master/sublime-completions/JavaScript.sublime-completions
[jQuery api]: https://github.com/Pleasurazy/Sublime-JavsScript-API-Completions/blob/master/sublime-completions/jQueryAPI.sublime-completions

## Relevant issues

> How to trigger classname tip when every typing?

Open file `Packages/User/Preferences.sublime-settings` or click `Setting - User` from menu. In my case, I just setup the `auto_complete_triggers` property as follow:

```json
  "auto_complete_triggers":
  [
    {
      "characters": "<>\"'-_qazwsxedcrfvtgbyhnujmikolpQAZWSXEDCRFVTGBYHNUJMIKOLP",
      "selector": "text, source, meta, string, punctuation, constant"
    }
  ],
```

It will active most of scope triggers and most of characters.