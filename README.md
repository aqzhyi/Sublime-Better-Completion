## Sublime API Completions Package

Lightweight, not complex, hint, simply auto-completion. There are no complex snippets, it's just completions.


## Features

手刻的浪漫

Make your Sublime text editor auto-completion support JavaScript, jQuery API, bootstrap classes and custom completion hint.

#### JavaScript and jQuery

![](https://raw.github.com/Pleasurazy/Sublime-JavsScript-API-Completions/master/README/JavaScript-and-jQuery/demo1.gif)

![](https://raw.github.com/Pleasurazy/Sublime-JavsScript-API-Completions/master/README/JavaScript-and-jQuery/static1.jpg)

![](https://raw.github.com/Pleasurazy/Sublime-JavsScript-API-Completions/master/README/JavaScript-and-jQuery/static2.jpg)

![](https://raw.github.com/Pleasurazy/Sublime-JavsScript-API-Completions/master/README/JavaScript-and-jQuery/static3.jpg)

![](https://raw.github.com/Pleasurazy/Sublime-JavsScript-API-Completions/master/README/JavaScript-and-jQuery/static4.jpg)

![](https://raw.github.com/Pleasurazy/Sublime-JavsScript-API-Completions/master/README/JavaScript-and-jQuery/static5.jpg)

#### Twitter Bootstrap

![](https://raw.github.com/Pleasurazy/Sublime-JavsScript-API-Completions/master/README/bootstrap-demo/demo1.gif)

![](https://raw.github.com/Pleasurazy/Sublime-JavsScript-API-Completions/master/README/bootstrap-demo/static1.jpg)

![](https://raw.github.com/Pleasurazy/Sublime-JavsScript-API-Completions/master/README/bootstrap-demo/static2.jpg)

![](https://raw.github.com/Pleasurazy/Sublime-JavsScript-API-Completions/master/README/bootstrap-demo/static3.jpg)


## Why this package?

* Compared with `*.sublime-snippet` files:

  More simpler to build own API completions.

* Compared with `*.sublime-completions` files:
  
  * **speak in English**:

      It seems like when scope matched would be override completions provide by sublime itself. refer to issue #3.

  * **speak in Chinese**:

      一但 scope 匹配成功之後，雖然自製的 auto-completion 能更順利工作；但是它會覆蓋掉原本 auto-completion，只有在自製的辭彙完全沒匹配，才會顯示原本的 auto-completion，而不是將它們融合。


## Setting

```js
{
  "completion_active_list": {
    // As filename within `${package}/sublime-completions/API-completions-${filename}.sublime-settings`.
    "jQuery": true,
    "JavaScript": true,
    "twitter-bootstrap": true
  },
  "completion_active_extend_list": {
    // As filename within `/User/API-completions-myglossary.sublime-settings`.
    // "myglossary": true
  }
}
```


## API References

* jQuery Version: 1.9

  * http://oscarotero.com/jquery/

* JavaScript

  * http://overapi.com/javascript/
  * http://www.w3schools.com/js/

* Twitter Bootstrap Version 2.3.2

  * http://twitter.github.io/bootstrap/index.html


## Installation

* Using **Package control** to install.

  ![](https://raw.github.com/Pleasurazy/Sublime-JavsScript-API-Completions/master/README/UsingPackageControl.jpg)

* Waiting download from **Github**.

* Happy programming.


## Relevant issues

> How to trigger completion hint when every typing?

Open file `Packages/User/Preferences.sublime-settings` or click `Setting - User` from menu. In my case, I just setup the `auto_complete_triggers` property as follow:

```js
  "auto_complete_triggers":
  [
    {
      "characters": "qazwsxedcrfvtgbyhnujmikolpQAZWSXEDCRFVTGBYHNUJMIKOLP",
      "selector": "text, source, meta, string, punctuation, constant"
    }
  ],
```

It will active most of scope triggers and most of characters.