# 🎵 SoundSpace — Your Music Site

A 2-page music website built to learn how websites work.
**100% free to host on GitHub Pages.**

---

## 📁 Files

```
music-site/
├── index.html   ← Page 1: registration form (the "front door")
├── music.html   ← Page 2: music hub (the "main room")
└── README.md    ← this file
```

---

## 🚀 How to put it online FREE (GitHub Pages)

### Step 1 — Create a GitHub account
Go to https://github.com and sign up (free).

### Step 2 — Create a new repository
1. Click the **+** icon → "New repository"
2. Name it: `my-music-site` (or anything you like)
3. Set it to **Public**
4. Click **Create repository**

### Step 3 — Upload your files
1. On your new repo page, click **"uploading an existing file"**
2. Drag and drop `index.html` and `music.html`
3. Scroll down and click **"Commit changes"**

### Step 4 — Enable GitHub Pages
1. Go to **Settings** (top menu of your repo)
2. Scroll to **Pages** (left sidebar)
3. Under "Branch", select **main** → **/ (root)**
4. Click **Save**

### Step 5 — Your site is live! 🎉
After ~1 minute, your site will be at:
```
https://YOUR-USERNAME.github.io/my-music-site/
```

---

## 🧠 How the "database" works

This site uses **localStorage** — storage built into every web browser.

| Action | What happens |
|--------|-------------|
| User fills the form | Data saved to localStorage as JSON |
| User revisits | JS reads localStorage → skips the form |
| User logs out | Session key removed (list stays) |
| Open DevTools → Application → Local Storage | See raw data! |

**The limitation:** localStorage only stores data in that browser, on that device.
To make a real shared database, the next step is **Firebase** or **Supabase** (both free tiers).

---

## 📈 How to scale this later

| Level | What to add | Cost |
|-------|------------|------|
| 1 (now) | localStorage | Free |
| 2 | Firebase Realtime DB | Free tier |
| 3 | Supabase (Postgres) | Free tier |
| 4 | Your own server (Node.js) | ~$5/month |

---

## 🛠 Things to try as you learn

- Change the `--accent` color in the CSS `:root` block
- Add a new genre card in `music.html`
- Add a new track row to the track list
- Link a real `.mp3` file using the HTML `<audio>` element
- Open browser DevTools (F12) → Console → watch the JS logs
