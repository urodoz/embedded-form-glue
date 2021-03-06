# Payment form from scratch with angular-cli

This page explains how-to create a dynamic payment form from scratch using
Angular and angular-cli and embedded-form-glue library.

## Requirements

You need to install [node.js LTS version](https://nodejs.org/en/).

Next ,install vue-cli:

```bash
npm install -g @angular/cli
# OR
yarn global add @angular/cli
```

More details on [angular-cli web-site](https://angular.io/guide/quickstart).

## Create the project

First, create the angular-cli minimal-example project (with default options):

```sh
ng new minimal-example
```

Add the dependency with yarn:

```bash
cd minimal-example
# with npm
npm install --save @lyracom/embedded-form-glue
# or with yarn
yarn add @lyracom/embedded-form-glue
```

Run and test it (in minimal-example folder):

```sh
ng serve --open
```

see the result on http://localhost:4200/

## add the payment form

First you have to add 2 theme files:

| File                  | Description
| --------------------- | ---------------------
| classic-reset.css     | default style applied before the [Lyra Javascript Library][JS Link] is loaded
| classic.js            | theme logic, like waiting annimation on submit button, ...

Add them in src/index.html in the the HEAD section:

```javascript
<!-- theme and plugins. should be loaded in the HEAD section -->
<link rel="stylesheet"
href="https://api.lyra.com/static/js/krypton-client/V4.0/ext/classic-reset.css">
<script
    src="https://api.lyra.com/static/js/krypton-client/V4.0/ext/classic.js">
</script>
```

For more information about theming, take a look to [Lyra theming documentation][JS Themes]

Change the src/app/app.component.html template to:

```html
<div class="form">
<h1>{{ title }}</h1>
  <div class="container">
    <div id="myPaymentForm"></div>
  </div>
</div>
````

Your payment form will be added to #myPaymentForm element.

Update the src/app/app.component.css styles to:

```css
h1 {
  margin: 40px 0 20px 0;
  width: 100%;
  text-align: center;
}

.container {
  display: flex;
  justify-content: center;
}
```

Update the default component src/app/app.component.ts to:

```js
import { Component, OnInit } from '@angular/core';
import KRGlue from "@lyracom/embedded-form-glue";

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  title = 'minimal-example';

  ngOnInit() {
    const publicKey = '69876357:testpublickey_DEMOPUBLICKEY95me92597fd28tGD4r5';
    const formToken = 'DEMO-TOKEN-TO-BE-REPLACED';

    KRGlue.loadLibrary('https://api.lyra.com', publicKey) /* Load the remote library */
          .then(({KR}) => KR.setFormConfig({                  /* set the minimal configuration */
            formToken: formToken,
          }))
          .then(({KR}) => KR.addForm('#myPaymentForm'))             /* add a payment form  to myPaymentForm div*/
          .then(({KR, result}) => KR.showForm(result.formId));      /* show the payment form */
  }

}
```

## your first transaction

The payment form is up and ready, you can try to make a transaction using
a test card with the debug toolbar (at the bottom of the page).

If you try to pay, you will have the following error: **CLIENT_998: Demo form, see the documentation**.
It's because the **formToken** you have defined using **KR.setFormConfig** is set to **DEMO-TOKEN-TO-BE-REPLACED**.

you have to create a **formToken** before displaying the payment form using Charge/CreatePayment web-service.
For more information, please take a look to:

* [Embedded form quick start][JS quick start]
* [embedded form integration guide][JS integration guide]
* [Payment REST API reference][REST API]

## Run it from github

You can try the current example from the current github repository doing:

```sh
cd examples/angular/minimal-example
npm install
npm run start
```

[JS Link]: https://lyra.com/fr/doc/rest/V4.0/javascript
[JS Themes]: https://lyra.com/fr/doc/rest/V4.0/javascript/features/themes.html
[JS quick start]: https://lyra.com/fr/doc/rest/V4.0/javascript/quick_start_js.html
[JS integration guide]: https://lyra.com/fr/doc/rest/V4.0/javascript/guide/start.html
[REST API]: https://lyra.com/fr/doc/rest/V4.0/api/reference.html
