# WP3 Q1 — PECO and PubMed search v2 (22 Oct 2026)
Built on P'Roong's "LTC_search strategy.xlsx" and the 15 Oct workshop. Draft for the 22 Oct meeting.

> **Note (31 Oct):** this is the earlier 22 Oct draft. Its E block still lists named tools (interRAI, MDS-HC, RUG-III, Kihon Checklist, AN-ACC, Pflegegrad, etc.). The accepted version (2,943 hits) has no named tools in E. The exact lines are D1 in "Q1 search v3.2 + ChatGPT prompt (22 Oct).txt".

## Q1 (locked)
What eligibility criteria and assessment tools do long-term care systems use to decide who enters LTC and at what care level, including people moving from intermediate or post-acute care, and what evidence supports them?

## PECO — Q1 broken into parts
| Part of Q1 | PECO | Plain meaning | In the search? |
|---|---|---|---|
| "LTC systems ... including people moving from intermediate or post-acute care" | **P** Population | People of any age being assessed for LTC, including people leaving IMC / post-acute care | Yes: Concept 1 = P1 (LTC) OR P2 (IMC/post-acute) |
| "eligibility criteria and assessment tools" | **E** Exposure | The rules and tools used to decide: criteria, assessment instruments, scoring/grading systems, decision algorithms | Yes: Concept 2 |
| (none) | **C** Comparison | Not required. Note any comparison tool or expert judgement if a study has one | No |
| "who enters LTC and at what care level" | **O** main | The decision itself: what is assessed (domains), the cut-off or rule, and the result (eligible or not, care level) | Yes: Concept 3 |
| "what evidence supports them" | **O** supporting | How trustworthy the tool is (reliability = different assessors get the same result; validity = it measures real need) and what happens later (LTC entry, decline, death) | No. Found by reading (agreed 15 Oct) |

Combine: (P1 OR P2) AND E AND O

