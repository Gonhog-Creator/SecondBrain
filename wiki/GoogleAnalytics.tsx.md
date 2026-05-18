# GoogleAnalytics.tsx

Source: junk_drawer/github/PersonalWebsite/src/components/GoogleAnalytics.tsx.txt

Category: [[github-code]]

## Summary
'use client'; import Script from 'next/script'; export function Analytics() { return ( <> <Script strategy="afterInteractive" src={`https://www.googletagmanager.com/gtag/js?id=G-MTR76P4RPF`}

## Full Content
'use client';

import Script from 'next/script';

export function Analytics() {
  return (
    <>
      <Script
        strategy="afterInteractive"
        src={`https://www.googletagmanager.com/gtag/js?id=G-MTR76P4RPF`}
      />
      <Script
        id="google-analytics"
        strategy="afterInteractive"
        dangerouslySetInnerHTML={{
          __html: `
            window.dataLayer = window.dataLayer || [];
            function gtag(){dataLayer.push(arguments);}
            gtag('js', new Date());
            gtag('config', 'G-MTR76P4RPF', {
              page_path: window.location.pathname,
            });
          `,
        }}
      />
    </>
  );
}


## Metadata
- Source file: junk_drawer/github/PersonalWebsite/src/components/GoogleAnalytics.tsx.txt
- Extracted: 2026-05-18
- Category: github-code
