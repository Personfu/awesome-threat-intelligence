# FLLC Bug Hunter Upgrade — awesome-threat-intelligence

## Portfolio role

This repo should become the **FLLC threat intelligence source map**: not just a list of links, but a scored, tagged, source-aware catalog for bug hunters, SOC analysts, and research workflows.

## Upgrade direction

### 1. Add source scoring

Move the link list toward structured metadata:

```json
{
  "name": "Example Feed",
  "category": "ioc-feed | malware | dns | bgp | cert-transparency | reputation | research",
  "access": "free | freemium | paid | academic",
  "format": ["csv", "json", "stix", "taxii", "rss"],
  "freshness": "realtime | daily | weekly | unknown",
  "best_for": ["triage", "hunting", "enrichment", "blocking", "research"],
  "cautions": ["false positives", "license restrictions", "requires validation"]
}
```

### 2. Bug-hunter workflows

Add curated workflows:

- subdomain and CT review;
- leaked credential notification workflow;
- domain reputation enrichment;
- phishing kit triage;
- ASN/IP risk review;
- CVE-to-exposure mapping;
- source confidence scoring.

### 3. Mission-control visual layer

Feed FLLC `/mission-systems` with:

- source cards;
- freshness badges;
- confidence scores;
- category filters;
- graph links between source type and use case.

### 4. Public/premium split

| Tier | Content |
| --- | --- |
| Public | Curated source map and how to validate intel |
| Basic | Source workflows and enrichment checklists |
| Premium | Custom intel brief templates and customer-owned scope reviews |

## Content outputs

- Blog: “Threat intelligence is not a link dump.”
- Short video: “IOC feeds need confidence, context, and expiration.”
- Member lesson: “Build a source-scored bug bounty enrichment pipeline.”

## Professional rules

- Validate before blocking.
- Track source freshness.
- Respect feed licenses.
- Do not publish private indicators from clients.
- Mark confidence and caveats on every output.
