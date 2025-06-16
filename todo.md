**Estimated Total Required Time: ~11-13 hours of active work remaining**

---

General note:

-   We skip all backgrounds todos at first and just read the corresponding LLM section and maybe add comments to them. (use \comment{})

**Phase 1: Foundation & Structure (Joint)**

- [x] **Review and Edit This To-Do List (15 min):** Discuss and agree on this work plan and task delegation.
-   [x] **Clean & Prune `literature.bib` (1 hour per person = 2 hours total):**
    -   [x] **Action:** Verify if `hanInstructMEInstructionGuided2023` and `talJointAudioSymbolic2024` (currently preprints) have **peer-reviewed versions**. If so, update their bib entries. If not, note them as arXiv, but prioritize finding peer-reviewed alternatives for your minimum of 8.
    -   [x] **Action:** Ensure you have at least 8 _relevant, peer-reviewed_ references for the paper. Add more if necessary to meet this count with high-quality, relevant sources.
-   [x] LLM generate Backgrounds for later revision
-   [ ] **Collaborative Outline of Background Subsections (30 min):** Based on the Rouard et al. paper and your presentation's structure (e.g., "Related Work," "Textual Inversion," "Style Conditioner"), collaboratively decide on the granular subsections within the "Backgrounds" section of your paper. This will guide writing and ensure logical flow.
-   [ ] ask llm to adapt backgrounds to new structure
-   [x] **Define & Document Consistent Formatting (15 min):** Agree on and document (e.g., in a comment at the top of the `.tex` file) formatting conventions for:
    -   Important terms (e.g., **bold**).
    -   Dataset names (e.g., _AudioSet_).
    -   Model names (e.g., MusicGen, Encodec).
    -   Code/technical components (`\texttt{pseudowords}`).
    -   Citation style (ensure `plainnat` is used for all).

---

**Phase 2: Drafting Core Sections (Individual & Parallel)**

**Max's Tasks (Estimated Total Time: ~5.5-6.5 hours)**

-   [ ] **Fast Re-Reading of Rouard et al. Paper (2 hours):** (Individual review) Perform a focused re-read to catch anything missed and ensure a deep understanding before synthesizing.
-   [ ] **Insert all figures** from this folder, decide which ones to include from the original paper, musicgens paper, our demos etc.
-   [ ] **add additional subsections to the outline based on the the figures**
-   [ ] **Draft Introduction - Purpose & Scope (1 hour):** Expand on the seminar work's purpose (critical review of Rouard et al.). Introduce the paper's core contributions (textual inversion, pseudowords, fast inference, double classifier free guidance) and provide a clear roadmap for _your_ paper, referencing the upcoming sections. (Leverage intro slides from presentation).
-   [ ] **Draft Backgrounds - Core AI/ML Concepts (3-4 hours):**
    -   Write concise explanations for the terms assigned in the explanation priorisation spreadsheet
    -   Integrate Figure \ref{Figure 1} discussion into the relevant section, explaining its purpose and content.
    -   **Action:** Investigate and resolve the inclusion of Equation \ref{eq:hypervolume}. If it's not directly from the Rouard et al. paper and central to their method, **remove it**. If it is, ensure its context is fully explained.
