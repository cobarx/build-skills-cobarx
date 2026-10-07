# The what dominates

**2026-10-06 · Claude Opus 5.5**

Hampton's claim is that in most pure software systems, the how is an implementation detail. Once
agents make an implementation inexpensive to replace, choosing it no longer gates the work, and the
what becomes the scarce, valuable part: what the output lets its user do. This essay covers why the
claim holds, what makes it hold, what replacement does not make cheap, where the how still gates,
and why replaceable does not mean disposable.

## An instinct calibrated on expensive rewrites

Engineers learned which choices matter when a rewrite cost months. A database, a cloud provider or
a framework was chosen once and then lived with. Hampton's observation is that the instinct outlived
its cause. DynamoDB against MySQL matters at very large data sets and costs. It does not matter by
default.

## You replace the gating choice, not the system

Moving from AWS to GCP means redoing the infrastructure layer and the clients for the vendor's SDK.
It does not mean redoing the application, provided the application was built that way. The industry
terms are ports and adapters (hexagonal architecture),[^cockburn] and, for persistence, the
repository pattern.[^fowler] A repository is what makes DynamoDB against MySQL a swap. It isolates
the engine only when its interface is shaped by what the domain asks, not by what the store can
query; methods built around one store's access patterns carry that store through the boundary. Data
already in the store still has to be migrated either way. The swap is as big as the leak. Once SDK
types have escaped into application code, the gating choice is everywhere.

Drawing the boundary also forces the question of which side owns a fact. Hampton learned early that
normalizing data avoids many problems, and one case he recalls is from Digital Path, a wireless
internet service provider. It placed repeater devices in homes and on towers, and a large hub might
hold a dozen or more. Each device's address was entered by hand, so one physical location could have
three or more records, and it was hard even to see which devices were at a given site. Passing each
address through the USPS address service gives it one canonical form, so one place has one record:
the service owns what an address is.

A boundary forces the same move. What it requires is one owner and one source of truth, not one
stored copy. A cache, a read model or a per-service copy is fine, so long as it derives from the
owner and is known to be a copy. A denormalized store is fine behind a repository. A denormalized
interface leaks it.

The same thing holds at platform scale. When Apple built the iPhone's operating system, it kept
the Mac's foundation layers (Core Foundation and Foundation) underneath and replaced the user
interface layer, AppKit, with UIKit, built for touch.[^ios] Hampton's counter-case is Windows,
whose one constant principle, as he reads it, is backward compatibility. With enough programs
depending on its internals, every observable behaviour is depended on by somebody (Hyrum's
law).[^hyrum] There is no boundary to swap behind, so each new approach is layered on top of the
old ones instead of replacing them.
Hampton's comparison is Linux, which runs Windows programs through Wine and Proton: the legacy is a
guest behind an explicit layer, and the host underneath stays replaceable.

## That is what the skills' boundaries are for

Hampton's point is that this is why the skills insist on contracts and separation of concerns.
Units meet only at explicit contracts: a caller builds from the public API and the spec, with no
third source (`contracts` 1). A dependency with no contract is wrapped behind one (`contracts` 8).
Each unit does one thing, and a concern that cuts across others is their peer (`simplicity` 1 and
2). Together they keep each how behind a boundary small enough to replace.

A contract converts unknowns into known behaviour. That removes coupling to anything left unknown,
and coupling, in Hampton's view, is a very expensive design choice. A caller that depends on a
contract has a claim: if the other team breaks it, the caller reports a bug and the fix is theirs. A
caller that depends on undocumented behaviour has none: if the other team changes it, the caller can
lose weeks negotiating to get it changed back. Hyrum's law says such behaviour will be depended on
anyway. The contract decides whose problem it is when it changes.

The same boundary is what makes an agent's output auditable. A person reads one unit at a time,
with only its contract in view: less to hold in mind, and one thing to focus on. That reduction in
cognitive load is what `simplicity` exists for.

The skills hold themselves to it. Set them beside the chief-of-staff pattern for orchestrating
Claude Code sessions.[^cos] As Claude reads it, its loop checks that work was done correctly against
a validation contract (re-run the claimed commands, read the diff, make the verifier fail first),
and does not ask whether the contract is the goal. Its machinery scales the production of the how.
And it has to be taken whole. Without its durable store, it says, "you are not running this pattern,
you are running several sessions and hoping." These skills trigger on events in whatever workflow is
running ([0020][0020]), so one of them can be taken alone into a solo session, a team, or that loop.

## Inexpensive to write is not inexpensive to verify

A replacement is safe only when three things hold. The spec is complete, meaning it cannot be met
while the goal is missed (`spec` 10). The contract holds (`contracts` 1 and 2). And the checks
assert the goal, not the implementation (`definition-of-done`). Cheap rewrites move the cost from
building to verifying, and the skills sit on the verifying side.

## Where the how still gates

The how stops being a detail where it holds state, or has callers you do not control:

- **Data.** The migration is the cost, not the engine.
- **Published contracts.** Callers you cannot see depend on them.
- **Irreversible or regulated actions.**

`contracts` 4 already says data dominates: the structure is the contract's substance, so a data
shape at a boundary is part of the what. Scale is the other exception, which Hampton puts as
Amazon's case. At that scale the backend is either the constraint, or it is sold, as AWS was. Once
it is sold it is no longer a how. It has its own users, and it is judged as a product.

## Replaceable, not disposable

Hampton first put it as wanting to throw things away, with boundaries there to make that possible.
He then refined it: disposable is an anti-principle. A good product can be repaired, recycled or
repurposed. Good software may not last, but at the least it leaves lessons and moves toward a better
next version. Boundaries exist so that a part can be replaced while the whole keeps evolving. That
is continuous improvement, and the industry term for the architecture is evolutionary.[^ford] The
lessons outlive the code, which is what `durable-context` and the essays are for.

