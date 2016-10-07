# Team Practices

This page is meant to describe the team practices that the FFD-Info-Exchange team will use.

It is a living document that will be amended as the team learns what works sprint by sprint.

Many of these practices come from agile development processes; with no specific framework being adopted.

# Team Cadence
Sprints will be used to time box our work.  
Sprints will be two weeks long.  
Sprints will start with sprint planning, and end with a demo and retrospective.

## Sprint Planning
At the beginning of a sprint a prioritized list of activities will be present on the team taskboard.
This meeting will be used to review those stories where we will:
* Gain a common understanding of what the stories entail
* Ensure the team is in a position to execute the story (any dependencies)
* Commit to which stories the team will complete for that given sprint

### Estimation
Storypointing in agile is used in conjunction with velocity to project how much a team can commit to.  However, given our team is nascent in nature, establishing the velocity is a second priority.
Estimation ensures that as we discuss stories, there is a common understanding as to what it entails.  Disconnects and following alignment is met by initial estimates from team members being quite different and the ensuing discusion.
Further, pointing gives a common baseline which can drive whether a story should be broken down further into smaller chunks.

There are at least 2 trains of thought in terms of units of measure for storypoint: complexity vs. effort (time).  
The difference between the two is described through the example of tasks that are great candidates for automation.  Those tasks often carry high effort estimates, but very low complexity estimates.
Given the forming nature of the team, we will use **effort estimates**.

**Estimation Points**

We will use estimation points that are part of the Fibonacci sequence (1,2,3,5,8).  Where each point is roughly 1 day of effort.  So if a story is expected to take 2 days its 2 points.  If you expect 4 days... need to select between 3 or 5! 

However in general, stories that initially get a 5 or 8 estimate should be considered to be broken down further.

At times discussion on a particular story can extend for quite a bit of time leading to a bulk of the time spent on one story.
The moderator will be tasked on preventing this from occurring.  Some techniques are (but are not limiteed to):
- Opt to timebox the card
- Focus on getting a consistent estimate amongst the team, implementation detail can be discussed in a kick-off
- Decide that too many dependencies/unknowns are present and move the story to the next sprint.

## Daily Standups
On days without planning or demos, the team will have a standup.  This meeting will be at most 15 minutes in length via a video call.
Each member will provide an update on what they completed yesterday, plan for today, and highlight any blockers.

The meeting will be from 4:30 - 4:45 EST.

If a team member is unable to attend the meeting, please post a slackup in the #ffd-info-sharing channel with your update for the day.

## Sprint Demos
Sprint demos will be an opportunity for the team to showcase the hard work that has been completed during the sprint.
This will be held via a video conference where members of the team can screen share the work they completed.
Sprint demos will be open to folks outside team; particularly the potential partner agency POCs.  Sprint demos will be also open to anyone within 18F.

## Retrospectives
Retros are a forum private to the team where we will review what went well, and what did not.
This will be a 30 minute meeting, and will be private to our team.  On request it can also be facilitated with the product owners and product steward not in attendance.
Will be split up into the following:

1 minute : Vote from 1-5 on how the sprint went (1 --> Poor, 5--> Excellent)

4 minutes : team will post in mural.ly stickies that represent:
- What went well
- What did not go well

5 min : moderator will group stickies together prior to team discussion

10 - 15 min : open discussion on stickies

5-10 min : team votes on **up to two** items to focus on for the next iteration.  There will be a lot of improvement opportunities we will not get to; but if they continue to be important to the team they will come up again in subsequent retros and get voted in.

# Team Taskboard - [Zenhub](https://github.com/18F/ffd-info-exchange/projects#boards?repos=69997339)
Zenhub is an extension that enables GitHub issues to be presented as a taskboard.  Zenhub is available on Chrome or Firefox. You can download the extension [here](https://www.zenhub.com)

Note that Zenhub is free for `public` GitHub repos and we currently have temporary authorization to use the tool.

Once installed GitHub Will have a `Boards` menu item next to `Pull Requests` from which you will be able to view the board.

## Taskboard Columns

Following is a description of each Zenhub column.

**TL:DR;** Unless you are the product owner or product steward for the project, you will be mostly concerned with the `Ready`, `In Process`, `Done` columns. 

**`New Issues`**

By default, GitHub issues get placed in this column when first created.  The product owner or product steward will then place them in the `Backlog` column.

**`Backlog`**

This column is a _somewhat_ ordered list of issues to be worked on.  Somewhat because as the list grows, what is most essential is the issues that would be worked on in the next sprint or two are ordered at the top of the list.  The product owner or product steward are responsible for keeping the list ordered.

**`Ready`**

During sprint planning the highest priority backlog items will be discussed and those the team will commit to doing during the sprint will be placed in the `Ready` column.

**`In Process`**

Over the course of the sprint as team members pick up stories, they are then placed `In Process` so that the team has an understanding of what is currently being worked on.

**`Done`**

As stories are completed, they are then placed into the `Done` column and the team member then picks up a new story from the `Ready` column.

**`Closed`**

At the end of the sprint, we will demo all stories in the `Done` column.  As a team we will assess whether we hit the goals of that story; and if so will `Close` the issue.  If not, then the story will be put back at the top of the `Backlog` to see if we continue the work in the next sprint or cut our losses.

## Slack
Given our distributed model, slack will be used for async comms.  The following are channels of note:
- #ffd-info-sharing

# Additional Principles

## Coding & Branchin Standards
TBD (GitFlow?)