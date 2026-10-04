# CC BY or CC BY-SA: a reading guide

Open. Proposed decision [0014](https://github.com/cobarx/build-skills-cobarx/pull/54) chooses
CC BY 4.0 and dismisses CC BY-SA 4.0 in one line. This guide is for reading up before that choice
is settled. Claims carry a confidence level and what it rests on. Legal text was checked against
the legal codes at `creativecommons.org/licenses/{by,by-sa}/4.0/legalcode.txt` on 2026-09-28.

## One clause differs

The two licences are the same text apart from ShareAlike. BY-SA adds §3(b):

> In addition to the conditions in Section 3(a), if You Share Adapted Material You produce, the
> following conditions also apply.
>
> 1. The Adapter's License You apply must be a Creative Commons license with the same License
>    Elements, this version or later, or a BY-SA Compatible License.
> 2. You must include the text of, or the URI or hyperlink to, the Adapter's License You apply. [...]
> 3. You may not offer or impose any additional or different terms or conditions on, or apply any
>    Effective Technological Measures to, Adapted Material that restrict exercise of the rights
>    granted under the Adapter's License You apply.

BY has only §3(a)(4) in its place: "the Adapter's License You apply must not prevent recipients of
the Adapted Material from complying with this Public License."

The Adapter's License covers only the adapter's own contributions (§1(b)). So the whole difference
is **what terms an adapter may put on what they add**: anything that doesn't block compliance
(BY), or BY-SA and its approved equivalents (BY-SA). High, from the text.

What ShareAlike does not do (high): it does not require anyone to share, so private copies stay
invisible; it does not apply to use, only to sharing adapted material; it does not change the
attribution conditions, which are identical.

## What both require, so it decides nothing

- **Attribution, §3(a)(1):** creator, copyright notice, licence notice, disclaimer notice, a link
  to the material, and "indicate if You modified the Licensed Material and retain an indication
  of any previous modifications."
- **Cure, §6(b):** rights reinstate if a violation is cured "within 30 days of Your discovery of
  the violation."
- **Irrevocable** for copies already shared; commercial use allowed; attribution binds only where
  copyright exists (the AI-authorship caveat in 0014).

## Two corrections to the 2026-09-25 analysis

1. **The modification history survives under both.** The working notes (MetanoiaFramework,
   `docs/context/skill-trust-network-notes.md`, thread 6) said CC BY keeps the root of the ancestry
   and loses the middle links. §3(a)(1)(b) makes everyone who shares "retain an indication of any
   previous modifications", so the chain of change notes carries through under either licence.
   What CC BY does not keep is the *terms* on an intermediate adapter's additions: they may license
   them with no attribution condition, or close them. Under BY-SA those additions stay BY-SA, so
   the intermediate author's credit and change marking travel too. High on the text; this narrows
   the ancestry argument for BY-SA.
2. **The cure runs from discovery, not notice.** Earlier I said 30 days "after notice." In practice
   a notice is usually the discovery, so the effect is the same, but the text says discovery.

## The considerations, ranked

**These decide it:**

1. **What must survive down the chain.** Root credit and modification history survive under both.
   Only BY-SA keeps every intermediate adapter's contributions open and credited. Question: is the
   ancestry timeline complete if the middle authors' additions can go closed? Moderate: depends on
   how many adapters would choose to close theirs.
2. **Adoption against the norm.** BY-SA is copyleft for prose. Two costs (moderate): corporate
   legal reviews treat ShareAlike more cautiously, and BY-SA material mixed into a BY or MIT
   project can only be shared onward under BY-SA, where BY mixes into anything. Against that, you
   called BY-SA "bold" and "transformative": the licence states the norm rather than inviting it.
3. **The asymmetry.** As sole author you can later add CC BY alongside BY-SA (loosen), and it
   reaches every release, since everyone can take the freer terms. You can also move from BY to
   BY-SA (tighten), but only future releases: copies already released under BY stay BY, and a
   fork of the last BY release can close its changes. High. Outside contributions block only
   loosening: a BY-SA contribution needs its contributor's consent to become BY, while BY
   material may go into a BY-SA work without asking.

**Secondary:**

4. **Code.** BY-SA 4.0 is one-way compatible with GPLv3 (Creative Commons determination, 2015):
   adapted BY-SA material may be shared under GPLv3. 0014 puts code under a separate software
   licence anyway, so this matters only if prose and code mix in one file. Moderate.
5. **Precedent.** trailofbits/skills uses BY-SA 4.0 for the whole repository, Python tooling
   included. Wikipedia (BY-SA) holds its citation culture; Stack Overflow (BY-SA) did not. Most
   open-access journals use BY (Plan S requires it). The licence did not make the difference;
   culture did (working notes, thread 8).

## What other skills repos did, and what happened to copies

Searched 2026-10-03. No general analysis of licences for skills exists;
[agentskills#379](https://github.com/agentskills/agentskills/discussions/379) proposes CC BY for prose and a software licence for scripts, unresolved. Projects that wrote down
a reason:

- [skillboss-dojo#13](https://github.com/mazzyst/skillboss-dojo/pull/13) moved its skills from
  BY-SA to Apache-2.0, keeping BY-SA for docs: "can I use this at work?" must be yes "with no clause
  to reason about." Private use does not trigger ShareAlike, so this is consideration 2's
  perception cost, paid.
- [green-claude#51](https://github.com/Institut-du-Numerique-Responsable/green-claude/pull/51):
  CC BY 4.0 for rules and `SKILL.md`, Apache-2.0 for code. The split 0014 proposes.
- [alekslinde/skills#6](https://github.com/alekslinde/skills/pull/6): Apache-2.0 for everything,
  because `npx skills` copies skill folders into commercial repos.

Copies are common and whole-file. trailofbits' `audit-context-building` appears in about 30 other
repos, mostly aggregators. Of eight sampled, none credits Trail of Bits in the skill file (nor
does the original), and two now declare `license: MIT` after an aggregator relabelled it. BY-SA
did not travel with the copies; credit, where it survived, was in repo READMEs and one mirror's
generated `ORIGIN.md`. High on what was found, low on how typical it is: one skill, one search.

This weakens consideration 1 as an argument for either licence: credit down the chain is carried
by tooling and culture more than by terms. Provenance is now its own question, [#63](https://github.com/cobarx/build-skills-cobarx/issues/63).

## Questions to answer

- Is root credit plus modification history enough, or must intermediate contributions stay open?
- Is the goal to state the norm now (BY-SA) or to maximise adoption and let culture carry credit
  (BY)?
- Does the asymmetry argue for starting with BY-SA and loosening later if it proves heavy?

## Reading list, in order

1. [CC BY-SA 4.0 legal code](https://creativecommons.org/licenses/by-sa/4.0/legalcode.en): §1(b)
   and (c), then §3(b). The only new text.
2. [CC BY 4.0 legal code](https://creativecommons.org/licenses/by/4.0/legalcode.en): §3(a) in full,
   and §6(b).
3. The deeds, side by side: [BY-SA](https://creativecommons.org/licenses/by-sa/4.0/) and
   [BY](https://creativecommons.org/licenses/by/4.0/).
4. [Compatible licenses](https://creativecommons.org/compatible-licenses/): what counts as a BY-SA
   Compatible License.
5. [ShareAlike compatibility: GPLv3](https://wiki.creativecommons.org/wiki/ShareAlike_compatibility:_GPLv3):
   how one-way compatibility works.
6. [Considerations for licensors and licensees](https://wiki.creativecommons.org/wiki/Considerations_for_licensors_and_licensees).
7. [Reusing Wikipedia content](https://en.wikipedia.org/wiki/Wikipedia:Reusing_Wikipedia_content):
   BY-SA as practised by the largest commons that uses it.
8. [trailofbits/skills](https://github.com/trailofbits/skills): the one skills library on BY-SA.
