# submission.ts

Source: junk_drawer/github/PersonalWebsite/src/types/submission.ts.txt

Category: [[github-code]]

## Summary
export type SubmissionStatus = 'pending' | 'approved' | 'rejected'; interface BaseSubmissionData { name: string; description?: string; [key: string]: unknown; } interface IngredientData extends BaseSubmissionData { type: 'ingredient';

## Full Content
export type SubmissionStatus = 'pending' | 'approved' | 'rejected';

interface BaseSubmissionData {
  name: string;
  description?: string;
  [key: string]: unknown;
}

interface IngredientData extends BaseSubmissionData {
  type: 'ingredient';
  // Add more specific fields for ingredient submissions here
}

interface DishData extends BaseSubmissionData {
  type: 'dish';
  // Add more specific fields for dish submissions here
}

type OtherData = Record<string, unknown>;

export interface Submission {
  id: string;
  type: 'ingredient' | 'dish' | 'other';
  status: SubmissionStatus;
  data: IngredientData | DishData | OtherData;
  submittedBy: string;
  submittedAt: string;
  updatedAt?: string;
  notes?: string;
}

export interface SubmissionFilters {
  status?: SubmissionStatus;
  type?: string;
  search?: string;
  startDate?: string;
  endDate?: string;
}


## Metadata
- Source file: junk_drawer/github/PersonalWebsite/src/types/submission.ts.txt
- Extracted: 2026-05-18
- Category: github-code
