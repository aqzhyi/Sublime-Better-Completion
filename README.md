Sublime API Completions Package
===============================

手刻的浪漫

This package aim at provide a simpler way to build own auto-completions and avoid `*.sublime-completions` override word-completion wrongly in some circumstance (issue#3).

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


## APIs

#### JavaScript and jQuery 1.9

![](https://raw.github.com/Pleasurazy/Sublime-API-Completions/master/README/JavaScript-and-jQuery/demo1.gif)

![](https://raw.github.com/Pleasurazy/Sublime-API-Completions/master/README/JavaScript-and-jQuery/static3.jpg)

#### Twitter Bootstrap 2 and 3

![](https://raw.github.com/Pleasurazy/Sublime-API-Completions/master/README/bootstrap-demo/demo1.gif)

![](https://raw.github.com/Pleasurazy/Sublime-API-Completions/master/README/bootstrap-demo/static3.jpg)


## Why this package?

* Several API completions ready to enable.

* More API completions create easier.

* Compared with `*.sublime-snippet` files:

    Simpler to build own API completions.

* Compared with `*.sublime-completions` files:

    This package will avoid `*.sublime-completions` override word-completion wrongly:

    * **speak in English**:

        It seems like when scope matched would be override word-completions provide by sublime itself. refer to issue#3.

    * **speak in Chinese**:

        一但 scope 匹配成功之後，雖然自製的 auto-completion 能夠順利工作；但是它也會覆蓋掉原本 word-completion。因此，只有在自製的辭彙的 scope 完全沒匹配時，才會正常地顯示原本的 word-completion，而不是將它們融合在一起顯示。


## Setting

API files is include the setting *keyword* such as `HTML`, `jQuery`, `myGlossary` as filename `API-completions-${filename}.sublime-settings` place in `/packages/User/` (good) or `/packages/${this-package}/sublime-completions/`.

```js
{
  // --------------------
  // sublime-API-Completions-Package
  // --------------------
  // API files is include the setting *keyword* such as `HTML`, `jQuery`, `myGlossary` as filename `API-completions-${filename}.sublime-settings` place in `/packages/User/` (good) or `/packages/${this-package}/sublime-completions/`.
  // After you enable, disable or added new your own completions, you might need restart your Sublime Text Editor.
  //
  // --------------------
  // APIs Setup
  // --------------------
  // `true` means enable it.
  // `false` means disable it.
  // `//` means disable it with code comment.
  "completion_active_list": {
    "HTML": false,
    "Underscore": false,
    "jQuery": false,
    "JavaScript": false,
    "twitter-bootstrap": false,
    "twitter-bootstrap3": false
    // Your own completions?
    "myHTML": false,
    "myAngularJS": false,
    "myGlossary": false,
    "myJavaScript": false
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

* Twitter Bootstrap Version 2 and 3

    * http://getbootstrap.com/

    * http://twitter.github.io/bootstrap/index.html

* HTML / HTML5

    * http://devdocs.io/html-html5/

## Installation

* Using **Package Control** to install.

    ![](https://raw.github.com/Pleasurazy/Sublime-API-Completions/master/README/UsingPackageControl.jpg)

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