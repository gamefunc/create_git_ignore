# create_git_ignore

常常写代码顺便编译都在同一个目录,
直接git init; git add --all; git commit -m "提交更新",
久而久之git目录几G大小,因为他连你的exe等文件更改都commit到git了;

但我们只需要git记录代码修改,比如.c, .txt, .cpp之类才记录,其他不记录;
那添加.gitignore即可;

由于我只写c/cpp/py/java/js/html/, accept_extensions列表基本齐全;
如果其他语言,需要自行添加到accept_extensions列表;

如果想忽略掉某些目录, 看priority_lines列表的例子, 该例子是android studio的;

如果某些后缀名你也想记录, 修改ignore_extensions列表即可;

更直接的方法是跑完出了.gitignore后,自己修改.gitignore就行;
