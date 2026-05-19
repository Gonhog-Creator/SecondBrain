#!/usr/bin/env python3
"""
Daily Research Paper Suggestion System

This script analyzes your wiki to identify knowledge gaps and suggests
research papers to fill them. Can be run daily via cron or manually.
"""

import os
import json
import random
from pathlib import Path
from datetime import datetime, timedelta
from collections import Counter

WIKI_DIR = Path("/Users/josemariabarbeito/PycharmProjects/SecondBrain/wiki")
RAW_SOURCES = Path("/Users/josemariabarbeito/PycharmProjects/SecondBrain/raw-sources")
DAILY_DIR = Path("/Users/josemariabarbeito/PycharmProjects/SecondBrain/Daily")
RESEARCH_LOG = DAILY_DIR / "research-suggestions.md"

# Knowledge areas based on your wiki content
KNOWLEDGE_DOMAINS = {
    "machine_learning": {
        "keywords": ["neural network", "deep learning", "ML", "AI", "training", "model", "tensorflow", "pytorch"],
        "sources": ["arXiv cs.LG", "arXiv cs.AI", "PMLR", "NeurIPS", "ICML"],
        "suggested_papers": [
            "Attention Is All You Need (Transformer architecture)",
            "Deep Residual Learning for Image Recognition (ResNet)",
            "BERT: Pre-training of Deep Bidirectional Transformers"
        ]
    },
    "process_engineering": {
        "keywords": ["chemical engineering", "reactor", "distillation", "process control", "transport phenomena"],
        "sources": ["AIChE Journal", "Chemical Engineering Science", "IEC&R"],
        "suggested_papers": [
            "Advances in Process Systems Engineering",
            "Machine Learning Applications in Chemical Engineering",
            "Digital Twins for Process Industries"
        ]
    },
    "materials_science": {
        "keywords": ["polymer", "material properties", "composite", "kevlar", "viscoelastic"],
        "sources": ["Nature Materials", "Advanced Materials", "Materials Today"],
        "suggested_papers": [
            "High-Performance Polymer Composites: Recent Advances",
            "Self-Healing Materials: A Review",
            "Machine Learning for Materials Discovery"
        ]
    },
    "ballistics_protection": {
        "keywords": ["ballistic", "armor", "NIJ", "body armor", "protection", "trauma"],
        "sources": ["International Journal of Impact Engineering", "Ballistics", "Personal Armour Systems Symposium"],
        "suggested_papers": [
            "Next-Generation Body Armor Materials",
            "Blast Protection: Current State and Future Directions",
            "Behind Armor Blunt Trauma: Mechanisms and Mitigation"
        ]
    },
    "software_engineering": {
        "keywords": ["software", "code", "github", "development", "architecture", "API"],
        "sources": ["IEEE Software", "ACM TOSEM", "arXiv cs.SE"],
        "suggested_papers": [
            "Clean Architecture: A Craftsman's Guide",
            "Microservices Patterns: With examples in Java",
            "The Pragmatic Programmer: 20th Anniversary Edition"
        ]
    },
    "data_science": {
        "keywords": ["data", "analytics", "visualization", "statistics", "regression"],
        "sources": ["Journal of Data Science", "Data Mining and Knowledge Discovery", "KDD"],
        "suggested_papers": [
            "Exploratory Data Analysis: A Systematic Approach",
            "Interpretable Machine Learning",
            "The Art of Data Science"
        ]
    },
    "history_politics": {
        "keywords": ["history", "politics", "war", "immigration", "policy"],
        "sources": ["American Historical Review", "Foreign Affairs", "Journal of American History"],
        "suggested_papers": [
            "The Long Civil Rights Movement",
            "Immigration Policy in Historical Perspective",
            "Cold War Historiography: New Approaches"
        ]
    }
}

def analyze_wiki_coverage():
    """Analyze wiki to see which knowledge domains are well-covered vs gaps."""
    if not WIKI_DIR.exists():
        return {}
    
    coverage = {domain: 0 for domain in KNOWLEDGE_DOMAINS}
    
    # Count files mentioning each domain's keywords
    for md_file in WIKI_DIR.glob("*.md"):
        try:
            content = md_file.read_text().lower()
            for domain, config in KNOWLEDGE_DOMAINS.items():
                for keyword in config["keywords"]:
                    if keyword.lower() in content:
                        coverage[domain] += 1
                        break
        except:
            continue
    
    return coverage

def get_recent_papers_count():
    """Count papers read in the last 30 days from research log."""
    if not RESEARCH_LOG.exists():
        return {}
    
    content = RESEARCH_LOG.read_text()
    # Simple count of entries in the last month
    lines = content.split('\n')
    recent_domains = Counter()
    
    for line in lines:
        for domain in KNOWLEDGE_DOMAINS:
            if domain.replace('_', ' ').title() in line:
                recent_domains[domain] += 1
    
    return recent_domains

