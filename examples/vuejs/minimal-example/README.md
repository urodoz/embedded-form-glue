# Payment form from scratch with vue-cli

This page explains how-to create a dynamic payment form from scratch using
vue.js and vue-cli and embedded-form-glue library.

## Requirements

You need to install [node.js LTS version](https://nodejs.org/en/).

Next ,install vue-cli:

```bash
npm install -g @vue/cli
# OR
yarn global add @vue/cli
```

More details on [vue-cli web-site](https://cli.vuejs.org/guide/installation.html).

## Create the project

First, create the vue-cli HelloWorld project:

```sh
vue create minimal-example
```

Add the dependency with yarn:

```bash
cd reate minimal-example
# with npm
npm install --save @lyracom/embedded-form-glue
# or yarn
yarn add @lyracom/embedded-form-glue
```

Run and test it:

```sh
npm run serve
```

see the result on http://localhost:8080/

For more  details, see https://cli.vuejs.org/guide/creating-a-project.html

## add the payment form

First you have to add 2 theme files:

| File                  | Description
| --------------------- | ---------------------
| classic-reset.css     | default style applied before the [Lyra Javascript Library][JS Link] is loaded
| classic.js            | theme logic, like waiting annimation on submit button, ...

Add them in public/index.html in the the HEAD section:

```javascript
<!-- theme and plugins. should be loaded in the HEAD section -->
<link rel="stylesheet"
href="https://api.lyra.com/static/js/krypton-client/V4.0/ext/classic-reset.css">
<script
    src="https://api.lyra.com/static/js/krypton-client/V4.0/ext/classic.js">
</script>
```

For more information about theming, take a look to [Lyra theming documentation][JS Themes]

Update the src/App.vue template to:

```html
<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <HelloWorld msg="Welcome to Your Vue.js App"/>
  </div>
</template>
````

Update the src/components/HelloWorld.vue template to:

```html
<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
      <div class="container">
        <div id="myPaymentForm"></div>
      </div>
  </div>
</template>
````

Your payment form will be added to #myPaymentForm element.

Update the src/components/HelloWorld.vue styles to:

```html
<style scoped>
.container {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
}
</style>
```

Import the embedded-form-vue component and create the payment form adding
the following in src/components/HelloWorld.vue on the mounted property of the application:

```javascript
/* import embedded-form-glue library */
import KRGlue from "@lyracom/embedded-form-glue";

/* define the public key, you should use your personal key */
export default {
    (...)
    mounted() {
        const publicKey = '69876357:testpublickey_DEMOPUBLICKEY95me92597fd28tGD4r5';

        KRGlue.loadLibrary('https://api.lyra.com', publicKey) /* Load the remote library */
              .then(({KR}) => KR.setFormConfig({       /* set the minimal configuration */
                formToken: 'DEMO-TOKEN-TO-BE-REPLACED',
              }))
              .then(({KR}) => KR.addForm('#myPaymentForm')) /* create a payment form */
              .then(({KR, result}) => KR.showForm(result.formId));  /* show the payment form */
    }
    (...)
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
cd examples/vuejs/minimal-example
npm install
npm run serve
```

[JS Link]: https://lyra.com/fr/doc/rest/V4.0/javascript
[JS Themes]: https://lyra.com/fr/doc/rest/V4.0/javascript/features/themes.html
[JS quick start]: https://lyra.com/fr/doc/rest/V4.0/javascript/quick_start_js.html
[JS integration guide]: https://lyra.com/fr/doc/rest/V4.0/javascript/guide/start.html
[REST API]: https://lyra.com/fr/doc/rest/V4.0/api/reference.html
