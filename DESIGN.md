---
name: Falamos
description: European Portuguese for people who moved to Portugal. The site is a tram stop in the app's «B · Eléctrico» world.
colors:
  tram-yellow: "#FFCC1A"
  tram-yellow-night: "#F0C02A"
  ink: "#111111"
  ink-muted: "#4D4120"
  board-white: "#FFFFFF"
  paper: "#FCF1D4"
  rail: "#E2D8B6"
  hover-cream: "#FFF3C4"
  sign-muted: "#FFE58A"
  highlighter: "#FFE27A"
  graphite-ground: "#1E1D1A"
  graphite-board: "#2A2925"
  graphite-paper: "#24231F"
  graphite-ink: "#EDEAE3"
  graphite-muted: "#A9A59C"
  graphite-line: "#45423C"
  graphite-rail: "#3A3833"
  graphite-hover: "#3A3420"
  graphite-sign-ink: "#141311"
  graphite-sign-muted: "#4E400C"
  shadow-night: "#0A0A09"
  night-sky: "#0C0B0A"
  line-1-blue: "#2B63C6"
  line-2-red: "#C2381F"
  line-9-green: "#17845A"
typography:
  display:
    fontFamily: "Bricolage, Geologica, system-ui, sans-serif"
    fontSize: "clamp(56px, 6vw, 76px)"
    fontWeight: 800
    lineHeight: 0.95
    letterSpacing: "-0.03em"
  display-terminus:
    fontFamily: "Bricolage, Geologica, system-ui, sans-serif"
    fontSize: "clamp(64px, 11vw, 150px)"
    fontWeight: 800
    lineHeight: 0.9
    letterSpacing: "-0.04em"
  display-pair:
    fontFamily: "Bricolage, Geologica, system-ui, sans-serif"
    fontSize: "clamp(36px, 6.2vw, 84px)"
    fontWeight: 800
    lineHeight: 1.04
    letterSpacing: "-0.035em"
  destination:
    fontFamily: "Bricolage, Geologica, system-ui, sans-serif"
    fontSize: "clamp(26px, 2.6vw, 36px)"
    fontWeight: 800
    lineHeight: 1.05
    letterSpacing: "-0.02em"
  phrase:
    fontFamily: "Bricolage, Geologica, system-ui, sans-serif"
    fontSize: "20px"
    fontWeight: 700
    lineHeight: 1.3
  line-number:
    fontFamily: "Bricolage, Geologica, system-ui, sans-serif"
    fontSize: "26px"
    fontWeight: 800
    lineHeight: 1
  headline:
    fontFamily: "Geologica, system-ui, sans-serif"
    fontSize: "clamp(28px, 3.4vw, 44px)"
    fontWeight: 700
    lineHeight: 1.12
    letterSpacing: "-0.015em"
  title:
    fontFamily: "Geologica, system-ui, sans-serif"
    fontSize: "22px"
    fontWeight: 700
    lineHeight: 1.3
  body:
    fontFamily: "Geologica, system-ui, sans-serif"
    fontSize: "17px"
    fontWeight: 400
    lineHeight: 1.5
  body-lede:
    fontFamily: "Geologica, system-ui, sans-serif"
    fontSize: "19px"
    fontWeight: 400
    lineHeight: 1.5
  label:
    fontFamily: "Geologica, system-ui, sans-serif"
    fontSize: "12px"
    fontWeight: 700
    lineHeight: 1
    letterSpacing: "0.06em"
rounded:
  chip: "6px"
  notice: "12px"
  number: "14px"
  plate: "16px"
  bubble: "18px"
  card: "20px"
  sign: "22px"
  pill: "999px"
spacing:
  gutter: "clamp(16px, 4vw, 56px)"
  wide: "1240px"
  row-pad: "22px 26px"
  section: "clamp(64px, 10vw, 128px)"
