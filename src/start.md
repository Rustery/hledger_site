# Get Started

<div class=pagetoc>

<!-- toc -->
</div>

Starting out with hledger and Plain Text Accounting, not to mention setting up a new accounting system, can be a lot to take in. This page aims to help!
After [installing](install.md) hledger, reading some of the docs below should be helpful.

## Quick starts

We have (too many) quick introductions. These assume a little bit of command line know-how:

- [Home page quick start](index.md#quick-start)
- [2 minute quick start](2-minute-quick-start.md)
- [5 minute quick start](5-minute-quick-start.md)
- [hledger manual: Common tasks](hledger.md#common-tasks)
- [Common workflows](common-workflows.md)

## Tutorials

Detailed step by step tutorials, with screenshots:

- [Tutorial: hledger basics](basics.md)
- [Tutorial: hledger-web](web.md)
- [Tutorial: hledger-ui](ui.md)
- [Tutorial: Accounting basics and further study](accounting.md)
- [Importing CSV data](import-csv.md)

## Videos

- [hledger fan's beginner videos](https://www.youtube.com/channel/UCZLxXTjOqLzq4z5Jy0AyWSQ/videos) cover some hledger basics
- [Videos](videos.md) has some old talks and presentations

## Manuals

The manuals are hledger's authoritative documentation, and the most maintained and accurate of the docs. Read them to know exactly what hledger does.

You can also view the hledger manual in the terminal with [`hledger help`](hledger.md#help).

- [hledger manual](hledger.md)
- [hledger-ui manual](hledger-ui.md)
- [hledger-web manual](hledger-web.md)

## How-tos

Practical advice and examples for real-world tasks:

- [FAQ](faq.md)
- [Cookbook](cookbook.md)

See also:

- [hledger's examples/ directory](https://github.com/simonmichael/hledger/tree/master/examples)
- [wiki.plaintextaccounting.org](https://wiki.plaintextaccounting.org)  general PTA tips, not hledger-specific
- [plaintextaccounting reddit](https://www.reddit.com/r/plaintextaccounting/new/) discussion of various PTA topics
- [PTA blog posts](https://plaintextaccounting.org/#articles-blog-posts) (old)

## Support

- See the [Support](support.md) page, especially the #hledger chat and hledger mail list

## Advice

Here are some thoughts on how to approach hledger and accounting.

### Little and often

Accounting is an ongoing activity, best done in regular small doses.
The more often you do it, the easier it is, because less has happened and you can remember it.
Ten minutes daily can achieve a lot. (Or less, once you get a routine going.)

### Small steps

You can start using hledger in very simple ways, and get immediate benefit.
Prioritise your work: a good way is to think about your most pressing needs and what kind of report would help.
For example,

- Take inventory of your debts, loans and assets; write down the names and numbers.
- Record these as "opening balances" transactions (as in the quick start docs).
- Make corrections until hledger shows your balances accurately.

Or:

- Start recording changes to the cash in your wallet, starting with today's balance.
- Then start reconciling daily (comparing the reported and actual balance, and troubleshooting any disagreements).
- Then start tracking the balance in your checking account.
- Then start tracking your other bank accounts.
- Then start categorising your incomes and expenses.
- Then find your bank transaction history and manually enter the transactions from the previous week.
- Then manually download your bank transactions as CSV and develop CSV rules so that you can print the CSV as journal entries.
- Then try downloading and importing this CSV into your journal daily for a while.
  (Only if you wish. Many people stick to manual data entry for the increased awareness it brings.)

If the task feels unclear or overwhelming, I recommend this small steps, verifiable reports approach.

If not, of course feel free to blaze away and do it all on day one.
But I would still recommend establishing a frequent reconciling routine.
It is *surprising* how quickly small events can slip through the cracks and create chaos,
and it takes a little time to develop the troubleshooting skills.
Reconciling often will save you time.

### Imperfection

Your bookkeeping does not have to be perfect or even very accurate [1].
As you practice, you will naturally learn more about the tools and
about double-entry accounting,
such as how to organise your account categories,
and how to write effective journal entries for various real-world events (transactions).

Later you can come back and improve your old journal entries if you wish.
You can decide what level of accuracy you need.

[1] Though if you really catch the PTA bug, you may find that nothing less than perfection will do!

<!--
Notes

I'll throw out the obvious: read the docs at hledger.org. Particularly the reference manuals for hledger and hledger-web - these are also available as local man pages and info manuals - but hledger.org has them with useful hyperlinks, and has additional docs such as Get Started, FAQ, Cookbook and Developer docs. Clearly you shouldn't have to read this.. library.. up front, but at least survey everything, including the tables of contents, to get a sense of where things are.
There's also a Videos page; and at https://plaintextaccounting.org/#articles-blog-posts , many bite-sized blog posts. These can be a nice alternative when reading docs gets boring.
There's a lot of rabbit holes you can go down when learning PTA, so setting some goals and managing your focus is helpful. Lisp, Haskell and Emacs are also big topics and definitely not needed for hledger use, though very fun and worthwhile in themselves.
You can always browse the mail list archives for past discussions that look interesting. And I will always recommend joining the hledger chat - a little bit of a hoop but not much. Checking the discussion there once in a while, or asking when you get stuck, can save a lot of time.
(answer to:
 B: I am not a coder/programmer/software professional—just a numbers-inclined user who is old enough to remember pre-GUI computing, appreciates the philosophy of plain text accounting, and had dabbled with code (Processing, Arduino, and HTML/CSS once upon a time).
 ...
 Now, I’m wondering if anyone here could offer some guidance towards a strategic course of study that would help me get the most out of hledger? Should I learn Lisp? Haskell? Maybe focus on understanding how to use Emacs?
 I do believe that continued use of hledger will drive more learning (It already has!) but I can’t help but think that troubleshooting as questions and issues arise isn’t the only (or most effective) way. There’s a lot of lingo, terms—a whole universe truly—that is new to me and I’m curious now that I have arrived where others might recommend I start to get a better sense of the lay of the land so to speak.
)

-->

