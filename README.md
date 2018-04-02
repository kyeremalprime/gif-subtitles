![csgo](https://github.com/kyeremalprime/gif-subtitles/blob/master/cache/6613d4e20309b780d465b38594ed07a3.gif)

## 目录结构
```
├── README.md
├── source.mp4              # 原视频(无声音)
├── templates               # web.py 模板文件目录
    ├── sorry.html          # html 模板
    ├── sorry.png           # html 中的图片
├── cache                   # 字幕和 gif 文件目录
    ├── *.ass               # 字幕文件
    ├── *.gif               # gif 文件
├── index.py                # web.py 入口及请求处理
├── utils.py                # 函数
├── delete.py               # 定时删除缓存脚本
└── config.py               # 配置文件
```
## 功能
生成自定义字幕的 gif   
sorry gif 大小为 546*300, 每秒帧数 8 (可在 config.py 中修改)  
demo: [http://demo.zzh.sb/](http://demo.zzh.sb/)

## 部署
支持版本: python3.4.* - python3.6.*   

### web.py
```
pip3 install web.py==0.40.dev0
```

### uWSGI
```
pip3 install uWSGI
```

### FFmpeg
```
# for ubuntu
sudo add-apt-repository ppa:kirillshkrogalev/ffmpeg-next 
sudo apt-get update 
sudo apt-get install ffmpeg
```
或编译源码, 参考 FFmpeg 官网: [https://trac.ffmpeg.org/wiki/CompilationGuide](https://trac.ffmpeg.org/wiki/CompilationGuide)   
需要有 libass 支持, 即编译 configure 需加上 --enable-libass

### 启动
```
cd [dir]
uwsgi -s 127.0.0.1:9001 -w index
```

### 定时删除
每 1 小时删除 cache/ 目录下 5 小时前的 .ass .gif 文件


```
crontab -e
0 */1 * * * /usr/bin/python3 /var/www/python/delete.py
```

## todolist

- [ ] 多线程
- [ ] 优化代码
- [ ] 优化代码结构
- [ ] 设计网页页面
- [*] 提供 API
- [ ] 用户可以设置 gif 大小及 fps
- [*] 配置更多 gif 模板
- [ ] 用户可以配置 gif 模板