components:
  sign:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.tram-yellow}"
    rounded: "{rounded.sign}"
    padding: "30px 30px 28px"
  sign-night:
    backgroundColor: "{colors.tram-yellow-night}"
    textColor: "{colors.graphite-sign-ink}"
  departures-board:
    backgroundColor: "{colors.board-white}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sign}"
  board-row:
    padding: "{spacing.row-pad}"
  board-row-hover:
    backgroundColor: "{colors.hover-cream}"
  line-number:
    textColor: "{colors.board-white}"
    typography: "{typography.line-number}"
    rounded: "{rounded.number}"
    size: "60px"
  line-number-a2:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.tram-yellow}"
  store-plate:
    textColor: "{colors.tram-yellow}"
    rounded: "{rounded.plate}"
    padding: "11px 14px"
  card:
    backgroundColor: "{colors.board-white}"
    textColor: "{colors.ink}"
    rounded: "{rounded.card}"
  tag-chip:
    backgroundColor: "{colors.tram-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.label}"
    rounded: "{rounded.chip}"
    padding: "5px 8px"
  word-chip:
    backgroundColor: "{colors.tram-yellow}"
    textColor: "{colors.ink}"
    rounded: "{rounded.pill}"
    padding: "7px 14px"
  bubble-them:
    backgroundColor: "{colors.board-white}"
    textColor: "{colors.ink}"
    rounded: "{rounded.bubble}"
    padding: "12px 16px"
  bubble-me:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.board-white}"
    rounded: "{rounded.bubble}"
    padding: "12px 16px"
  option:
    backgroundColor: "{colors.board-white}"
    textColor: "{colors.ink}"
    rounded: "{rounded.number}"
    padding: "10px 14px"
  option-right:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.tram-yellow}"
  language-switch-active:
    backgroundColor: "{colors.tram-yellow}"
    textColor: "{colors.ink}"
    rounded: "{rounded.pill}"
    padding: "5px 12px"
---

# Design System: Falamos

This is the site's record of «B · Eléctrico», the visual world it shares with the Falamos mobile app. The app's theme files are the source of truth for colour roles, radii, edges and type roles (`src/theme/colors.ts`, `metrics.ts` and `typography.ts` in the app repo). When a role changes there, change it here and in `index.html`'s `:root` in the same pass. Divergences that ship today are listed under Colors.

## Overview

**Creative North Star: "The Tram Stop"**

Falamos is a stop on a Lisbon or Porto tram line, and the lines leaving it are the newcomer's real worries: Finanças, renting, the doctor and the A2 exam. Every surface is a piece of street furniture. There is an ink route sign with yellow lettering, a white departures board with a 2px ink edge and a hard offset shadow, square metro line numbers, and a rail that runs down the page and links the stops. By day the ground is tram yellow. By night it is warm graphite, and yellow moves onto the one thing that should glow, the sign.

Density is low and the type is loud. Portuguese words are set large in Bricolage Grotesque because the language is the product. Interface copy is set in Geologica, plain and warm. Depth is physical, never atmospheric: boards sit on the ground and throw a hard, unblurred shadow down and to the right. The night-tram video is the only moving part of the system. Everything else stays still apart from hover feedback.

The page speaks one language at a time, English by default and Ukrainian at `#uk`. Both versions are in the markup, so a switch never reflows the layout into a different design.

**Key Characteristics:**
- Tram-yellow day ground, warm-graphite night ground, chosen by `prefers-color-scheme`.
- Every edge is 2px, every shadow is a hard offset with zero blur.
- Square line numbers in metro colours stand for the course's lines.
- Bricolage only on Portuguese text, Geologica for everything in the interface language.
- One rail on the left axis (the pole in the header, then the line through the stops).
- Bilingual EN/UK with both strings in the markup and `[data-l]` switching.

## Colors

A two-theme palette of tram yellow and ink, with a set of metro line colours used only as line identity.

