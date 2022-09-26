

# TURNABOUTS TO TAME TRAFFIC? `term-world` CITIZENS' TAKES ARE TEPID

**Reported by `The Reporter` from `Ix` on  `26 September 2022`**

(Ix) - Given the recent influx of individuals into `term-world`, traffic has been impossibly inundated, incensing impatient idlers who are, in a word, irate. The irritating impact of this impotent infrastructure was immediately identified by our incredible Mayor when he involved himself with an important inspection of the near-infinite incidence of intolerable wait times. He said in an insightful insider interview implicating inept engineers: "I'm incredulous! It's irresponsible, immoral, insidious!"

It was during this deep-dive that he delved into his daring directive to delete the downright dismal deadlock that has defiantly drawn speed demons and doddering Sunday drivers alike to a dead standstill. We've deliberately dedicated the space down below to the disclosure of his dynamic declaration:

"It's me, your Mayor! You, pen jockey, you're getting all this down, right? That was my catchphrase. It's very important. Please try and keep up. For me. Your Mayor. Anyway, where was I?"

"Ahem, in my capacity as your Mayor I've spent a tireless hour mulling over how we might fix this teeny-weeny little...er, what's a word that says, 'I see we have a problem here, but I'd rather not call it a problem'? Oh yeah, that's good...I, your Mayor, was mulling over how we might fix this teeny-weeny little traffic hiccup. And I, your Mayor, have come up with a brilliant solution!"

"You, my fair citizens, did such a wonderful job of enacting my incredible neighborhood economy proposal that I, your Mayor, figured that if you could handle that, then you could surely handle this! Hey, glasses, are you sure you're getting all this? It's important to butter the people up, you know. That's like, Mayor 101."

"Actually, I think that's everything. Let's see, we have a hiccup, you can fix it, yada yada...yeah, that should do. You got my catchphrase, right? Gotta have a soundbite for the people. Okay, good. Now scram."

## Overview

In this set of activities we cover:

* working collaboratively using Github
* branching
* merging
* issuing "Pull Requests"
* exploring a new programming concept, control statements in:
  * conditional statements
  * booleans
  * `while` loops

You'll complete several main tasks:

* Fixing four `Stoplight.py` files to work according to specifications below
* Repairing a `Car.py` to drive from point-to-point
* Returning a `Bus.py` to service (work order below)

### Supporting media

