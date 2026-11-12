# Falamos — site

Static site on GitHub Pages: https://falamos-app.github.io

`config.json` is read by every installed app (at launch and on return, at most every 30 minutes):

- `ios` / `android`:
  - `min` — older versions show a full screen «update to continue» (only for backend changes old versions can't handle);
  - `recommended` — older versions get a quiet card on the Today screen, closed for good per version;
  - `storeUrl` — where «Update» leads (`https://apps.apple.com/app/id…`, `https://play.google.com/store/apps/details?id=com.falamos.app`);
  - `notes` — what the new version brings: `{ "uk": "…", "en": "…" }`.
- `notice` — a note for everyone on the Today screen and on the photo screen when the server fails:
  `{ "id": "pg-upgrade-1", "text": { "uk": "…", "en": "…" }, "until": "2026-12-01T14:00:00Z" }`.
  A new `id` shows it again to those who closed the previous one; after `until` it is gone by itself.

A broken file is ignored by the app (it keeps the last good one), but check JSON before saving.