### Primary
- **Tram Yellow** (tram-yellow): the day ground of the whole page, the lettering on the ink sign, the right answer and the A2 number on ink, the tag chip, and the word chips. Yellow is never text on white or on the yellow ground. It is text only on ink.
- **Night Tram Yellow** (tram-yellow-night): the dimmed yellow of the night theme. It becomes the sign and terminus ground, the A2 number, the right answer and the board header lettering, so the one glowing block on a dark page is the sign.

### Secondary
- **Line 1 Blue** (line-1-blue), **Line 2 Red** (line-2-red), **Line 9 Green** (line-9-green): square line numbers and the stop markers on the rail, with white numerals. They come from the app's `LINE_COLORS`, which also holds purple (#7A3FC2), amber (#A3520A) and teal (#1C7A92) for lines the site doesn't show yet. A line keeps its colour by day and by night. The red also draws the line strip's stops in the renting demo.

### Neutral
- **Ink** (ink): text, every 2px edge, every hard shadow, the sign, the departures-board header, and the learner's own speech bubble, by day.
- **Board White** (board-white): boards, cards, the other speaker's bubble, answer options, and the letter.
- **Warm Paper** (paper): the quiet strip at the foot of the board, the CIPLE notice, and the exam's part list.
- **Rail Cream** (rail): the hairline inside a letter or under the line strip, and the rail at night.
- **Hover Cream** (hover-cream): a board row under the pointer.
- **Ink Muted** (ink-muted): worries on the board, ledes, body text in the stops and translations. It is a warm olive-brown on the site (see drift below).
- **Sign Muted** (sign-muted): secondary text on the ink sign and terminus, and translations in the learner's bubble.
- **Highlighter** (highlighter): marks the words the app picks out of a photographed letter.
- **Graphite family** (graphite-ground, graphite-board, graphite-paper, graphite-ink, graphite-muted, graphite-line, graphite-rail, graphite-hover, graphite-sign-ink, graphite-sign-muted, shadow-night): the night theme, role for role. The ground is lifted off pure black so the near-black shadow still reads as depth.
- **Night Sky** (night-sky): the band behind the tram video, in both themes.

### Named Rules
**The Yellow-on-Ink Rule.** Tram yellow is a ground or a fill. As text it appears only on ink by day (or on night graphite). It is never text on white or on the yellow ground.

**The Lines Are Identity Rule.** Metro colours mark a course line and nothing else. They are never a decorative accent, a button, or a section background.

**The Mirror Rule.** Colour values are the app's roles. A new colour enters the app's `colors.ts` first, or not at all.

**Shipping drift, not canon.** The site's muted text is #4D4120 where the app's `inkMuted` is #4A4A4A. The night word chip uses graphite-hover with yellow lettering where the app's night `chip` is #141311. Several components also restate ink and yellow as literal hex in their night overrides instead of reading the role variables. Reconcile these with the app the next time the theme is touched. Don't copy them into new surfaces.

## Typography

**Portuguese Font:** Bricolage Grotesque 700/800, self-hosted as "Bricolage" (falls back to Geologica, then system-ui)
**Interface Font:** Geologica 400/600/700, self-hosted (falls back to system-ui)

**Character:** The two families split by language, not by size. Bricolage is a quirky, condensed-feeling grotesque that makes every Portuguese word look like a destination on a route board. Geologica is a calm, round-shouldered sans with Cyrillic, which carries both interface languages.

