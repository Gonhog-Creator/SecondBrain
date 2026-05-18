# movie.ts

Source: junk_drawer/github/PersonalWebsite/src/types/movie.ts.txt

Category: [[github-code]]

## Summary
export interface Movie { id: string; title: string; releaseDate?: string; genre?: string; genres?: string[]; imdbId?: string; imdbScore?: number; rottenTomatoesScore?: number; myRating: number;

## Full Content
export interface Movie {
  id: string;
  title: string;
  releaseDate?: string;
  genre?: string;
  genres?: string[];
  imdbId?: string;
  imdbScore?: number;
  rottenTomatoesScore?: number;
  myRating: number;
  posterUrl: string;
  plot?: string;
  year?: string;
  rated?: string;
  director?: string;
  actors?: string[];
  language?: string;
  country?: string;
  metascore?: string;
  awards?: string;
  production?: string;
  runtime?: number;
  style?: string;
  mediaType?: string;
  watchedDate?: string;
  differences?: {
    imdb: number;
    rotten: number;
  };
  protagonistRating?: number;
  antagonistRating?: number;
  soundtrackRating?: number;
  setDesignRating?: number;
  plotRating?: number;
  endingRating?: number;
}


## Metadata
- Source file: junk_drawer/github/PersonalWebsite/src/types/movie.ts.txt
- Extracted: 2026-05-18
- Category: github-code
