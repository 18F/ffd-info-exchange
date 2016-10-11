# Team practices

This page is meant to describe the team practices that the FFD-Info-Exchange team will use.

It is a living document that anyone on the team can amend as we learn, sprint by sprint, what works best for us.

Many of these practices come from agile development processes and aren't framework specific. 

# Team cadence
Sprints will time box our work.  
Sprints will be two weeks long.  
Sprints will start with sprint planning and end with a demo and retrospective.

## Sprint planning
At the beginning of a sprint a prioritized list of activities will be present on the team taskboard.
We'll use this meeting to review those stories with the goals of:
* Gaining a common understanding of what the stories entail
* Ensuring the team is in a position to execute the stories (identifying any dependencies)
* Committing to which stories the team will complete for that given sprint

### Estimation
In agile, teams use storypointing (in conjunction with velocity) to project how much they can commit to. However, because our team is nascent, establishing the velocity is a second priority.

Estimation ensures that, as we discuss stories, we'll develop a common understanding as to what those stories entail. Different initial estimates from team members — and the ensuing discussion — may yield disconnects followed by alignment. Further, pointing gives a common baseline that can drive whether a story should be broken down further into smaller chunks.

There are at least two trains of thought in terms of units of measure for storypoint: complexity vs. effort (time).  
The difference between the two is described through the example of tasks that are great candidates for automation. Those tasks often carry high effort estimates but very low complexity estimates.
Given the forming nature of the team, we will use **effort estimates**.

**Estimation points**

We will use estimation points that are part of the Fibonacci sequence (1, 2, 3, 5, 8), where each point represents roughly one day of effort. So if a story is expected to take two days to complete, it will carry a value of two points. If you expect a story to take four days to complete, you'll need to select a point value of three or five! 

However, in general, stories that initially get an estimate of five or eight should be broken down further.

At times, discussion on a particular story may extend for quite a bit of time, leading to the bulk of the team's time being spent on that story.
The moderator is responsible for preventing this from occurring. Some techniques for preventing this include (but aren't limited to):
- Opting to timebox the card
- Focusing on getting a consistent estimate amongst the team (implementation detail can be discussed in a kick-off)
- Deciding that too many dependencies/unknowns are present and moving the story to the next sprint.

## Daily standups
On days without planning or demos, the team will have a standup. This meeting will be at most 15 minutes in length and will take place via a video call.

Each team member will provide an update on what they completed yesterday and what they're planning for today, and will highlight any blockers.

The standup will be from 4:30 - 4:45 EST.

If a team member is unable to attend the meeting, they should post a slackup in the #ffd-info-sharing channel with their update for the day.

## Sprint demos
Sprint demos are an opportunity for the team to showcase the hard work they've completed during the sprint.
Demos will be held via video conference where members of the team can screen share the work they completed.
Sprint demos will be open to folks outside the team, particularly the potential partner agency POCs. Sprint demos will be also open to anyone within 18F.

## Retrospectives
Retros are a forum private to the team where we will review what went well and what didn't.
Retros will be 30 minutes in length and private to our team. On request, we can also include product owners and product stewards who aren't normally in attendance.
Here's the time breakdown for each retro:

1 minute : Vote from 1-5 on how the sprint went (1 --> Poor, 5--> Excellent)

4 minutes : team will post in mural.ly stickies that represent:
- What went well
- What did not go well

5 min : moderator will group stickies together prior to team discussion

10 - 15 min : open discussion on stickies

5-10 min : team votes on **up to two** items to focus on for the next iteration.  There will be a lot of improvement opportunities we will not get to, but if they continue to be important to the team they will come up again in subsequent retros and get voted in.

# Team taskboard - [Zenhub](https://github.com/18F/ffd-info-exchange/projects#boards?repos=69997339)
Zenhub is an extension that enables GitHub issues to be presented as a taskboard. Zenhub is available on Chrome or Firefox. You can download the extension [here](https://www.zenhub.com)

Note that Zenhub is free for `public` GitHub repos and we currently have temporary authorization to use the tool.

Once installed, GitHub will have a `Boards` menu item next to `Pull Requests` from which you will be able to view the board.

## Taskboard columns

Following is a description of each Zenhub column.

**TL:DR;** Unless you are the product owner or product steward for the project, you will be mostly concerned with the `Ready`, `In Process`, `Done` columns. 

**`New Issues`**

By default, GitHub issues get placed in this column when they're first created. The product owner or product steward will then place them in the `Backlog` column.

**`Backlog`**

This column is a _somewhat_ ordered list of issues to be worked on. Somewhat because as the list grows, the tasks that need to be worked on in the next sprint or two occupy the spots at the top of the list, and lower-priority tasks are farther down. The product owner or product steward is responsible for keeping the list ordered.

**`Ready`**

During sprint planning, the team will discuss the highest-priority backlog items, and those the team will commit to doing during the sprint will be placed in the `Ready` column.

**`In Process`**

Over the course of the sprint, as team members pick up stories, those items will appear in the `In Process` column. This will give the team an understanding of what's currently being worked on.

**`Done`**

As stories are completed, they're placed in the `Done` column. When a team member finishes a story, they can select a new one from the `Ready` column.

**`Closed`**

At the end of the sprint, we will demo all stories in the `Done` column.  As a team, we will assess whether we hit the goals of that story; if so, we will `Close` the issue.  If not, then the story will be put back at the top of the `Backlog` to see if we continue the work in the next sprint or cut our losses.

## Slack
Given our distributed model, slack will be used for async comms. The following are channels of note:
- #ffd-info-sharing

# Additional principles

## Coding & Branching Standards
TBD (GitFlow?)