### Hierarchy
- **Display** (800, clamp 56–76px, 0.95, -0.03em): the word «Falamos» on the stop sign.
- **Display Terminus** (800, clamp 64–150px, 0.9, -0.04em): «Falamos!» at the terminus.
- **Display Pair** (800, clamp 36–84px, 1.04, -0.035em): the struck-out Brazilian and the kept European pairs.
- **Destination** (800, clamp 26–36px, 1.05, -0.02em): a line's Portuguese destination on the departures board.
- **Phrase** (700, 20px, 1.3): dialogue lines, exam questions, and letter text (16px), all in Portuguese.
- **Line Number** (Bricolage 800, 26px; 20–28px by context): the numerals in line squares.
- **Headline** (Geologica 700, clamp 28–44px, 1.12, -0.015em, balanced wrap, max 22ch): section titles. Stop titles run at clamp 27–40px/1.14, and any Portuguese phrase inside a title switches to Bricolage 800.
- **Title** (Geologica 700, 22px, 1.3): the tagline on the sign.
- **Body** (Geologica 400, 17px/1.5, or 16px on phones): default text. The lede is 19px and stop bodies are 18px/1.55, held to 46–52ch.
- **Label** (Geologica 700, 12px, 0.06em, uppercase): «Coming soon», the «Example» chip, and speaker names in dialogue. The board header uses the same treatment at 15px.

### Named Rules
**The Bricolage-Is-Portuguese Rule.** Bricolage is applied only through `[lang="pt"]`. It has no Cyrillic, so no English or Ukrainian string is ever set in it, however display-sized.

**The One Language at a Time Rule.** Every interface string ships as an `en`/`uk` pair (`data-l`). English shows by default, `html.uk` swaps to Ukrainian, and Portuguese is shared by both.

## Layout

The page is one vertical ride: the stop (sign and departures board), the night tram, the pt-PT pairs, four stops on a rail, and the terminus. Content sits in a 1240px column with a fluid gutter (clamp 16–56px). Sections breathe at clamp 64–128px vertically.

On desktop the header is a two-column grid with the sign in a 300–400px column and the board taking the rest. A 14px ink pole runs the full height of the header behind the sign. The stops are a three-column grid (64px number column, then text 5fr and demo 6fr) hung on a 6px rail at the same left axis.

At 960px and below the header stacks into sign then board, and the demo moves under the text. At 600px and below the pole and rail narrow to 12px and 5px, the line squares shrink to 44–48px, the board drops its arrow column and Portuguese subtitle, the tram video crops to 4:3, and the pairs stack.

**The One Axis Rule.** The pole, the rail and the terminus pole share the left axis, so the reader always rides the same line down the page, from the first stop to the end of the line.

## Elevation & Depth

Depth is hard and physical. Boards, cards and the sign sit on the ground and cast a solid offset shadow down and to the right, in ink by day and in near-black (shadow-night) by night. Nothing is blurred, glowing or glassy.

### Shadow Vocabulary
- **Street furniture** (`box-shadow: 8px 8px 0 var(--shadow)`, 6px on phones): the stop sign and the departures board.
- **Card** (`box-shadow: 6px 6px 0 var(--shadow)`): demo cards and the photographed letter.
- **Small** (`box-shadow: 3px 3px 0 var(--shadow)`): speech bubbles.
- **Ring** (`box-shadow: 0 0 0 2px var(--line)` with a 3px ground-coloured border): line squares on the rail, cut out of it like a stop marker.

### Named Rules
**The Hard Shadow Rule.** Shadows have zero blur and come in three steps (8, 6 and 3). They are the world's material, and the app uses the same device for cards and controls.

## Shapes

Corners are generously rounded but never pill-soft on containers: 22px for the sign and board, 20px for cards, 18px for bubbles, 16px for plates, 14px for line squares and options, 12px for notices, and 6px for the tag chip. Pills (999px) are kept for chips, the language switch, the exam parts and the pause button. A bubble's corner nearest the speaker drops to 6px. Edges are always 2px (`--line`). The only deliberate tilt is the photographed letter at -1.6deg, which reads as a real sheet of paper.

## Components

### Stop Sign
An ink route board with yellow lettering (at night, a yellow board with graphite lettering). It holds the app mark, the language switch, «Falamos» in Display, the tagline, a short description in sign-muted, and two store plates. It uses 22px corners, 30px padding and the 8px street-furniture shadow. The terminus is the same sign hung on the pole at the end of the line: a header strip («Fim da linha» in Bricolage, «End of the line» / «Кінцева» in the label role) over «Falamos!», the note and the store plates; the footer sits on the ground below.

