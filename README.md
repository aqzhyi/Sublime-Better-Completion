Sublime API Completions Package
===============================

This package aim at provide a simpler way to build own auto-completions.

**auto-completion** is lightweight, easier, simpler than **snippets**.

This package also provide several APIs completions such as JavaScript API, jQuery API, Underscore API, HTML5 and Bootstrap Classes collect by me.


## Compatible

2013/09

- Sublime Text 3 with MAC OS X 10.8.4 **tested**!

- Sublime Text 2 with MAC OS X 10.8.4 **tested**!

2013/07

- Sublime Text 2 with Windows 8 64bit **tested**!

- Sublime Text 2 with Windows 7 32bit **tested**!

- Sublime Text 3 with Windows 8 64bit **tested**!


[![](https://raw.github.com/Pleasurazy/Sublime-JavsScript-API-Completions/master/README/CanISwitchToSublimeText3.jpg)](http://www.caniswitchtosublimetext3.com/8f)


## Features

手刻的浪漫

#### JavaScript and jQuery 1.9

![](https://raw.github.com/Pleasurazy/Sublime-JavsScript-API-Completions/master/README/JavaScript-and-jQuery/demo1.gif)

![](https://raw.github.com/Pleasurazy/Sublime-JavsScript-API-Completions/master/README/JavaScript-and-jQuery/static3.jpg)

![](https://raw.github.com/Pleasurazy/Sublime-JavsScript-API-Completions/master/README/JavaScript-and-jQuery/static5.jpg)

#### Twitter Bootstrap 2.3.2

![](https://raw.github.com/Pleasurazy/Sublime-JavsScript-API-Completions/master/README/bootstrap-demo/demo1.gif)

![](https://raw.github.com/Pleasurazy/Sublime-JavsScript-API-Completions/master/README/bootstrap-demo/static1.jpg)

![](https://raw.github.com/Pleasurazy/Sublime-JavsScript-API-Completions/master/README/bootstrap-demo/static2.jpg)

![](https://raw.github.com/Pleasurazy/Sublime-JavsScript-API-Completions/master/README/bootstrap-demo/static3.jpg)

#### HTML / HTML5

![](https://raw.github.com/Pleasurazy/Sublime-JavsScript-API-Completions/master/README/HTML/html-demo1.gif)

![](https://raw.github.com/Pleasurazy/Sublime-JavsScript-API-Completions/master/README/HTML/static1.jpg)

![](https://raw.github.com/Pleasurazy/Sublime-JavsScript-API-Completions/master/README/HTML/static2.jpg)


## Why this package?

* Compared with `*.sublime-snippet` files:

  Simpler to build own API completions.

* Compared with `*.sublime-completions` files:

  * **speak in English**:

      It seems like when scope matched would be override completions provide by sublime itself. refer to issue #3.

  * **speak in Chinese**:

      一但 scope 匹配成功之後，雖然自製的 auto-completion 能更順利工作；但是它會覆蓋掉原本 auto-completion，只有在自製的辭彙完全沒匹配，才會顯示原本的 auto-completion，而不是將它們融合。


## Setting

API files is include the setting *keyword* such as `HTML`, `jQuery`, `myGlossary` as filename `API-completions-${filename}.sublime-settings` place in `/packages/${this-package}/sublime-completions/` or `/packages/User/`.

```js
{
  // --------------------
  // sublime-API-Completions-Package
  // --------------------
  // API files is include the setting *keyword* such as `HTML`, `jQuery`, `myGlossary` as filename `API-completions-${filename}.sublime-settings` place in `/packages/${this-package}/sublime-completions/` or `/packages/User/`.
  // After you enable, disable or added new your own completions, you might need restart your Sublime Text.
  //
  // --------------------
  // APIs Collected by github/Pleasurazy
  // --------------------
  // `true` means load file and enable it
  // `false` means load file and disable it
  "completion_active_list": {
    "HTML": false,
    "Underscore": false,
    "jQuery": true,
    "JavaScript": true,
    "twitter-bootstrap": true
  },
  // --------------------
  // Enable your own APIs
  // --------------------
  // `true` means load file and enable it
  // `false` means load file and disable it, but didn't effect `completion_active_list` setting.
  "completion_active_extend_list": {
    // "myGlossary": true,
    // "myAngularJS": true
  }
}
```

After you enable, disable or added new your own completions, you might need restart your Sublime Text.


## API References

* jQuery Version: 1.9

  * http://oscarotero.com/jquery/

* JavaScript

  * http://overapi.com/javascript/
  * http://www.w3schools.com/js/

* Underscore 1.5.1

  * http://underscorejs.org/

* Twitter Bootstrap Version 2.3.2

  * http://twitter.github.io/bootstrap/index.html

* HTML / HTML5

  * http://devdocs.io/html-html5/

## Installation

* Using **Package Control** to install.

  ![](https://raw.github.com/Pleasurazy/Sublime-JavsScript-API-Completions/master/README/UsingPackageControl.jpg)

* Waiting download.

* Happy programming.


## Relevant issues

> How to trigger completion hint when every typing?

Open file `Packages/User/Preferences.sublime-settings` or click `Setting - User` from menu. In my case, I just setup the `auto_complete_triggers` property as follow:

```js
{
  "auto_complete_triggers":
  [
    {
      "characters": "qazwsxedcrfvtgbyhnujmikolpQAZWSXEDCRFVTGBYHNUJMIKOLP",
      "selector": "text, source, meta, string, punctuation, constant"
    }
  ]
}
```

It will active most of scope triggers and most of characters.