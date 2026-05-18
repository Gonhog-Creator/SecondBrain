# not-found.tsx

Source: junk_drawer/github/PersonalWebsite/src/app/not-found.tsx.txt

Category: [[github-code]]

## Summary
import Link from 'next/link'; export default function NotFound() { return ( <div className="flex flex-col items-center justify-center min-h-screen bg-background p-4 text-center"> <h1 className="text-4xl font-bold text-foreground mb-4">404 - Page Not Found</h1> <p className="text-muted-foreground mb-8"> The page you&apos;re looking for doesn&apos;t exist or has been moved. </p> <Link

## Full Content
import Link from 'next/link';

export default function NotFound() {
  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-background p-4 text-center">
      <h1 className="text-4xl font-bold text-foreground mb-4">404 - Page Not Found</h1>
      <p className="text-muted-foreground mb-8">
        The page you&apos;re looking for doesn&apos;t exist or has been moved.
      </p>
      <Link 
        href="/" 
        className="px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700 transition-colors"
      >
        Return Home
      </Link>
    </div>
  );
}


## Metadata
- Source file: junk_drawer/github/PersonalWebsite/src/app/not-found.tsx.txt
- Extracted: 2026-05-18
- Category: github-code