-   [ ] **Draft Discussion - Technical & Methodological Aspects (1.5-2 hours):**
    -   **Convert Outline to Prose:** Transform the existing outline points into detailed prose, citing evidence from the paper.
    -   Discuss: "Why audio and style encoding instead of just style encoding?" (based on authors' intent and your analysis).
    -   Discuss: "Why style conditioning of 1.5-4.5s instead of longer?" (authors' reasons vs. implications).
    -   Discuss: "Why 5hz downsampling after codebook instead of before?" (authors' reasons vs. implications).
    -   Elaborate on "Music generation speed" and its practical implications (referencing presentation notes).
    -   Elaborate on "Train compute, dataset size + quality + model scaling" (referencing presentation notes about 1.4bn params vs. SOTA). **Action:** If you're citing a general "proof of concept" for scaling, ensure you have a specific, peer-reviewed citation.

**Felix's Tasks (Estimated Total Time: ~5.5-6.5 hours)**

-   [ ] **Fast Re-Reading of Rouard et al. Paper (2 hours):** (Individual review) Perform a focused re-read to catch anything missed and ensure a deep understanding before synthesizing.
-   [ ] comment environment setup felix,
-   [ ] llm generate and mark backgrounds for later revision
-   [ ] **Draft Introduction - Context & Outline (1 hour):** Write the paragraphs that provide context for the research (e.g., current state of music generation, problem statement) and clearly outline the structure of _this seminar work_, mentioning what each subsequent section will cover. (Leverage intro slides from presentation).
-   [ ] **Draft Backgrounds - Music-Specific AI Models (2 hours):**
    -   Write concise explanations for the terms assigned in the explanation priorisation spreadsheet
-   [ ] **Develop Experiments Section (4-5 hours):**
    -   Describe Rouard et al.'s experimental setup (datasets, training procedures, evaluation protocols).
    -   Present and interpret the _actual results_ from the Rouard et al. paper. This involves carefully extracting data from their tables and figures, and explaining them. **Action:** Replace or verify Table \ref{tab1} with real data from the paper and discuss it thoroughly. (Leverage "Experimental Results" slide from presentation).
    -   Explain KNN$_{overfit}$, KNN$_{common}$) and human metrics (OVL, SIM, VAR), clarifying their definitions and significance.
-   [ ] **Draft Discussion - Broader Implications & User-Centric Aspects (1.5-2 hours):**
    -   **Convert Outline to Prose:** Transform the existing outline points into detailed prose, citing evidence.
    -   Elaborate on "Out-of-Training Distribution Generalization" (Music of Africa test, Pfeifen) and what these examples reveal. (Leverage presentation notes).
    -   Discuss "Safety": Address the importance of safety/ethics in AI music generation. Analyze the linked "Model Card" for what it _does_ and _does not_ cover.
    -   Elaborate on specific "Testing" examples (e.g., 30s highlife input, folk and silence). (Leverage presentation notes).
    -   Analyze "User reactions" from `fiddle_1u2.txt` and draw conclusions about user perception.

---

**Phase 3: Refinement & Finalization (Joint & Individual)**

-   [ ] **Review slides and write down all requirements missing in this todo list**
-   [ ] **Draft Summary Section (1 hour):** (Joint or Max's primary, with Felix review) Write a concise summary covering the paper's problem, methods, key findings, and your main conclusions/critical insights.
-   [ ] **Ongoing Self-Review - Clarity & Coherence (Ongoing - ~2 hours total for paper):** (Individual for own sections, then exchange) As you write, periodically re-read your sections to ensure clarity, logical flow, and that all explanations are easy to understand for a CS student in their second semester.
-   [ ] **Ongoing Bibliography Management & Citation Check (Ongoing - ~1 hour total):** (Felix's primary, Max review)
    -   Continuously add new relevant references to `literature.bib` as you find them.
    -   Ensure _all in-text citations_ (`\cite{}`) are correctly linked and that you meet the requirement of at least 8 _peer-reviewed_ references (no Wikipedia, prefer published over arXiv).
    -   Verify that `plainnat` style is working correctly.
    -   **Action:** Ensure all exact citations (also to figures and tables) are marked and discussed in the text.
-   [ ] **Final Proofreading (1 hour):** (Both) A final pass for any typos, grammatical errors, and awkward phrasing.
-   [ ] **Final Formal Requirements Check (30 min):** (Both)
    -   Check overall length: 14-20 pages.
    -   Review consistent capitalization and formatting.
    -   Ensure participation of both team members is evident.
    -   Verify automatic proofreading has been used.
    -   Consider getting feedback from others if time allows.

---
