Sublime Better Completion Package
===============================

手刻的浪漫

This package aim at provide a simpler way to build own auto-completions and avoid `*.sublime-completions` override word-completion wrongly in some circumstance (issue#3).

**auto-completion** is lightweight, easier, simpler than **snippets**.

This package also provide several APIs completions such as JavaScript, jQuery, Lodash, Underscore, HTML5, CSS3 and Bootstrap Classes, React.js, etc


## Compatible

Should be working fine with ST2 and ST3.

2015/02

- Sublime Text 3 with MAC OS X 10.10.2 using Package Control **tested**!

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

        It seems like when scope matched would be override word-completions provide by sublime itself. refer to [issue#3](https://github.com/Pleasurazy/Sublime-Better-Completion/issues/3).

    * **In Chinese**:

        一但 scope 匹配成功之後，自製的 auto-completion 雖然能夠順利工作；但是它也會覆蓋掉原本 word-completion。因此，只有在自製的辭彙的 scope 完全沒匹配時，才會正常地顯示原本的 word-completion，卻沒有將它們融合在一起顯示。這使得可被選擇的 completions 將會有所遺失。


## Preview

Support APIs see Setting section.

#### JavaScript and jQuery 1.9

![](https://raw.github.com/Pleasurazy/Sublime-Better-Completion/master/README/JavaScript-and-jQuery/demo1.gif)

![](https://raw.github.com/Pleasurazy/Sublime-Better-Completion/master/README/JavaScript-and-jQuery/static3.jpg)

#### Twitter Bootstrap 2 and 3

![](https://raw.github.com/Pleasurazy/Sublime-Better-Completion/master/README/bootstrap-demo/demo1.gif)

![](https://raw.github.com/Pleasurazy/Sublime-Better-Completion/master/README/bootstrap-demo/static3.jpg)


## Setting

Make your own API files that contains *keyword* such as `html`, `jquery`, `myglossary` as filename `sbc-api-${filename}.sublime-settings` and place them in `/packages/User/`.

```js
{
  // --------------------
  // sublime-better-completions-Package (sbc package)
  // --------------------
  // API files is contains the *keyword* such as `html`, `jquery`, `myglossary` with lowercase as filename `sbc-api-${filename}.sublime-settings` place in `/packages/User/` (your own) or `/packages/${this-package}/sublime-completions/` (package build-in).
  // After you enable, disable or added new your own completions, you might need restart your Sublime Text Editor.
  //
  // Your own setting file `sbc-setting.sublime-settings` need to place in `/packages/User/` and contains all your api setting property that you want to enable.
  //
  // --------------------
  // APIs Setup
  // --------------------
  // `true` means enable it.
  // `false` means disable it.
  "completion_active_list": {
    // build-in completions
    "css-properties": false,
    "gruntjs-plugins": false,
    "html": false,
    "lodash": false,
    "javascript": false,
    "jquery": false,
    "jquery-sq": false, // Single Quote
    "php": false,
    "phpci": false,
    "sql": false,
    "twitter-bootstrap": false,
    "twitter-bootstrap-less-variables": false,
    "twitter-bootstrap3": false,
    "twitter-bootstrap3-sass-variables": false,
    "underscorejs": false,
    "react": false,

    // Your own completions?
    // ~/Library/Application\ Support/Sublime\ Text\ 3/Packages/User/sbc-api-my-angularjs.sublime-settings
    "my-angularjs": false,

    // ~/Library/Application\ Support/Sublime\ Text\ 3/Packages/User/sbc-api-my-glossary.sublime-settings
    "my-glossary": false,

    // ~/Library/Application\ Support/Sublime\ Text\ 3/Packages/User/sbc-api-my-html.sublime-settings
    "my-html": false,

    // ~/Library/Application\ Support/Sublime\ Text\ 3/Packages/User/sbc-api-my-javascript.sublime-settings
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
    * https://www.scaler.com/topics/javascript/

* Underscore 1.5.1

    * http://underscorejs.org/

* Twitter Bootstrap Version 2 and 3

    * http://getbootstrap.com/
    * http://twitter.github.io/bootstrap/index.html
    * https://github.com/twbs/bootstrap-sass

* HTML / HTML5

    * http://devdocs.io/html-html5/

* Lodash 3.3.0

    * http://devdocs.io/lodash/

## Installation

* Using **Package Control** to install.

    ![](https://raw.github.com/Pleasurazy/Sublime-Better-Completion/master/README/UsingPackageControl.jpg)

    Waiting download.

    <kbd>CTRL+SHIFT+P</kbd> or <kbd>CMD+SHIFT+P</kbd> type in `sbc settings user` to open user setting file

    Paste setting json. (see Setting section)

    Enable your favorite APIs.

    Restart your sublime text app.

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
