# Boring-Tools
这里的小工具都是我花一天时间写好，来替代一个小时可以完成的重复操作的。(笑)
<br/><br/>  

## 海外下载网易云的歌单  

在国内一直用网易云在线听音乐，从来没把音乐保存到本地。到德国发现网易云音乐好多歌没版权，听不了。YouTube资源特丰富，而且有大佬专门写的下载工具 `yt_dlp` ,于是我捣鼓了一下把网易云音乐的歌单通过脚本从YouTube下载到了本地，

首先，先到网易云音乐的网页版登陆自己的账号，并点开`我的音乐`。然后 `Ctrl+Shift+J` 打开浏览器的Console，输入以下程序。

```javascript
list = window.frames[0].document.querySelector(".m-table").querySelectorAll("tr");
for (let i = 1;i<list.length;i++){console.log(list[i].querySelector("b").title)}
```
打开文件夹`/NE2YT2LC`，复制Console打印出来的歌单保存至 `pt.txt`, 然后打开 `powershell`进入目录`/NE2YT2LC`下，使用如下命令运行Python脚本。
```powershell
python ytdl.py
```
然后等待一会，歌曲会自动下载到`/songs`文件夹内。


## yt-dlp使用

```powershell
yt-dlp -i --format bestaudio --extract-audio --audio-format mp3 --output "%(title)s.%(ext)s" --yes-playlist [index] 
```

index可以从视频的url里获取，(`watch?v=`后跟视频代号，`&list=`后跟歌单代号)。<br/>

`--yes-playlist`为可选项，加上可下载整个歌单。