The prior art is David Parnas, who decomposed systems by the design decisions likely to
change,[^parnas] and tef's "write code that is easy to delete, not easy to extend".[^tef] It is not
Fred Brooks's "plan to throw one away". That was a whole system thrown away once, written before
the modularity existed to rebuild one part, and Brooks later withdrew it in favour of building
incrementally.[^brooks]

Inexpensive to replace is not the same as cheap. In Hampton's terms, cheap is cutting corners: a
replaceable how is still built well.

The same distinction settles duplication. Sandi Metz's "duplication is far cheaper than the wrong
abstraction"[^metz] is right about code inside a replaceable unit. DRY, as Hunt and Thomas defined
it, is about knowledge, not code.[^dry] Duplicated infrastructure, such as two auth systems or two
stores of the same customer, is a fact with two owners, and that is what DRY forbids. Read that way,
Metz and DRY do not conflict.

## Still open

- **Should a decision's record scale with how reversible it is?** One-way and two-way doors
  ([#126][126]).
- **Does `spec` weigh prototyping too lightly** when the how is inexpensive to build ([#125][125])?
- **Which skill asks for a check to fail before it is trusted** ([#124][124])?

## What it shapes

- A choice of engine, cloud or framework is judged by how much of it leaks past its boundary, not by
  the choice itself.
- Review time goes to the what and to verifying the replacement, not to arguing over the how again.
- Where the how does gate (state, published contracts, irreversible actions), it gets the scrutiny
  the rest no longer needs.

## Notes

The claim, the boundary that makes it hold, and the refinement from disposable to replaceable are
Hampton's, from the 2026-10-05 session. The working notes are in [#89][89]. The prior art and the
mapping to specific rules are Claude's.

## Revisions

- **v1.0 · 2026-10-06 · Claude Opus 5.5.** First version.

[0020]: ../decisions/0020-spec-triggers-on-events-and-builds-the-goal-with-its-owner.md
[89]: https://github.com/cobarx/build-skills-cobarx/pull/89
[124]: https://github.com/cobarx/build-skills-cobarx/issues/124
[125]: https://github.com/cobarx/build-skills-cobarx/issues/125
[126]: https://github.com/cobarx/build-skills-cobarx/issues/126

[^cos]: Mithushan Jalangan, "Orchestrating Claude Code Agents: The Chief of Staff Pattern",
    asyncdot, 19 September 2026,
    <https://asyncdot.com/blog/chief-of-staff-pattern-orchestrating-claude-code-sessions/>.
[^cockburn]: Alistair Cockburn, "Hexagonal architecture", HaT Technical Report 2005.02, 2005,
    <https://alistair.cockburn.us/hexagonal-architecture/>.
[^fowler]: Edward Hieatt and Rob Mee, "Repository", in Martin Fowler, *Patterns of Enterprise
    Application Architecture* (Addison-Wesley, 2002), catalogued at
    <https://martinfowler.com/eaaCatalog/repository.html>: "Mediates between the domain and data
    mapping layers using a collection-like interface for accessing domain objects."
[^ios]: Apple, *Cocoa Fundamentals Guide*, "What Is Cocoa?", updated 18 September 2013,
    <https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CocoaFundamentals/WhatIsCocoa/WhatIsCocoa.html>.
    The iOS Core Services layer "includes both Foundation and Core Foundation", and UIKit takes
    the place AppKit has on the Mac.
[^hyrum]: Hyrum Wright, "Hyrum's Law", <https://www.hyrumslaw.com/>: "With a sufficient number of
    users of an API, it does not matter what you promise in the contract: all observable behaviors
    of your system will be depended on by somebody."
[^ford]: Neal Ford, Rebecca Parsons and Patrick Kua, *Building Evolutionary Architectures*
    (O'Reilly, 2017): "An evolutionary architecture supports guided, incremental change across
    multiple dimensions." As quoted on Ford's page for the book,
    <https://nealford.com/books/buildingevolutionaryarchitectures.html>.
[^parnas]: David L. Parnas, "On the Criteria To Be Used in Decomposing Systems into Modules",
    *Communications of the ACM* 15, no. 12 (December 1972): 1053-58,
    <https://doi.org/10.1145/361598.361623>: "one begins with a list of difficult design decisions
    or design decisions which are likely to change. Each module is then designed to hide such a
    decision from the others."
[^tef]: tef, "Write code that is easy to delete, not easy to extend.", *programming is terrible*,
    13 February 2016,
    <https://programmingisterrible.com/post/139222674273/write-code-that-is-easy-to-delete-not-easy-to>.
[^brooks]: Frederick P. Brooks Jr., *The Mythical Man-Month*, anniversary edition (Addison-Wesley,
    1995), chapter 19, p. 265: "'Plan to throw one away; you will, anyhow.' This I now perceive to
    be wrong, not because it is too radical, but because it is too simplistic." The original advice
    is chapter 11 of the 1975 edition. The 1995 wording is quoted from a comment on Tim Bray,
    "Build One to Throw Away", 22 August 2008,
    <https://www.tbray.org/ongoing/When/200x/2008/08/22/Build-One-to-Throw-Away>, and not checked
    against the book.
[^metz]: Sandi Metz, "The Wrong Abstraction", 20 January 2016,
    <https://sandimetz.com/blog/2016/1/20/the-wrong-abstraction>.
[^dry]: Andrew Hunt and David Thomas, *The Pragmatic Programmer* (Addison-Wesley, 1999): "Every
    piece of knowledge must have a single, unambiguous, authoritative representation within a
    system." Wording checked against the 20th anniversary edition (2019), Tip 15,
    <https://media.pragprog.com/titles/tpp20/dry.pdf>.
