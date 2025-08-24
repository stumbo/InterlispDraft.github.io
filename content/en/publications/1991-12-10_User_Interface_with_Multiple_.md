---
title: "User Interface with Multiple Workspaces for Sharing Display System Objects"
date: '1991-12-10'
authors: 
    - D. Austin Henderson
    - Stuart K. Card
    - John T. Maxwell
abstract: "Workspaces provided by an object-based user interface appear to share windows and other display objects. Each workspace's data structure includes, for each window in that workspace, a linking data structure called a placement which links to the display system object which provides that window, which may be a display system object in a preexisting window system. The placement also contains display characteristics of the window when displayed in that workspace, such as position and size. Therefore, a display system object can be linked to several workspaces by a placement in each of the workspaces' data structures, and the window it provides to each of those workspaces can have unique display characteristics, yet appear to the user to be the same window or versions of the same window. As a result, the workspaces appear to be sharing a window. Workspaces can also appear to share a window if each workspace's data structure includes data linking to another workspace with a placement to the shared window. The user can invoke a switch between workspaces by selecting a display object called a door, and a back door to the previous workspace is created automatically so that the user is not trapped in a workspace. A display system object providing a window to a workspace being left remains active so that when that workspace is reentered, the window will have the same contents as when it disappeared. Also, the placements of a workspace are updated so that when the workspace is reentered its windows are organized the same as when the user left that workspace. The user can enter an overview display which shows a representation of each workspace and the windows it contains so that the user can navigate to any workspace from the overview."
---

