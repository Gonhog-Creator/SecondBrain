# tsconfig.json

Source: junk_drawer/github/PersonalWebsite/tsconfig.json.txt

Category: [[github-code]]

## Summary
{ "compilerOptions": { "target": "ES2017", "lib": [ "dom", "dom.iterable", "esnext" ], "allowJs": true, "skipLibCheck": true,

## Full Content
{
  "compilerOptions": {
    "target": "ES2017",
    "lib": [
      "dom",
      "dom.iterable",
      "esnext"
    ],
    "allowJs": true,
    "skipLibCheck": true,
    "strict": true,
    "noEmit": true,
    "esModuleInterop": true,
    "module": "esnext",
    "moduleResolution": "bundler",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "jsx": "react-jsx",
    "incremental": true,
    "plugins": [
      {
        "name": "next"
      }
    ],
    "paths": {
      "@/*": [
        "./src/*"
      ]
    }
  },
  "include": [
    "**/*.ts",
    "**/*.tsx",
    ".next/types/**/*.ts",
    "next-env.d.ts",
    "out/types/**/*.ts",
    ".next/dev/types/**/*.ts"
  ],
  "exclude": [
    "node_modules"
  ]
}


## Metadata
- Source file: junk_drawer/github/PersonalWebsite/tsconfig.json.txt
- Extracted: 2026-05-18
- Category: github-code
