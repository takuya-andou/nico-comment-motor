# nico-comment-motor
ニコ生のコメントで動くモーター

##用意したもの
- ラズベリーパイ
- モータードライバー(TA7291P)
- モーター
- ブレッドボード
- 単三電池×４


##準備

###配線
下記のURLの図にあるとおりに配線しました。  
http://www.hiramine.com/physicalcomputing/raspberrypi/webiopi_motordriver.html

###WebIOPiのインストール
Raspberry Pi 2の場合はエラーが出るようなので、下記のURLを参考にした  
http://denshikousaku.net/control-servos-on-raspberry-pi-part3-for-pi2

```
wget http://sourceforge.net/projects/webiopi/files/WebIOPi-0.7.1.tar.gz/download
tar xvzf download
cd WebIOPi-0.7.1/python/native

mv cpuinfo.c cpuinfo.c.original
mv gpio.c gpio.c.original

wget http://denshikousaku.net/wp-content/uploads/2015/02/cpuinfo.c
wget http://denshikousaku.net/wp-content/uploads/2015/02/gpio.c

cd ../..
sudo ./setup.sh
```

###ニコ生のコメントを受信する準備
falseberryさんが作成された000000_nicomment.jarをダウンロード  
http://falseberry.dip.jp/uploaded/  

##使い方
1. 000000_nicomment.jar　をPCで起動して
2. Raspberry Pi上でmysocket.pyを実行
