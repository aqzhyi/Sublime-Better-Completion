## Sublime API Completions Package

Lightweight, not complex, hint, simply auto-completion. There are no complex snippets, it's just completions.


## Features

手刻的浪漫

Make your Sublime text editor auto-completion support JavaScript, jQuery functions and bootstrap classes hint.

![](https://raw.github.com/Pleasurazy/Sublime-JavsScript-API-Completions/master/README/demo-animation.gif)

![](https://raw.github.com/Pleasurazy/Sublime-JavsScript-API-Completions/master/README/demo1.jpg)

![](https://raw.github.com/Pleasurazy/Sublime-JavsScript-API-Completions/master/README/demo2.jpg)

![](https://raw.github.com/Pleasurazy/Sublime-JavsScript-API-Completions/master/README/demo3.jpg)

![](https://raw.github.com/Pleasurazy/Sublime-JavsScript-API-Completions/master/README/demo4.jpg)

![](https://raw.github.com/Pleasurazy/Sublime-JavsScript-API-Completions/master/README/demo5.jpg)

![](https://raw.github.com/Pleasurazy/Sublime-JavsScript-API-Completions/master/README/bootstrap-demo1.jpg)

![](https://raw.github.com/Pleasurazy/Sublime-JavsScript-API-Completions/master/README/bootstrap-demo2.jpg)

![](https://raw.github.com/Pleasurazy/Sublime-JavsScript-API-Completions/master/README/bootstrap-demo3.jpg)


## Different

* with `*.sublime-completions` files

  It seems like when scope matched would be override completions provide by sublime itself.

* with `*.sublime-snippet` files

  More simpler, more lightweight with **Sublime API Completions Package**.


## Setting

```json
{
  "completion_active_list": {
    // As filename within `/sublime-completions/API-completions-${filename}.sublime-settings`.
    "jQuery": true,
    "JavaScript": true,
    "twitter-bootstrap": true
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

* Through the **Package control** to install.

  ![](https://raw.github.com/Pleasurazy/Sublime-JavsScript-API-Completions/master/README/through_package_control_install.jpg)

* Waiting download from **Github**.

* Happy programming.


## Relevant issues

> How to trigger completion hint when every typing?

Open file `Packages/User/Preferences.sublime-settings` or click `Setting - User` from menu. In my case, I just setup the `auto_complete_triggers` property as follow:

```json
  "auto_complete_triggers":
  [
    {
      "characters": "qazwsxedcrfvtgbyhnujmikolpQAZWSXEDCRFVTGBYHNUJMIKOLP",
      "selector": "text, source, meta, string, punctuation, constant"
    }
  ],
```

It will active most of scope triggers and most of characters.