### Departures Board
A white board with a 2px edge, 22px corners and the 8px shadow. The header is ink with yellow lettering: a 15px uppercase Geologica label on the left and «Português de Portugal» in Bricolage on the right. Each row is a link: a line square, the destination in Bricolage, the worry in muted Geologica, and an arrow. Rows are divided by 2px rules. On hover a row fills with hover-cream and the arrow slides 5px right (0.25s, `cubic-bezier(.2,.8,.2,1)`). Focus draws the global 3px ink outline inset by 5px. A paper-coloured foot lists the other lines.

### Line Square
A square with 14–16px corners, a metro-colour fill, and a white Bricolage 800 numeral. The A2 square is ink with yellow (yellow with graphite at night). On the rail it gets the ground-colour ring.

### Store Plate
Outlined in the sign's line colour, with 16px corners, a 22px phone icon, the store name, and a «Coming soon» pill label pushed to the right. It is not a link until the real store URL exists.

### Language Switch
A pill outline holding two 14px bold pills, EN and UA. The current one is filled with the sign text colour. It writes `#en`/`#uk` to the address with `replaceState`.

### Card
A white board with a 2px edge, 20px corners and a 6px shadow. It holds the demos: the explanation of a letter, the line strip, and the practice test.

### Chips
- **Word chip:** a pill on the yellow ground with a 2px edge, the Portuguese word in Bricolage 800 at 19px, and its gloss in 14px Geologica.
- **Tag chip:** a 6px-cornered yellow label with a 2px edge and Label type («Example»), marking demo content as an example.

### Speech Bubbles
White with an edge and a 3px shadow for the other speaker. The learner's own bubble is ink with white text and sign-muted translations. The Portuguese line is Bricolage 700 at 20px, the translation is Geologica 400 at 15px, and the speaker's corner drops to 6px.

### Answer Options
Rows with a 2px edge and 14px corners, Bricolage 700 at 18px, and a small 8px-cornered letter box. The right answer turns ink with yellow (yellow with graphite at night).

### Rail and Stops
A 6px rail runs down the page with stop sections hung on it. Each stop's stretch takes its line's colour (blue, red, green; the A2 stretch is the pole colour), as the course map in the app, and the last stretch runs on into the terminus pole. Inside the renting demo, a 4px rail in the line's colour carries 20px ring stops, filled once a stop is done.

### Night Tram
A full-width video on night-sky, bordered top and bottom by 2px. Its caption is a graphite pill of text, with a 46px round graphite pause button in night yellow next to it. The video plays only when it comes near the viewport and only without reduced motion. Otherwise the poster stays and the button offers to play.

## Do's and Don'ts

### Do:
- **Do** read colours from the role variables on `:root` and add a night value for every new role in the `prefers-color-scheme: dark` block.
- **Do** draw every edge at 2px and every shadow as a hard offset (8, 6 or 3px, zero blur).
- **Do** set Portuguese text with `lang="pt"` so it takes Bricolage, and give every interface string an `en` and a `uk` version.
- **Do** keep metro colours for line numbers and line rails only, with white numerals.
- **Do** mark demo content with the «Example» tag chip.
- **Do** keep the tram video the only moving element, honour reduced motion, and give it a pause control.
- **Do** change a colour role in the app's theme first, then mirror it here and in `index.html`.

### Don't:
- **Don't** set English or Ukrainian text in Bricolage. It has no Cyrillic.
- **Don't** put yellow text on white or on the yellow ground.
- **Don't** blur a shadow, add gradients or glass, or invent a fourth shadow step.
- **Don't** show store links, prices, ratings or download counts until they are real. Plates stay «Coming soon».
- **Don't** animate whole words on the board. A board-flip was tried and dropped because the tilt read as a glitch.
- **Don't** use a metro line colour as a decorative accent or a call to action.
