# How to Use tmux for Remote & Local Development

> Source: https://deliciousbrains.com/tmux-for-local-development/
> Collected: 2026-11-21
> Published: Unknown

Title: How to Use tmux for Remote & Local&nbsp;Development

URL Source: http://deliciousbrains.com/tmux-for-local-development/

Final URL: https://deliciousbrains.com/tmux-for-local-development/

Published Time: 2022-05-25T11:05:32+00:00

Markdown Content:
![Image 1](https://cdn.deliciousbrains.com/content/uploads/2022/05/24113418/how-i-use-tmux-featured-img.jpg)

The tmux terminal multiplexer is often used in remote development, but it has interesting applications for local dev work as well. In this article, I’ll explain what a terminal multiplexer does, show you how to install tmux, run through the basic commands such as starting a tmux session, and show you how to navigate between windows and panes. Finally, I’ll show you why (and how) I use tmux for local development.

I’ll admit that local development isn’t the most obvious use case for tmux, but I started using it that way in 2016 and fell in love with this super awesome little tool. For me, the best part of using tmux for local dev work is the ability to almost instantly get my preferred command line “workspace” set up as soon as I fire up my terminal emulator.

## [#](https://deliciousbrains.com/tmux-for-local-development/#toc)Table of Contents

1.   [What Is tmux?](https://deliciousbrains.com/tmux-for-local-development/#what-is-tmux)
2.   [How to Install tmux](https://deliciousbrains.com/tmux-for-local-development/#install-tmux)
    1.   [Installing tmux on Linux](https://deliciousbrains.com/tmux-for-local-development/#install-tmux-linux)
    2.   [Installing tmux on macOS](https://deliciousbrains.com/tmux-for-local-development/#install-tmux-mac)
    3.   [Installing tmux on Windows](https://deliciousbrains.com/tmux-for-local-development/#install-tmux-windows)

3.   [How to Use tmux](https://deliciousbrains.com/tmux-for-local-development/#how-to-use-tmux)
    1.   [Command Structure](https://deliciousbrains.com/tmux-for-local-development/#command-structure)
    2.   [Sessions](https://deliciousbrains.com/tmux-for-local-development/#sessions)
    3.   [Attaching and Detaching](https://deliciousbrains.com/tmux-for-local-development/#attaching-detaching)
    4.   [Windows and Panes](https://deliciousbrains.com/tmux-for-local-development/#windows-panes)

4.   [Why Use tmux Locally?](https://deliciousbrains.com/tmux-for-local-development/#why-use-tmux-locally)
5.   [Wrapping Up](https://deliciousbrains.com/tmux-for-local-development/#wrapping-up)

## [#](https://deliciousbrains.com/tmux-for-local-development/#what-is-tmux)What is tmux?

The name “tmux” is a contraction of “terminal multiplexer.” This means you can open multiple split-views (panes) in a single terminal window, and each will function as its own independent terminal. They run visually, right next to each other, eliminating the need to open a new window.

It’s often thought of as a tool you use when working on a remote server, as it saves opening up multiple terminal (SSH) sessions to the machine when you’re trying to do a few things at once.

Maybe you’ve got a script you need to run that takes a while and at the same time you want to monitor its output to a log file with a command like `tail -f`. Perhaps all the while editing some other configuration files or scripts you’re getting ready to run next.

Normally you’d fire up three or more separate instances of your terminal application and SSH into the server with each one. With tmux you only need one SSH connection to the server.

The great thing about tmux is it allows you to have multiple panes open at the same time, each with their own shell running, but using the same, single SSH connection.

![Image 2: tmux with three panes.](https://cdn.deliciousbrains.com/content/uploads/2022/05/17070716/tmux-with-three-panes-1-1540x866.png)

Not only that, you can also have multiple windows open at the same time, a bit like tabs with more panes in them.

![Image 3: tmux with second window.](https://cdn.deliciousbrains.com/content/uploads/2022/05/17070825/tmux-with-second-window-1-1540x866.png)

A huge benefit of using tmux on a remote server is that if your internet connection should die for any reason, that tmux session just keeps on truckin’. Your long-running job that you just kicked off and forgot to [nohup](https://en.wikipedia.org/wiki/Nohup) and background with stream redirection keeps on going too. Just `tmux attach` once your internet is back and you’ve SSH’d into the server again, with all the same panes and windows there waiting for you. You can even detach from your current session, log back in at another computer, and find it’s still running.

## [#](https://deliciousbrains.com/tmux-for-local-development/#install-tmux)How to Install tmux

Installation varies by operating system, but Linux and Mac systems typically only require a single command. Installing it on Windows is slightly trickier, as you have to use the Windows Subsystem for Linux (WSL) feature that premiered in Windows 10.

### [#](https://deliciousbrains.com/tmux-for-local-development/#install-tmux-linux)Installing tmux on Linux

Installing tmux on Linux uses `sudo`, but the following commands differ by distribution:

#### [#](https://deliciousbrains.com/tmux-for-local-development/#ubuntu-debian)Ubuntu/Debian

```
sudo apt-get update
sudo apt-get install tmux
```

#### [#](https://deliciousbrains.com/tmux-for-local-development/#fedora)Fedora

```
sudo dnf -y install tmux
```

#### [#](https://deliciousbrains.com/tmux-for-local-development/#centos)CentOS

```
sudo yum -y install tmux
```

#### [#](https://deliciousbrains.com/tmux-for-local-development/#nix)Nixpkgs or NixOS

If you have Nixpkgs installed on [Linux](https://nixos.org/download.html#nix-install-linux), [macOS](https://nixos.org/download.html#nix-install-macos), or [Windows WSL2](https://nixos.org/download.html#nix-install-windows), you can use the following command:

```
nix-env -iA nixpkgs.tmux
```

For NixOS, you can instead add `programs.tmux` to your `configuration.nix` file, optionally with some changes to the defaults:

```
# tmux
  programs.tmux = {
    enable = true;
    shortcut = "a";
    baseIndex = 1;
    keyMode = "vi";
    secureSocket = false;
    clock24 = true;
  };
```

You can then just `sudo nixos-rebuild switch` to install and configure tmux.

### [#](https://deliciousbrains.com/tmux-for-local-development/#install-tmux-mac)Installing tmux on macOS

The easiest way to do this on a Mac is to use [Homebrew](https://brew.sh/). I highly recommend installing this package manager if you haven’t already. It makes life so much easier.

```
brew install tmux
```

### [#](https://deliciousbrains.com/tmux-for-local-development/#install-tmux-windows)Installing tmux on Windows

To get Windows to run tmux, you’ll need to install WSL and a Linux distro first.

The first step is to install WSL or WSL2, the upgraded version. To install WSL2, you’ll need to be running on Windows 10 version 2004 and higher (Build 19041 and higher) or Windows 11. Older builds of Windows can’t use WSL2, but may be able to [manually install WSL](https://docs.microsoft.com/en-us/windows/wsl/install-manual).

A single command in Windows PowerShell or command prompt will take care of just about everything: enabling required components, downloading the latest Linux kernel, and installing Ubuntu for you:

```
wsl --install
```

You can change the Linux distro that will be installed by using the `-d` flag, followed by the name of the distro. You can see a list of the currently available distributions with this command:

```
wsl --list --online
```

You’ll have to [import the distro manually](https://docs.microsoft.com/en-us/windows/wsl/use-custom-distro) if you want to use one that isn’t listed.

The next step is to create a username and password that you’ll use in Linux. Click your **Start** menu and open your Linux distribution. You may have to search for it.

![Image 4: Finding the new Ubuntu install on Windows. ](https://cdn.deliciousbrains.com/content/uploads/2022/05/11124124/tmux-opening-ubuntu-in-Windows-1.png)

Once it’s finished unpacking the files, Linux will prompt you to enter a username and password. Now that you’ve got a Linux distro up and running, the next step is to update your packages:

```
sudo apt update
sudo apt upgrade
```

Running the following Linux command will install tmux:

```
sudo apt install tmux
```

Congratulations! You have successfully installed tmux on Windows. 😅

## [#](https://deliciousbrains.com/tmux-for-local-development/#how-to-use-tmux)How to Use tmux

To start tmux, open your terminal and let fly with this:

```
tmux
```

You’ll now see a single tmux window with just one pane and a status bar along the bottom. The status bar displays information about the current tmux session, including the name of the current session, the window numbers and the running process in their active pane, which window is active (*), the name of the host, and the time and date.

![Image 5: A screenshot of tmux showing the status bar.](https://cdn.deliciousbrains.com/content/uploads/2022/05/17075221/tmux-with-status-bar-1540x866.png)

As you’ll [see later](https://deliciousbrains.com/tmux-for-local-development/#why-use-tmux-locally), a lot of the default tmux configuration can be changed.

### [#](https://deliciousbrains.com/tmux-for-local-development/#command-structure)Command Structure

Before diving into exactly how to use tmux, let’s take a moment to look at how it structures commands. All tmux commands consist of a prefix followed by a command. The most common prefix you’ll use with tmux is **Ctrl+b**. In all cases, you can press **Ctrl+b** instead of typing `tmux` within a tmux pane.

The default prefix is an awkward combination of keys. A lot of people (including me) configure tmux to use **Ctrl+a** instead. You can do this by adding these lines to your `~/.tmux.conf` file:

```
unbind C-b
set -g prefix C-a
```

From this point forward, we’ll use **Ctrl+a** when referring to the prefix. If you decide not to remap the prefix, make sure to use **Ctrl+b** instead,

### [#](https://deliciousbrains.com/tmux-for-local-development/#sessions)Sessions

Sessions are basic to tmux. Sessions can consist of multiple windows, any of which may have multiple panes. The active window is called a notion.

By starting tmux with the `tmux` command, you are starting a new session. The sessions are numbered by default, starting with `0`. As shown in the [cheat sheet](https://deliciousbrains.com/tmux-for-local-development/#basic-commands-cheat-sheet) below, you can create a named session instead by using the `-s` flag and following it with the session name.

```
tmux new -s [name]
```

You’re not required to give your sessions a name, but the default numbering does make it hard to keep track as your list of tmux sessions grows. You can rename existing tmux sessions using the `rename-session` command and the `-t` flag. That flag tells tmux to `target-session`.

```
tmux rename-session -t [old name or number] [new name]
```

For example, we can use this to rename our first session from `0` to something more descriptive.

![Image 6: Renaming a session in tmux.](https://cdn.deliciousbrains.com/content/uploads/2022/05/17075429/tmux-renaming-session-1540x866.png)

As you can see in the bottom-left, the session has been renamed to `learning`.

Instead of typing out the entire command, like with most commands in tmux you can use a shortcut. In this case **Ctrl+a** and **$** will get you a prompt to rename the session.

You can have multiple sessions running in the same terminal at the same time. The easiest way to create a new session is with the command `tmux new-session`. However, this will create a new session with default numbering. It’s better to use the `-s` flag and give our new session a descriptive name:

```
tmux new -s practice
```

Those sessions will continue to run until you close them with the `kill-session` command. You can see all the running sessions with `tmux ls`.

![Image 7: A view of the sessions in tmux.](https://cdn.deliciousbrains.com/content/uploads/2022/05/17080142/tmux-list-sessions-1540x866.png)

To switch sessions without having to first [detach](https://deliciousbrains.com/tmux-for-local-development/#attaching-detaching), use **Ctrl+a** and **s**, and then select another session with arrow keys and **Enter**. You can also select the required session directly by entering its displayed number.

![Image 8: A view of tmux showing sessions and the number of windows in each session.](https://cdn.deliciousbrains.com/content/uploads/2022/05/17080510/tmux-list-sessions-with-windows-1540x866.png)

### [#](https://deliciousbrains.com/tmux-for-local-development/#attaching-detaching)Attaching and Detaching

You will automatically attach to a new session when you start it. To reattach to an existing session, use the `attach-session` command, followed by the `-t` flag to target a named or numbered session:

```
tmux attach-session -t [session name or number]
```

As a shortcut, you can quickly attach to the last session you were using by not providing the `-t …` flag. In fact, tmux is very good at guessing what command you’d like to do and often the first letter or two of the command will be enough.

```
tmux a
```

To detach from all sessions, use `tmux detach` or press **Ctrl+a** followed by **d**. To detach from just the current session, you’ll have to target that session specifically with the `-s` flag:

```
tmux detach -s [session name or number]
```

Remember, detaching from the session does not stop any running process. Everything will continue to run until you stop the process or kill the session. You can end any active session by pressing **Ctrl+a** and **x**, and then **y**.

To kill all sessions, use the `kill-server` command.

```
tmux kill-server
```

### [#](https://deliciousbrains.com/tmux-for-local-development/#windows-panes)Windows and Panes

Windows and panes are how you use tmux to its full potential. Panes are the part of a window where we run processes, commands, and scripts. So far in this tutorial, we’ve only used one window with a single pane. One of the great things about tmux is that you can run multiple processes at the same time, while keeping an eye on both because they’re in different panes in the same window.

You can split windows into panes either horizontally or vertically. To create two vertical panes, press **Ctrl+a** followed by **%**.

![Image 9: Splitting panes in tmux.](https://cdn.deliciousbrains.com/content/uploads/2022/05/17080913/tmux-first-split-panes-1540x866.png)

You’ll now have a new pane to the right of the first one. You can continue to split panes, either vertically with the command above, or by pressing **Ctrl+a** and **”** to create horizontal panes.

![Image 10: Further pane splitting in tmux, this time splitting the right-hand pane horizontally.](https://cdn.deliciousbrains.com/content/uploads/2022/05/17081132/tmux-with-more-split-panes-1540x866.png)

I created a vertical split followed by a horizontal split, but you can set it up any way you like. By default, tmux activates the cursor in the most recently created pane. Navigate between them with a combination of **Ctrl+a** and your arrow keys. For example, if you want to move to a pane to the right, you would press **Ctrl+a** followed by **→**. To go to the next pane, you can use **Ctrl+a** followed by **o**. Using **Ctrl+a** and **;** instead toggles between the current and previous panes.

You can also navigate by using the pane numbers. Pressing **Ctrl+a** and **q** will very briefly show the pane numbers. Enter the number while it’s still being displayed, and you’ll automatically switch to that pane. This is a good test of your reflexes, but it’s actually one more keystroke than just using your arrow keys.

![Image 11: Three panes in tmux with pane numbers displayed.](https://cdn.deliciousbrains.com/content/uploads/2022/05/17081416/tmux-split-panes-with-numbers-1540x866.png)

Personally, I want even faster pane navigation, so I’ve configured tmux to enable **Alt+arrow-key** for switching panes by adding the following to my `~/.tmux.conf` file.

```
# Use Alt-arrow keys without prefix key to switch panes
bind -n M-Left select-pane -L
bind -n M-Right select-pane -R
bind -n M-Up select-pane -U
bind -n M-Down select-pane -D
```

To close a pane, use the **exit** command or press **Ctrl+d**. Doing this in the last open pane will exit tmux completely.

#### [#](https://deliciousbrains.com/tmux-for-local-development/#resizing-panes)Resizing Panes

You can change the relative size of each pane. Naturally, increasing the size of one pane may cause others to shrink in proportion.

To change pane size, navigate to the correct pane and press **Ctrl+a** followed by **:**. Your status bar will change from green to yellow. You can then use the following commands to change the boundary lines of that pane. Note that you’re limited by the bounds of your terminal. For example, resizing a right-hand pane by moving the boundary line to the right will not work, as there is no space for the pane to expand into.

*   **resize-pane -R:** Expands the pane to the right.
*   **resize-pane -L:** Expands the pane to the left. 
*   **resize-pane -U:** Expands the pane upward.
*   **resize-pane -D:** Expands the pane downward. 

However, as that’s rather slow and laborious, tmux has a few key bindings configured by default for resizing quickly.

*   **Ctrl+a Ctrl+arrow-key:** Grows or shrinks the pane by 1 column or row.
*   **Ctrl+a Alt+arrow-key:** Grows or shrinks the pane by 5 columns or rows.

If you hold down that **Alt** key and mash the arrow key a few times, it’ll keep on resizing the pane without having to hit the **Ctrl+a** prefix again.

#### [#](https://deliciousbrains.com/tmux-for-local-development/#navigating-between-windows)Navigating Between Windows

Use **Ctrl+a** and **c** to create a new window (think tab) in the current session. You will automatically switch to the new window when you create it.

You can navigate to another window by pressing **Ctrl+a** followed by the window’s number as displayed in the status bar, or switch to the next window with **Ctrl+a** and **n**. Entering **Ctrl+a** and **p** will take you back to the previous window.

To quickly toggle back and forwards between two windows, use **Ctrl+a** and **l** (that’s lowercase L, for “last”). You can tell which window is the last one by “-” following its name in the status bar, just like how the current window has “*” after its name.

![Image 12: A view of tmux showing currently selected and previous windows.](https://cdn.deliciousbrains.com/content/uploads/2022/05/17082105/tmux-active-window-selected-1540x866.png)

You may find while using tmux that you need to switch between windows across sessions. You can do this by pressing **Ctrl+a** followed by **w** to display a list of the current windows. It will not display windows for detached sessions. You can select the window you want by scrolling through the list with your arrow keys.

![Image 13: The list of open windows in tmux.](https://cdn.deliciousbrains.com/content/uploads/2022/05/17082321/tmux-show-windows-1540x866.png)

It can get a little confusing seeing a whole bunch of windows with just a number and `: bash` in the status bar. So you can rename the current window with **Ctrl+a** and **,**.

![Image 14: Renaming the active window in tmux.](https://cdn.deliciousbrains.com/content/uploads/2022/05/17082603/tmux-renaming-active-window-1540x866.png)

In the following screenshot you can see the result of naming both windows to reflect the projects they’ll be used for.

![Image 15: tmux showing two renamed windows.](https://cdn.deliciousbrains.com/content/uploads/2022/05/17084328/tmux-after-renaming-windows-1540x866.png)

## [#](https://deliciousbrains.com/tmux-for-local-development/#basic-commands-cheat-sheet)Basic Commands Cheat Sheet

Below you’ll find a cheat sheet with the basic commands you’ll use most often with tmux. To see a complete list of all the keyboard shortcuts in tmux, press **Ctrl+a** followed by **?**.

| Command | Description |
| --- | --- |
| tmux | Starts tmux from the Mac Terminal or Linux. |
| tmux new -s [name] | Starts a new named tmux session. Replace [name] with the name of your session. |
| tmux a # | Attaches to a numbered session. Replace # with the number of your session. |
| tmux a -t [name] | Same as above, but used with named sessions. |
| tmux ls | Shows the complete list of all tmux sessions. |
| tmux kill-session -t [name] | Closes the named session. Note that this is different from detaching from a session. Detaching from a session will leave processes running. |
| exit | Exits tmux without detaching from any sessions. |

## [#](https://deliciousbrains.com/tmux-for-local-development/#why-use-tmux-locally)Why Use tmux Locally?

Using tmux on a remote server means internet connection problems may interrupt your work, but they won’t interrupt the processes you’re running. Given that connection issues can’t stop me using the command line on a machine I’m sitting right in front of, why do I use tmux locally? The biggest advantage is that as soon as I start my terminal emulator, my preferred command line workspace is waiting and ready to go.

Video Player

In the video above, you can see me firing up [Alacritty](https://alacritty.org/) (my terminal emulator), having shown that there was no other terminal emulator open beforehand. I was able to attach to my already running “dev” tmux session, switch to another window, switch to my “dbi” session, and then check on the still running [WP Offload Media](https://deliciousbrains.com/wp-offload-media/) acceptance tests I kicked off earlier. If you look closely you’ll notice windows still there for [WP Offload SES](https://deliciousbrains.com/wp-offload-ses/) development, [WP Migrate](https://deliciousbrains.com/wp-migrate-db-pro/) testing, and working with various storage providers. Everything was just as I left it, even though there was no previously open terminal emulator window.

I have a tmux window for each of the projects I’m currently working on. Each of those windows generally has at least a couple of panes where the current working directory is within the project’s source tree or related folders. I hop between the projects with a quick **Ctrl+a N**, where “N” is the number of the window. So to get to my WP Offload Media stuff I just hit **Ctrl+a 2**.

On my “admin” window I usually have [htop](https://hisham.hm/htop/) open in one pane as it’s handy for quickly seeing what’s hogging my machine’s resources if things start getting slow. Otherwise, the other two panes are generally used for updating my `.dotfiles`, reading [man pages](https://en.wikipedia.org/wiki/Man_page), or general support stuff like `curl -I https://cdn.example.com/some/customers/bucket/object.png`.

Before using tmux, when I still used a Mac, I used [Magnet](https://magnet.crowdcafe.com/) for rearranging terminal windows after [MercuryMover](https://web.archive.org/web/20180427111430/http://www.heliumfoot.com/mercurymover/) went away. It wasn’t ideal for getting things set up nicely. Trying to get to a specific window quickly without having to resort to my trackpad was nearly impossible, and I’ve always struggled to get tiling terminal emulators to work how I like.

The great thing is tmux acts more like a [tiling window manager](https://en.wikipedia.org/wiki/Tiling_window_manager), giving you lots of ways to get to your panes in a window, and rearrange them to suit your workflow. If you’re trying to reduce how much you use a mouse or trackpad, you’ll be very happy.

In fact, after using tmux for just a little while, I started looking at tiling window managers on my Linux machines. I used the excellent [Qtile](http://www.qtile.org/) window manager for quite a while, but these days I tend to use [i3-gaps](https://github.com/Airblader/i3). This led to using a tiling window manager on [macOS](https://github.com/koekeishiya/yabai) too! Eventually though, I couldn’t resist switching to Linux full time, and now I use [NixOS](https://nixos.org/) with the aforementioned [i3wm](https://i3wm.org/) fork for my desktop. So be warned, using tmux day in, day out, could lead you to massively improving your entire desktop experience! 😂

### [#](https://deliciousbrains.com/tmux-for-local-development/#reboot)What Happens When You Reboot?

_“Okay smarty pants, what happens when you reboot your machine and that tmux session dies? Where’s your nice comfortable multi-window workspace now?”_

Let me introduce you to my very favorite tmux plugins, [tmux-resurrect](https://github.com/tmux-plugins/tmux-resurrect) and [tmux-continuum](https://github.com/tmux-plugins/tmux-continuum).

Video Player

In the video, I willfully kill my beloved “dev” and other tmux sessions, create a new session with `tmux new -s dev`, and by pressing **Ctrl+a** and **Ctrl+r**, I resurrect my previous sessions to how they were before I killed the tmux server.

It’s incredibly useful to have all my shell sessions restored with the current working directories as I left them. And as seen in the video, if there was a program running that tmux-resurrect deems safe to restart like `htop` or `vim`, then they come back to life too!

### [#](https://deliciousbrains.com/tmux-for-local-development/#resizing)Resizing and Zooming Panes

Another thing I love about using tmux as my primary means of accessing the command line is its excellent support for resizing. I discussed this briefly while outlining the commands, but it’s worth mentioning again.

![Image 16: tmux resized alongside other windows.](https://cdn.deliciousbrains.com/content/uploads/2022/05/17111640/tmux-resized-alongside-other-windows-1540x866.png)

In the above screenshot my main local terminal window now only takes up half of the screen, there’s two other terminals open in the other half, one logged into a server created with [SpinupWP](https://spinupwp.com/), and the other my ancient iMac.

Even with the bumped up font size I’ve used for your viewing pleasure 😉, tmux has smoothly resized its panes and kept all the ratios intact, and by switching to “horizontal” layout with **Ctrl+a** and **Alt+2**, my super long command prompts aren’t disturbed. 😄

If I want to see more of a pane while still keeping the window a little more cramped than normal, I can zoom the current pane with **Ctrl+a** and **z**.

![Image 17: tmux resized alongside other windows with zoomed pane.](https://cdn.deliciousbrains.com/content/uploads/2022/05/17113019/tmux-resized-alongside-other-windows-with-zoomed-pane-1540x866.png)

I love that feature. It’s great for quickly reviewing log files, etc., with long lines that would normally wrap in a smaller terminal pane.

### [#](https://deliciousbrains.com/tmux-for-local-development/#vim-keys)Vim Key Navigation

I’ve been using [Vi](https://en.wikipedia.org/wiki/Vi) and [Vim](https://www.vim.org/) for over 25 years now, so it’s how my hands do text editing. Apart from using Vim for general text editing, I generally use “vim mode” in everything I can, including in my [IDE](https://www.jetbrains.com/help/phpstorm/using-product-as-the-vim-editor.html) and the [bash command line](https://www.gnu.org/software/bash/manual/bash.html#Readline-vi-Mode).

As such, it’s great that if I want to scroll back up or move around in the output of my current tmux pane, I can simply hit **Ctrl+a** and then use the usual Vim keys for navigation without leaving the keyboard.

## [#](https://deliciousbrains.com/tmux-for-local-development/#wrapping-up)Wrapping Up

Hopefully that’s enough of an overview of why I think tmux is the bee’s knees for not just remote command line work, but also on your local development machine.

If you haven’t tried tmux yet, what are you waiting for?! If you give tmux a go for the first time let us know how you get on in the comments, and if you’re already a daily tmux user why not share your tips in the comments too?