def identify_gaps(coverage, recent):
    """Identify knowledge gaps - domains with low coverage or no recent papers."""
    scores = {}
    
    for domain in KNOWLEDGE_DOMAINS:
        # Score = inverse of coverage + inverse of recent activity
        coverage_score = max(1, 10 - coverage.get(domain, 0))  # 1-10
        recent_score = max(1, 5 - recent.get(domain, 0))     # 1-5
        total_score = coverage_score + recent_score
        scores[domain] = total_score
    
    return scores

def suggest_paper(gap_scores):
    """Suggest a paper based on identified gaps."""
    # Weight random choice by gap score
    domains = list(gap_scores.keys())
    weights = [gap_scores[d] for d in domains]
    
    # Pick domain with highest gap score (with some randomness)
    selected_domain = random.choices(domains, weights=weights, k=1)[0]
    
    config = KNOWLEDGE_DOMAINS[selected_domain]
    paper = random.choice(config["suggested_papers"])
    
    return {
        "domain": selected_domain,
        "domain_display": selected_domain.replace('_', ' ').title(),
        "paper": paper,
        "sources": config["sources"],
        "keywords": config["keywords"][:5]  # Top 5 keywords
    }

def log_suggestion(suggestion):
    """Log the suggestion to research log."""
    DAILY_DIR.mkdir(exist_ok=True)
    
    today = datetime.now().strftime("%Y-%m-%d")
    
    entry = f"""
## [{today}] {suggestion['domain_display']}

**Suggested Paper:** {suggestion['paper']}

**Domain:** {suggestion['domain_display']}
**Relevant Keywords:** {', '.join(suggestion['keywords'])}
**Suggested Sources:** {', '.join(suggestion['sources'])}

**Action:**
- [ ] Find and read paper
- [ ] Take notes
- [ ] Integrate into wiki

---
"""
    
    if RESEARCH_LOG.exists():
        content = RESEARCH_LOG.read_text()
    else:
        content = "# Research Paper Suggestions Log\n\nDaily suggestions for expanding knowledge based on wiki gaps.\n"
    
    content = content + entry
    RESEARCH_LOG.write_text(content)

def generate_daily_briefing():
    """Generate a daily briefing with paper suggestion."""
    print("=" * 70)
    print("DAILY RESEARCH PAPER SUGGESTION")
    print("=" * 70)
    print()
    
    # Analyze wiki
    coverage = analyze_wiki_coverage()
    recent = get_recent_papers_count()
    gaps = identify_gaps(coverage, recent)
    
    # Show current coverage
    print("Current Wiki Coverage by Domain:")
    print("-" * 50)
    for domain, count in sorted(coverage.items(), key=lambda x: x[1]):
        recent_count = recent.get(domain, 0)
        bar = "█" * min(count, 20) + "░" * (20 - min(count, 20))
        print(f"{domain.replace('_', ' '):25} |{bar}| {count:3} files, {recent_count} recent papers")
    print()
    
    # Suggest paper
    suggestion = suggest_paper(gaps)
    
    print("=" * 70)
    print(f"TODAY'S SUGGESTION: {suggestion['domain_display'].upper()}")
    print("=" * 70)
    print()
    print(f"📄 Paper: {suggestion['paper']}")
    print()
    print(f"🔍 Why this domain? Low coverage in your wiki (gap score: {gaps[suggestion['domain']]})")
    print()
    print(f"📚 Suggested Sources:")
    for source in suggestion['sources']:
        print(f"   - {source}")
    print()
    print(f"🏷️  Related Keywords in Your Wiki:")
    print(f"   {', '.join(suggestion['keywords'])}")
    print()
    print("=" * 70)
    print("NEXT STEPS:")
    print("=" * 70)
    print("1. Search for the paper on arXiv, Google Scholar, or suggested sources")
    print("2. Download PDF to raw-sources/papers/")
    print("3. Read and take notes")
    print("4. Tell Cascade: 'Process the paper I just downloaded'")
    print()
    print("Alternative: Ask Cascade to find a current paper on this topic")
    print("=" * 70)
    
    # Log it
    log_suggestion(suggestion)
    print(f"\n✅ Logged to: {RESEARCH_LOG}")

def main():
    generate_daily_briefing()
    
    # Also print commands for Cascade
    print()
    print("COMMANDS YOU CAN USE:")
    print("-" * 50)
    print('"Search for a recent paper on [topic] and suggest one to read"')
    print('"Find papers on machine learning for chemical engineering"')
    print('"What are the latest developments in [domain]?"')

if __name__ == "__main__":
    main()
