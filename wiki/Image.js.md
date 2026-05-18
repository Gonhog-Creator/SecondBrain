# Image.js

Source: junk_drawer/github/PersonalWebsite/src/components/Image.js.txt

Category: [[github-code]]

## Summary
import NextImage from 'next/image'; export default function Image({ src, alt, width, height, ...props }) { const isGHPages = process.env.NEXT_PUBLIC_GH_PAGES === 'true'; const basePath = isGHPages ? '/PersonalWebsite' : ''; // Handle different image paths let imageSrc = src; // If the image is in the public folder

## Full Content
import NextImage from 'next/image';

export default function Image({ src, alt, width, height, ...props }) {
  const isGHPages = process.env.NEXT_PUBLIC_GH_PAGES === 'true';
  const basePath = isGHPages ? '/PersonalWebsite' : '';
  
  // Handle different image paths
  let imageSrc = src;
  
  // If the image is in the public folder
  if (src.startsWith('/')) {
    imageSrc = `${basePath}${src}`;
  }

  return (
    <NextImage
      src={imageSrc}
      alt={alt || ''}
      width={width}
      height={height}
      unoptimized={true}
      {...props}
    />
  );
}


## Metadata
- Source file: junk_drawer/github/PersonalWebsite/src/components/Image.js.txt
- Extracted: 2026-05-18
- Category: github-code