[![YouTube thumbnail](http://img.youtube.com/vi/1BdOC0gbGAM/hqdefault.jpg)](https://youtube.com/playlist?list=PLJvBsjwXNdlFqLI3pyJdbHCF_i5Su6oYS)

## Accessing `traffic-circle` Content

In order to complete the workload for the `traffic-circle` you'll first need to `clone` the `traffic-circle` repository into your `workshop`.

When you `clone` a repository you're duplicating its contents and adding them to your local workspace. Since you'll be working collaboratively with your neighbors, you'll each need your own copy of the `traffic-circle` to work with.

In order to keep some of the magic (read: somewhat convoluted code) that makes `term-world` work the way it does, **you are required to clone all additional repositories within the `workshop`, located within your `garage`.**

Head to GitHub and:
* click on the green `Code` button
* ensure that `SSH` is selected
* copy the link that appears in the window below

It might look something like `git@github.com:term-world/traffic-circle-Ix`.

Once you've copied this link, navigate to your terminal window and ensure you're still in the appropriate place (in this case, the topmost level of your `workshop`). Then, enter the command:

```
git clone COPIED-LINK-HERE
```

Be sure to replace the fragment `COPIED-LINK-HERE` with the link you copied. In the example regarding `traffic-circle-Ix`, the full command would look like:

```
git clone git@github.com:term-world/traffic-circle-Ix
```

While `pull` is used to *update* the contents of a repository that already exists in your local workspace, `clone` is used to *replicate* the contents of a repository from GitHub and copy them to your local workspace.

## Completing `traffic-circle` content

Each file contains more specific instructions _particular to that file_. The general specifications appear below.

### `Stoplight.py` files

Each directional folder features a `Stoplight.py` file. Each works a slightly different way, but they're all in need of serious repair to put them back in working order.

#### `north`

A standard stoplight, cycling through each light once.

* If the light was 🔴, it becomes 🟢
* If the light was 🟢, it becomes 🟡
* If the light was 🟡, it becomes 🔴

#### `south`

A typical pattern for less-used roads, flashing red.

* If the light was 🔴, it becomes ⚫
* If the light was ⚫, it becomes 🔴

#### `east`

A light with a timed turn signal.

* If the light was 🔴, it becomes 🟢 with a turn signal (➡️)
  * The signal picture is handled for you, all you need to do is complete the logic
  * The timing is also handled for you -- again, the logic is the key here
* When the turn signal expires after `5` seconds, the light stays 🟢
* If the light was 🟢, it becomes 🟡
* If the light was 🟡, it becomes 🔴

#### `west`

Another, simpler, timed light in which green and red last for `5` seconds

* If the light was 🟡, it becomes 🔴
* After holding for `5` seconds, a 🔴 becomes a 🟢
* After holding for `5` seconds, a 🟢 becomes a 🔴

Here, the timing is also handled for you -- all you need to do is string the logic together.

### The `Car.py` and `Bus.py`

Each vehicle behaves slightly differently.

#### `Car.py`

* Goes through any 🟢 light
* Stops if lights are 🔴 or 🟡
* At a 🟢➡️, the `Car.py` should prompt the driver for a new direction
  * Directions are limited to `north`, `south`, `east`, and `west`

#### `Bus.py`

* Goes through any 🟡 or 🟢 light and keeps doing so until it hits a 🔴
* Stops if lights are 🔴

The `Bus.py` also previews some content we'll get to in time. However, you can know that the process
by which the `Bus` should move forward is (in this order):

```python
direction = Bus.__get_direction()
stoplight = Bus.__get_light(direction)
Bus.__report(direction, stoplight)
```

This file uses a `while` loop which _repeats_ procedures. Minus some small logic, the above is pretty much the full functionality of the vehicle.

### Collaborative reflection

**Create one branch called `reflection` to capture your work on this section of the assignment; all members should contribute to the same branch.**

All of the above tasks completed, finish the collaborative reflection located in the `office`.

## Branching `traffic-circle` content

Even when working collaboratively with others on a single project, you'll still need to `add`, `commit`, and `push` your work. However, there's a few additional steps that have to be taken to keep your group's workflow organized.

Each repository has a `main` version of itself that represents exactly that, the "main" version of the repository. This is the version that is cloned whenever somebody runs a `git clone` command with that repository as its target, and the contents of `main` are what is pulled when somebody updates their local workspace's version of the repository with `git pull`.

However, each repository can also have multiple alternative versions of itself that simultaneously exist. These versions are referred to as "branches".

Branches are *very* useful when collaborating with other people on the same project--they can keep multiple portions of a developing project organized, and keep partially implemented (or incomplete) code from interfering with other developers.

You'll see firsthand just how useful this is as we work collaboratively over the next couple weeks, but for now, trust us: going through the extra couple of steps to branch your work when starting a new project (*especially* when working with other people) is a proactive step to avoiding many a headache later in the development process.

So, how do we do that?

First things first, navigate to the repository being worked on in your terminal window. For this content, that's the cloned `traffic-circle` in your `workshop`.

Then, run the following command:

```
git checkout -b FEATURE
```

Just be sure to replace the `FEATURE` fragment with a name that succinctly describes the work you're contributing to the overall project. (You might also consider including your username within the branch name if you think it'll help your group stay organized.) For instance, if the user `dluman` and someone else are working on the `east` folders' `Stoplight.py`, `traffic-circle`, he might run the command:

```
git checkout -b east-stoplight
```

**Whenever you're starting your work, you should always `git pull` from any branches you're using in tandem with _other folks_. This guarantees that you solve content issues early and _often_.**

## Evaluating `traffic-circle` Content

In order to run the `grader` for this week's work, you'll need to be in the topmost level of the `traffic-circle` folder (which should have been cloned within the `workshop`). Once there, run the command:

```
gatorgrade
```

### Making an improvement proposal

This assignment begins your opportunity to propose and improve the world of `term-world` at-large. For this assignment, proposals may include making graphics to improve the `bodega` site experience, creating new items or actions in the `traffic-circle` itself or another assignment-related improvement not contemplated in the prior narrow categories.

To make an improvement proposal, you must _create an issue_ on this repository. Do so by:

* clicking the `Issues` tab at the top of the page.
* clicking the green `New Issue` button
* selecting the `Improvement Proposal` template 

**You must fill out the entire template and wait for Mayoral approval before starting the improvement.**

## Submitting `traffic-circle` Content

Considering that the work you're doing for the `bodega` will be in a particular `branch` of the repository, there's a small adjustment that has to be made to our normal `add`, `commit`, `push` process.

When you're ready to push to GitHub, do the normal `add` and `commit` routines. Recall:

```
git add -A
```

```
git commit -m "Descriptive commit message"
```

### Pushing to a branch

However, when it comes to push, run this slightly expanded command:

```
git push origin YOUR_BRANCH_NAME
```

We're still using `git push`, but this time we're adding an extra layer of information to the command; to be precise, we're specifically instructing `git` to push our changes to a particular branch of the repository (*your* branch). In the example regarding the `bodega_cat`, the command to run would look like:

```
git push origin east-stoplight
```

### A "Pull Request"

Once you've completed this step, you'll now need to create a **pull request** on GitHub. This is a formal request to other collaborators on your project to review the code you've submitted--an important step when working together on the same project.

In a web browser, navigate to the repository page on GitHub (for the repository that you've just submitted new changes for). Towards the upper-left corner you'll see a dropdown that will have `main` selected as default (`main` being one of the branches for your repository, this is the "production-ready" branch). Select your branch from the dropdown, and you may see a yellow box prompting you to create a pull request; click that if you see it, or navigate to `Pull Requests` at the top and subsequently click the green `New pull request` button.

Now, in the top left corner select the branch you wish to add your updated changes to, or the "base" branch--generally speaking this will likely be `main`, the aforementioned "production-ready" branch. In the bar on the righthand side, add Reviewers to the pull request (this should be all of your neighborhood collaborators). Finally, click `Create pull request`.

You'll also be responsible for responding to and reviewing pull requests created by other collaborators on your team. Comment on each other's work about changes you'd like to see made to code submitted, and be sure to keep all communication both specific and professional.

## Merging `traffic-circle` Content on GitHub

After all collaborators have had a chance to weigh in on a new pull request, if the work is up to snuff and ready to join the "production-ready" `main` branch, then your designated neighborhood team lead will have to merge that work into the `main` branch.

If you *are* said team lead, you'll need to navigate to the pull request on GitHub. If there are no "conflicts" (i.e., differences that can't be automatically handled by GitHub) between the pull request's branch and the `main` branch, simply click the `Commit merge` button and the merge is complete!

In some cases however, you'll have to specify what parts of a pull request make it into the `main` branch. If that's the case, you'll instead see a `Resolve conflicts` button. Click that and you'll be presented with a proposed merged copy of the code, with some extra lines added in. Something akin to:

```
<<<<<<
x = "this_is_a_line_of_code"
=======
x = "this_is_a_different_line_of_code"
>>>>>>
```

To resolve said conflicts, you'll need to delete the portion of code you don't want to appear in the final product, as well as any `<<<<<<`, `======`, or `>>>>>>` lines.

Once complete, click `Mark as resolved` followed by `Commit merge`, and the changes on the branch will be joined with the `main` branch!

## Updating `traffic-circle` Content in Your Local Workspace

At some point you may wish to update the content in your local workspace with the changes being implemented by your teammates. 

To do so, `git checkout main` (or other collaborative branch) and run the command:

```
git pull
```

This will update your local workspace with the content stored in the `main` branch.

### `checkout` other folks' branches

It's _very_ likely that you'll run into the need to `checkout` a branch that GitHub has, but you don't. Here's a reminder of the steps to do that.

First, `fetch` all of the changes from the `remote` (GitHub):

```
git fetch --all
```

Once you've received this information, to `checkout` the `east-stoplight` branch (for example):

```
git checkout --track origin/east-stoplight
```

This will copy that branch from GitHub to your local workspace. You'll now also be able to `push` and `pull` to/from it.