## What changed from the 14 Oct run (1,817 hits; 1,670 for 2005–2026)
Removed, because they add noise:
- "Intermediate Care Facilities"[Mesh]: in MeSH this means US homes for people with intellectual disability, not Thai IMC
- "Aftercare"[Mesh] (261,406 alone): too broad. Replaced with "Subacute Care"[Mesh] and "Transitional Care"[Mesh]
- rehabilitation[tiab] (in the sheet's P2): far too broad. Kept "geriatric rehabilitation" only
- assess*, criteri*: dropped at the workshop
- algorithm*, "risk score*" (sheet E): these pull in prediction studies
- "Patient Selection"[Mesh] (73,013): mostly trial and surgery selection

Added, to fill gaps:
- P1: LTC insurance (central to Japan, Korea, Germany), nursing/care homes, home care, aged care, social care
- E: named tools (interRAI, MDS-HC, MAPLe, RUG-III, Kihon Checklist, Aged Care Assessment, AN-ACC, Pflegegrad), "Disability Evaluation"[Mesh], case-mix
- O: "Eligibility Determination"[Mesh], entitle*, certif* (Japan care-need certification), gatekeep*, needs-based
- Duplicates merged ("needs assessment*" covers needs assessment/assessments; "long-term care"[tiab] covers "long-term care system*" and "facilit*")

## PubMed lines (run each, note the count)
**P1 — LTC**
("Long-Term Care"[Mesh] OR "Insurance, Long-Term Care"[Mesh] OR "Nursing Homes"[Mesh] OR "Homes for the Aged"[Mesh] OR "Home Care Services"[Mesh] OR "Assisted Living Facilities"[Mesh] OR "long-term care"[tiab] OR "long term care"[tiab] OR "long-term services and supports"[tiab] OR "long term services and supports"[tiab] OR LTSS[tiab] OR LTCI[tiab] OR "residential care"[tiab] OR "institutional care"[tiab] OR "nursing home*"[tiab] OR "care home*"[tiab] OR "aged care"[tiab] OR "home care"[tiab] OR "home-based care"[tiab] OR "home and community-based services"[tiab] OR "home and community based services"[tiab] OR "social care"[tiab] OR "continuing care"[tiab])

**P2 — IMC / post-acute / transitional**
("Subacute Care"[Mesh] OR "Transitional Care"[Mesh] OR "Patient Discharge"[Mesh] OR "intermediate care"[tiab] OR "post-acute"[tiab] OR postacute[tiab] OR "subacute care"[tiab] OR "sub-acute care"[tiab] OR "transitional care"[tiab] OR "care transition*"[tiab] OR "transition of care"[tiab] OR "transitions of care"[tiab] OR "step-down care"[tiab] OR "step down care"[tiab] OR reablement[tiab] OR "geriatric rehabilitation"[tiab] OR "hospital discharge"[tiab] OR "discharge planning"[tiab])

**E — criteria and tools**
("Needs Assessment"[Mesh] OR "Disability Evaluation"[Mesh] OR "needs assessment*"[tiab] OR "need assessment*"[tiab] OR "assessment tool*"[tiab] OR "assessment instrument*"[tiab] OR "assessment scale*"[tiab] OR "assessment system*"[tiab] OR "assessment framework*"[tiab] OR "screening tool*"[tiab] OR "screening instrument*"[tiab] OR "decision rule*"[tiab] OR "decision tool*"[tiab] OR "decision support"[tiab] OR "grading system*"[tiab] OR "classification system*"[tiab] OR "classification tool*"[tiab] OR "scoring system*"[tiab] OR "eligibility criteria"[tiab] OR "case-mix"[tiab] OR casemix[tiab] OR interRAI[tiab] OR "MDS-HC"[tiab] OR "RAI-HC"[tiab] OR "Method for Assigning Priority Levels"[tiab] OR "Resource Utilization Group*"[tiab] OR "RUG-III"[tiab] OR "Kihon Checklist"[tiab] OR "Aged Care Assessment"[tiab] OR "AN-ACC"[tiab] OR Pflegegrad*[tiab])

**O — the eligibility / care-level decision**
("Eligibility Determination"[Mesh] OR eligib*[tiab] OR ineligib*[tiab] OR entitle*[tiab] OR certif*[tiab] OR gatekeep*[tiab] OR "care need*"[tiab] OR "service need*"[tiab] OR "care requirement*"[tiab] OR "level of care"[tiab] OR "levels of care"[tiab] OR "care level*"[tiab] OR "care intensity"[tiab] OR "care allocation"[tiab] OR "service allocation"[tiab] OR "resource allocation"[tiab] OR "care placement"[tiab] OR "placement decision*"[tiab] OR "care decision*"[tiab] OR "admission criteri*"[tiab] OR "access criteri*"[tiab] OR "needs-based"[tiab] OR "need-based"[tiab])

**Final** (with History numbers P1=#1, P2=#2, E=#3, O=#4):
(#1 OR #2) AND #3 AND #4 NOT ("Animals"[Mesh] NOT "Humans"[Mesh])

## Seed check
Paste after the final line (use its History number in place of #5):
#5 AND (15743300[pmid] OR 12145374[pmid] OR 15498843[pmid] OR 23869339[pmid] OR 18366782[pmid] OR 38037101[pmid] OR 18191276[pmid] OR 20510982[pmid] OR 18781503[pmid] OR 38667450[pmid])
Which were missed: (15743300[pmid] OR 12145374[pmid] OR 15498843[pmid] OR 23869339[pmid] OR 18366782[pmid] OR 38037101[pmid] OR 18191276[pmid] OR 20510982[pmid] OR 18781503[pmid] OR 38667450[pmid]) NOT #5
Note: 38667450 is context only (not expected). 20510982 and 18781503 (CANS, PCANS) are rehab/child cases and may be missed by design.

## If the final count is too high (P'Roong's target: about 2,000–3,000 in PubMed)
Cut in this order, re-running the seed check each time:
1. Remove "home care" and "social care" from P1
2. Remove "Patient Discharge"[Mesh] from P2
3. Remove certif* from O (re-check that Tsutsui 15743300 still comes back)
4. Remove "eligibility criteria" from E (it often means trial eligibility)

## Decisions for the meeting
- Date limit: none, 1990+, or 2005+ (P'Roong tested 2005–2026)
- Content experts (Aj Harisd, อ.ยี้) review the term list. P'Roong's advice is that this is expected for publication
- PROSPERO: register once PECO and search terms are stable, before data extraction (P'Roong, 15 Oct). Preliminary searching is allowed before registration
- Then translate to Embase, CINAHL and Scopus with AI, checking each subject-heading term by hand (Emtree is not the same as MeSH)
- Second reviewer
