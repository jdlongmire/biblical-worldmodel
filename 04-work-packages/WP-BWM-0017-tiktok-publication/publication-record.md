# TikTok publication record

- Published: `2026-09-14 11:06 AM` (per TikTok Studio's post list; platform review cleared shortly after)
- Account: [oddxian](https://www.tiktok.com/@oddxian)
- Caption: "A doctor examining Adam the day after creation would see a grown man—and could be wrong about how he got there. Can a calculated age differ from actual history? Explore the Biblical WorldModel at worldmodel.thinxai.net/the-story/ #BiblicalWorldModel #FaithAndScience #Genesis #ChristianApologetics #oddXian"
- Public URL: https://www.tiktok.com/@oddxian/video/7685422904376380685
- AI-generated content disclosure: **On** (live post shows "Creator labeled as AI-generated")
- Disclose post content (brand/product/service): **Off**
- Audience control (18+): **Off**
- Who can see this post: **Everyone**
- Music copyright check: **No issues found**
- Content check lite: **No issues found** (standard "could still be removed if it violates Community Guidelines" disclaimer, not a flagged issue)
- Artifact SHA-256: `61680e9ad5e20c533e84179e3ae1886b0ea74cca689f43dbbe10182b6d042db8`

TikTok Studio displayed **Video published** immediately on posting. TikTok then ran its own standard platform-level content review, separate from the two pre-post checks above -- the post briefly showed **Only me** / **Content under review** in Studio's post list (TikTok's own FAQ: "all content goes through a review process before being posted... This applies to everyone and everything on our platform," typical turnaround "within 12 hours"). It cleared to **Everyone** within roughly two minutes.

Independent verification: opened `https://www.tiktok.com/@oddxian/video/7685422904376380685` directly in a fresh browser tab (not the Studio management view). The video plays publicly under the `oddXian` byline with the correct caption and visuals, and displays the "Creator labeled as AI-generated" badge.

## Production issue found and fixed during this run

The upload silently hung on a spinner indefinitely on the first two attempts. DevTools console showed `Failed to load resource: net::ERR_ACCESS_DENIED` on a `blob:https://www.tiktok.com/...` URL. First suspected Adblock Plus (which had full-site access) and disabled it -- no change, same error. Root cause: the source video file was owned `thinxai:thinxai` mode `600`, while the browser (and its renderer processes) run as user `jdlongmire` on this workstation -- the file dialog could still list and select the file, but the renderer process had no read permission on its bytes once it tried to actually stream them into the upload, surfacing as an opaque blob-access error rather than a clear permissions message. Fixed with `chmod 644` on the source file; the upload then completed normally.

Human-Curated, AI-Enabled (HCAE)
