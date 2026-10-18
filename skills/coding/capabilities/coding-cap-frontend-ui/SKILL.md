---
name: coding-cap-frontend-ui
description: "Frontend State, UX and Accessibility"
---

# Frontend State, UX and Accessibility

Map events, components, local/global state, effects, async requests, render and navigation. Check stale closures/state, loading/error/empty cases, cancellation, focus/keyboard, accessibility labels, responsive behavior and security of rendered content. Keep framework conventions, public props and design tokens stable. Add interaction tests for user-observable changes; use screenshot/visual regression tools only when available and executed. Do not report visual verification unless actual rendering was observed.

Read the owning Domain or Methodology when the concrete task triggers it. Preserve operator scope and explicit test evidence.

## Optional real-browser contract test

When browser automation is already available and authorized, test what users can observe: stable accessible roles/names/labels and rendered outcomes, not brittle CSS internals or guessed delays. Prefer framework auto-waiting or explicit event/state readiness; isolate browser contexts and clean up after each test. Exercise loading/error, keyboard/focus and negative access paths as relevant. Distinguish component test, real-browser E2E and manual visual review; do not claim rendered behavior from code inspection or a screenshot never captured. Do not install a browser/test runner or visit production sites without authorization.
