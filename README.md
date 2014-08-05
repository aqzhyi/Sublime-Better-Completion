Sublime Better Completion Package
===============================

手刻的浪漫

This package aim at provide a simpler way to build own auto-completions and avoid `*.sublime-completions` override word-completion wrongly in some circumstance (issue#3).

**auto-completion** is lightweight, easier, simpler than **snippets**.

This package also provide several APIs completions such as JavaScript API, jQuery API, Underscore API, HTML5 and Bootstrap Classes collect by me.


## Compatible

Should be working fine with ST2 and ST3.

2014/08

- Sublime Text 3 with MAC OS X 10.9.4 manual installed **tested**!

2013/09

- Sublime Text 3 with MAC OS X 10.8.4 using Package Control **tested**!

- Sublime Text 2 with MAC OS X 10.8.4 using Package Control **tested**!

2013/07

- Sublime Text 2 with Windows 8 64bit **tested**!

- Sublime Text 2 with Windows 7 32bit **tested**!

- Sublime Text 3 with Windows 8 64bit **tested**!


## Why this package?

* Several API completions ready to enable.

* More API completions create easier.

* Compared with `*.sublime-snippet` files:

    Simpler to build own API completions.

* Compared with `*.sublime-completions` files:

    This package will avoid `*.sublime-completions` override word-completion wrongly:

    * **In English**:

        It seems like when scope matched would be override word-completions provide by sublime itself. refer to issue#3.

    * **In Chinese**:

        一但 scope 匹配成功之後，雖然自製的 auto-completion 能夠順利工作；但是它也會覆蓋掉原本 word-completion。因此，只有在自製的辭彙的 scope 完全沒匹配時，才會正常地顯示原本的 word-completion，而不是將它們融合在一起顯示。


## APIs

#### JavaScript and jQuery 1.9

![](https://raw.github.com/Pleasurazy/Sublime-Better-Completion/master/README/JavaScript-and-jQuery/demo1.gif)

![](https://raw.github.com/Pleasurazy/Sublime-Better-Completion/master/README/JavaScript-and-jQuery/static3.jpg)

#### Twitter Bootstrap 2 and 3

![](https://raw.github.com/Pleasurazy/Sublime-Better-Completion/master/README/bootstrap-demo/demo1.gif)

![](https://raw.github.com/Pleasurazy/Sublime-Better-Completion/master/README/bootstrap-demo/static3.jpg)


## Setting

API files is contains the *keyword* such as `html`, `jquery`, `myglossary` with lowercase as filename `sublime-better-completion-api-${filename}.sublime-settings` place in `/packages/User/` (your own) or `/packages/${this-package}/sublime-completions/` (package build-in).

```json
{
  // --------------------
  // sublime-better-completions-Package
  // --------------------
  // API files is contains the *keyword* such as `html`, `jquery`, `myglossary` with lowercase as filename `sublime-better-completion-api-${filename}.sublime-settings` place in `/packages/User/` (your own) or `/packages/${this-package}/sublime-completions/` (package build-in).
  // After you enable, disable or added new your own completions, you might need restart your Sublime Text Editor.
  //
  // Your own setting file `sublime-better-completion-setting.sublime-settings` need to place in `/packages/User/` and contains all your api setting property that you want to enable.
  //
  // --------------------
  // APIs Setup
  // --------------------
  // `true` means enable it.
  // `false` means disable it.
  "completion_active_list": {
    // build-in completions
    "gruntjs-plugins": false,
    "html": false,
    "javascript": false,
    "jquery": false,
    "jquery-sq": false, // Single Quote
    "php": false,
    "phpci": false,
    "twitter-bootstrap": false,
    "twitter-bootstrap3": false,
    "underscorejs": false,

    // Your own completions?
    "my-angularjs": false,
    "my-glossary": false,
    "my-html": false,
    "my-javascript": false
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

    ![](https://raw.github.com/Pleasurazy/Sublime-Better-Completion/master/README/UsingPackageControl.jpg)

    Waiting download.

    Happy programming.

---

* Manual Install Instructions

    Please refer to [this-package/Install_instructions.md].

[this-package/Install_instructions.md]: https://github.com/Pleasurazy/Sublime-Better-Completion/blob/master/Install_instructions.md


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