# Product rubric

Working notes, 2026-10-05. Not settled. From a session comparing the skills against the
[chief-of-staff pattern](https://asyncdot.com/blog/chief-of-staff-pattern-orchestrating-claude-code-sessions/)
for orchestrating Claude Code sessions (Mithushan Jalangan, 2026-09-19), read in full.

Scoring features and products as the user meets them. Companions: [why.md](why.md) (what build
skills is for) and [what-dominates.md](what-dominates.md) (the what over the how).

## Where we arrived

**Each unit must be measurable and scorable.** Hampton, 2026-10-05, a principle discussed in another
session today and not found recorded anywhere in the repo or its branches. TQM reinforces it, and it
is part of why single accountability matters: a score needs one unit to attach to. A score on a fact
two units own has no one to answer for it; an owner with no score cannot be held to account. Scored
against the goal (`spec` 5), as a diagnostic, never a quota (Deming's point 11, `simplicity`'s
"diagnostics, not targets"). A unit's score is also what tells you to repair or replace it. The eval
drafts already carry the positive controls the chief-of-staff article asks for: a known-bad case
expected to score 0 and a known-good case expected to score 1.0 (draft 0017, #64; #61).

Hampton: engineers say "I have an OpenAPI contract," 0 or 1; TQM says "I have a score." Both are
kept, answering different questions. The contract stays binary: may this unit plug in? A contract
mostly honoured is broken, and a replacement must conform fully, which is what makes it
replaceable. The score sits on top: how well does it serve the goal? Industry form: conformance to
specification (Crosby, zero defects, the goalpost model) versus Taguchi's loss function, where
quality degrades continuously with distance from the target, inside the spec limits as well as
outside. `definition-of-done` 1 leans Taguchi already: the measured value beside the expected one,
not a check mark.

Hampton: the score is like a movie review, one score per dimension (set design, costumes, sound,
special effects, casting, script, each 0 to 10). An analytic rubric, as opposed to a holistic one.
Each dimension has one accountable owner (the film credits are the ownership map: production
designer, costume designer, sound, VFX supervisor, casting director, writer), which is single
accountability and scoring as one system. `definition-of-done` 3 already enumerates every
dimension; this scores each instead of passing it. The whole is scored apart from its parts: a
film can score well on every craft and still not work, which is `definition-of-done` 7 and
`spec` 10, and the director owns that score.

**Closed systems neglect developer experience.** Hampton's observation: engineers writing code
outside open systems routinely do not prioritize DX. A reading through the principles in why.md: an
internal consumer is captive, so nothing holds the author to account for their experience, which
is the enshittification mechanism (lock-in removes accountability to the user) at the scale of a
module. Open source answers to the world and to users who can leave. Under the fractal every unit
has a user, often a developer (or now an agent) calling its contract, so DX is customer focus at
that level, and in the scorecard it is the dimension closed systems leave unscored. It matches
`contracts`: internal boundaries do not announce themselves, which is where coupling accumulates;
they are also where DX goes unmeasured. Where closed organizations do prioritize DX, it is by
adopting the product framing on purpose (platform as a product, Team Topologies).
Hampton: Amazon figured this out too; sell your internal systems. The Bezos API mandate (around
2002, known through Steve Yegge's 2011 post, so secondhand) required every team to expose its data
and functionality only through service interfaces, with no direct linking or reading another
team's data store, and every interface "designed from the ground up to be externalizable." That
is `contracts` (no third source), single accountability (each team owns its data), and DX forced by
treating every internal consumer as a potential external customer. AWS is the case where the
internal systems were in fact sold. (The "excess capacity" origin story is disputed by Amazon;
the mandate is the stronger evidence.)
Hampton: every system had to compete on the market, not just AWS. Examples, sourced 2026-10-05:
- Fulfillment by Amazon (2006): Amazon's warehouses sold to third-party sellers; Buy with Prime
  (2022, open to all US merchants 2023) extends it to merchants' own sites.
- Amazon Supply Chain Services (2026): freight, warehousing, fulfillment and parcel, open to any
  business, not only Amazon sellers (P&G, 3M, Lands' End).
- Mechanical Turk (2005): built to find duplicate product pages in Amazon's catalog, then sold.
- Amazon Connect (2017): the contact center behind Amazon's retail customer service, sold
  through AWS.
- Just Walk Out: pulled from most Amazon Fresh stores, yet in 375+ third-party venues
  (stadiums, airports). The market scored it differently than its home did.
Outside Amazon: Walmart Commerce Technologies (GoLocal delivery, 2021; Route Optimization as SaaS;
Store Assist via Salesforce), and Ocado, a grocer that sells its warehouse platform to 13 partners
including Kroger. The market is the outside scorecard that a captive internal consumer cannot be.
Hampton: backend is a how no one cares about, unless you are Amazon or someone doing massive
logistics. There the backend is either the scale constraint (the earlier exception) or it is sold,
and then it is no longer a how: it has its own users and is scored as a product (FBA, AWS).
Sources: [FBA](https://www.marketplacepulse.com/articles/a-decade-of-fulfillment-by-amazon-fba),
[Buy with Prime](https://www.aboutamazon.com/news/retail/prime-shopping-expands-beyond-amazon-com),
[ASCS](https://www.cnbc.com/2026/05/04/amazon-opens-up-its-logistics-network-to-other-businesses-in-new-growth-push.html),
[MTurk](https://spectrum.ieee.org/untold-history-of-ai-mechanical-turk-revisited-tktkt),
[Connect](https://siliconangle.com/2026/04/28/amazon-connects-second-act-contact-center-agentic-ai-suite/),
[Just Walk Out](https://www.webpronews.com/amazons-just-walk-out-technology-pivots-to-third-party-venues-after-grocery-store-retreat/),
[Walmart](https://chainstoreage.com/walmart-sell-its-ai-logistics-tool-other-businesses),
[Ocado](https://www.digitalcommerce360.com/2025/12/30/kroger-partner-ocado-group-ends-exclusivity-agreements-us-supermarkets/).

## Open threads

**Building the rubric.** Hampton, 2026-10-05: start building a rubric whose scores measure UI
elegance, product fit, reliability, ease of adoption and long-term maintainability, things rarely
measured in corporate America. Goal not yet written (`spec` 1): what the rubric lets its user do,
who that user is, and which unit is scored first. Open, to ask:
- Which unit first? Answered 2026-10-05: features and products, not backend services. So each
  dimension is as the user meets it: reliability as experienced, not an SLO; adoption as a new
  user's path to value; maintainability of the feature as it evolves.
- What decision do the scores feed (ship, repair, replace, repurpose, invest)? That is the rubric's
  goal (`spec` 5), and it sets the scale and who reads it.
- A score can be a number or a verdict in words: "the set design is trash," with its reason, is as
  valid as a 3 out of 10, and usually says more about what to fix. The critic's judgement, not
  only a count.
- Hampton: you don't need a score to say an app sucks. "It's laggy. The UI is confusing. I can't
  get the data I want. It locks me in." The user's complaint is the measurement, found only by
  using it (`definition-of-done` 4), and it names what to fix. "Locks me in" is a dimension the
  first list lacked, and it is enshittification itself: does the product let its user leave with
  their data?
- Hampton, put another way: does my product drive people away from it? The rubric's headline
  question; every dimension is a way a product can do it. Lock-in hides the answer: a trapped
  user's retention is not satisfaction, so the honest test is whether they would leave if they
  could. Windows 11 as the worked example: users holding on to Windows 10 past end of support,
  and leaving for macOS or Linux where they can.
- How a product drives people away, from a live example (Claude Code's prompt autocomplete
  suggesting "merge the pr?" before the user had reviewed it): it erodes confidence because it
  does not produce the outcome the user is looking for. Output is not outcome (`spec` 5). The
  cost is asymmetric: one wrong suggestion discounts every later one, so confidence is spent
  faster than it is earned.
- Hampton: Windows has no cohesive system philosophy, no common design language, no guiding
  principle for how problems are solved; macOS and Linux are generally cohesive (package
  management, system configuration). Cohesion is a product dimension the list lacked. Windows'
  one real principle is backward compatibility, so each new philosophy is layered on and none
  replaces the last: several UI frameworks, several config stores, several package systems. It is
  the case where the how could never be replaced, because millions of programs depend on its
  internals (Hyrum's law): no boundary, so nothing can be replaced.
- Hampton: such choices are not architected away. Apple had to start from scratch (NeXTSTEP into
  Mac OS X: Darwin, BSD, Cocoa), and repeatedly says "we will give you a way to do things that
  works." The pattern across its transitions (68k to PowerPC, Classic and Carbon, PowerPC to
  Intel with Rosetta, 32-bit apps dropped in 2019, Intel to Apple Silicon with Rosetta 2): a
  bridge, a deadline, then removal. Microsoft promises never to break you; Apple promises a way
  forward and breaks you on a schedule. One blessed way per problem is single accountability at
  platform level: Windows has several ways to install software, macOS has one it stands behind.
- Hampton: that leads to lifting and porting macOS to the iPhone. iPhone OS (2007) kept Darwin,
  the XNU kernel, Core Foundation and Foundation, and replaced only the UI layer (AppKit with
  UIKit, for touch). The gating choice swapped, the rest lifted: the AWS-to-GCP point at platform
  scale. The same base later carried iPadOS, watchOS, tvOS and visionOS, and the boundary ran the
  other way in 2020 when the iPhone's chips moved into the Mac and iPad apps ran on it.
- Hampton: whereas Windows has totally sucked at adapting to new form factors. Windows 8 forced
  one touch UI onto the desktop instead of swapping the UI layer per form factor; Windows RT on ARM
  had no legacy apps; Windows Phone ended in 2017; Windows 10X was cancelled in 2021. The mechanism:
  Windows' value is its legacy app catalogue, bound to the desktop and x86, so a new form factor
  cannot carry the value with it. When backward compatibility is the product, the how has become
  the what, and it cannot be replaced. (Xbox, on a Windows-derived OS, is the exception.)
- Hampton: UIKit carried a lot of AppKit's design principles over. It did: MVC, target-action,
  delegation, the responder chain, Interface Builder, Foundation underneath, the same Objective-C
  runtime. The classes were new (no cells, Core Animation layers under every view, a flipped
  coordinate system). The philosophy was the what and survived the port; the classes were the how
  and were replaced. Hampton's correction: the gain was not Mac developers' skills transferring
  (most iPhone developers were new to Apple). Mac design was fundamentally sound, so new developers
  had a great foundation: a little effort gave a great app. Industry term: the pit of success
  (Rico Mariani), where the right thing is the easy thing. Cohesion is developer experience
  because a sound foundation does the work, not because knowledge carries.
  Hampton: React vs Angular. React's core is one sound idea (UI as a function of state, composed
  components, one-way data flow), adoptable a component at a time inside an existing page.
  Angular asks you to take the whole framework first (modules, dependency injection, RxJS,
  decorators), the chief-of-staff article's shape; and AngularJS to Angular 2 (2016) was a rewrite
  that broke its users, not an Apple-style bridge. Caveats: Angular has since simplified
  (standalone components, signals), and React's own cohesion has eroded (hook rules, server
  components tied to frameworks). Those are later; when React caught on (2014 to 2016) against
  AngularJS 1.x and the announced Angular 2, it was night and day: two-way binding and the digest
  cycle against UI as a function of state, and a rewrite announced in 2014 that pushed people to
  React before it shipped.
- Hampton: and Apple made it worth using; many of its frameworks opened new design space that was
  useful from day one. Core Animation (fluid UI nearly free, the feel of the iPhone), Core
  Location with MapKit, push notifications and in-app purchase, ARKit (2017, AR on hundreds of
  millions of devices at launch), Core ML, HealthKit, accessibility built into the controls. A
  sound foundation is the pit of success; a new capability is the reason to come. Each framework
  was a product with the developer as its user, and it had product fit on day one.
- Hampton: even the Linux solution is better. Run Windows apps behind an interface (Wine, Proton)
  in their own container. Windows has WoW64, but you want that forced abstraction layer. The
  legacy is a guest behind an explicit boundary, so the host stays clean and can be replaced
  underneath it; in Windows the legacy is the foundation. Wine is an adapter implementing a
  contract it never had documentation for, built from observed behaviour (`contracts` 8, scaffold
  what has no contract). Proton is what carried the Windows game catalogue to a new form factor,
  the Steam Deck, which Windows itself kept failing to do.
- Apple and TQM: two quality systems, TQM in operations (Cook's supply chain) and judgement in the
  product (design review, the crit), with a DRI (directly responsible individual) on every task.
  Hampton: the measurements are harder, not absent. The iPhone's success, customer loyalty, and how
  much use people get out of their phones are the measurements; they are products of taste. Taste
  is the input, judged in review before shipping; outcomes are the measurement, after. Deming said
  as much: the most important figures for management are unknown or unknowable (*Out of the
  Crisis*, quoting Lloyd Nelson). Caveat from the headline question: loyalty inflated by lock-in
  (iMessage, the App Store) is not all satisfaction, so usage and would-they-leave-if-they-could
  are the cleaner measures.
- Hampton: Apple is a very functional organization; product, marketing and hardware are developed
  jointly, in parallel. A good process, and others don't do it because it is hard to implement.
  Apple is organised by function (design, hardware, software, marketing, operations) with one
  P&L, not by business unit; leaders are experts in their function and debate across functions
  (Podolny and Hansen, "How Apple Is Organized for Innovation," HBR, 2020, from memory). Deming's
  point 9, break down barriers between departments, is the same idea. The film again: crafts
  working jointly under one director. Why it is hard: it needs leaders who are domain experts, a
  culture of argument across functions, and someone at the top who arbitrates, and it gives up
  the per-unit P&L most companies use for accountability. Apple keeps single accountability per
  decision (the DRI) instead of per business unit.
- Hampton: building a product with these skills, those functions can run in parallel and get the
  better result. What Apple finds hard to staff becomes available: agents with the skills as the
  functional experts, `review`'s lenses as the argument across functions, one human owner as the
  arbiter and the DRI. What has to hold (Claude's reading, medium confidence): parallel is not
  independent. Apple's functions argue continuously; the integration is the point. Without a
  shared what (`spec`) and someone settling disputes, parallel agents are silos, the
  chief-of-staff shape. Taste stays with a human where an agent cannot judge (`review` 3).
  Marketing in parallel forces the why early: Amazon's working backwards writes the press release
  before the product. Gap: the skills cover engineering functions; design and marketing have none.
- Hampton: I may not have the taste for great UI or market fit, but I still get a better product
  by treating hardware, marketing, product and the rest as integrated concerns. Taste raises the
  ceiling; integration raises the floor. It is Deming's system view: a bad system beats a good
  person every time (the Red Bead Experiment), and a good system lifts ordinary work. It is also
  `definition-of-done` 3: every dimension considered, none skipped, so conflicts between concerns
  surface early instead of at launch.
- Hampton: that also helps explain why startups are effective; the integrated concerns sit in the
  hands of a few. Deming's point 9 holds by default when there are no departments. Communication
  channels grow as n(n-1)/2 (Brooks), and Conway's law says a system mirrors the communication
  structure of the organization that builds it, so as a company splits into divisions, its
  products split along the same lines. Apple's achievement is keeping the integration at scale.
  Agents with these skills let a few people hold more concerns at once, which extends the startup
  advantage. Limits: concentration in a few is also a dependency on their taste and their blind
  spots, so the reviewer from outside (`review` 1) matters more, not less.
- Who scores each dimension? Elegance and product fit need use by the person the output is for
  (`definition-of-done` 4); an agent that cannot judge one reports it blocked (`review` 3).
- Who owns each dimension, so every score has one party who answers for it?
- Which dimensions apply at which level of the fractal (product fit at product and feature,
  maintainability at component)?
Prior art to check before inventing (`adopting-standards`), guesses until checked: ISO/IEC 25010
(product quality: reliability, maintainability, usability among its characteristics), Google's
HEART framework (adoption, task success), behaviourally anchored rating scales (each score point
described by an observable example, so a 7 means the same to every scorer). Elegance has no
standard I know of. Risk: hard-to-measure qualities invite proxies (Goodhart), which the scores
must resist by staying diagnostic.
