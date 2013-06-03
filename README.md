## JavaScript API

Lightweight, not complex, hint, simply completion. There are no complex snippets, it's just completions.

## Features
![](https://raw.github.com/Pleasurazy/Sublime-JavsScript-API-Completions/master/README/demo-animation.gif)

![](https://raw.github.com/Pleasurazy/Sublime-JavsScript-API-Completions/master/README/demo1.jpg)

![](https://raw.github.com/Pleasurazy/Sublime-JavsScript-API-Completions/master/README/demo2.jpg)

![](https://raw.github.com/Pleasurazy/Sublime-JavsScript-API-Completions/master/README/demo3.jpg)

![](https://raw.github.com/Pleasurazy/Sublime-JavsScript-API-Completions/master/README/demo4.jpg)

![](https://raw.github.com/Pleasurazy/Sublime-JavsScript-API-Completions/master/README/demo5.jpg)

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
      "characters": "<>\"'-_qazwsxedcrfvtgbyhnujmikolpQAZWSXEDCRFVTGBYHNUJMIKOLP",
      "selector": "text, source, meta, string, punctuation, constant"
    }
  ],
```

It will active most of scope triggers and most of characters.