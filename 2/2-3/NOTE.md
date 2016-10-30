ffmpegが入っていないとaviファイルも開けないっぽい？
http://stackoverflow.com/questions/13112168/opencv-fails-to-read-avi-file

`--with-ffmpeg`フラグをつけて再インストール
```shell
brew install ffmpeg
brew install --HEAD opencv --with-ffmpeg

//リンクのエラーが出たので
brew link --overwrite opencv
```

その結果、無事表示された。
