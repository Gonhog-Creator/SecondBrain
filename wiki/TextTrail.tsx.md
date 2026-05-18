# TextTrail.tsx

Source: junk_drawer/github/PersonalWebsite/src/components/ui/TextTrail.tsx.txt

Category: [[github-code]]

## Summary
import React, { ReactNode } from 'react'; import { motion } from 'framer-motion'; type TextTrailProps = { children: ReactNode; className?: string; }; const TextTrail: React.FC<TextTrailProps> = ({ children, className = '' }) => { return (

## Full Content
import React, { ReactNode } from 'react';
import { motion } from 'framer-motion';

type TextTrailProps = {
  children: ReactNode;
  className?: string;
};

const TextTrail: React.FC<TextTrailProps> = ({ children, className = '' }) => {
  return (
    <motion.div
      className={className}
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.5 }}
    >
      {children}
    </motion.div>
  );
};

export default TextTrail;


## Metadata
- Source file: junk_drawer/github/PersonalWebsite/src/components/ui/TextTrail.tsx.txt
- Extracted: 2026-05-18
- Category: github-code
