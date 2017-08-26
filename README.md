# ehdataset

An e-hentai dataset and a simple recommendation algorithm.

Raw data comes from [E-HentaiCrawler](https://github.com/shuiqukeyou/E-HentaiCrawler).

The maximum gid is 1020617 at 2017/1/21 16:07:18.

The raw data is converted to `list` of Python and saved by `pickle` module.


## Usage

```
import pickle
with open("ehdataset",'rb') as file:
    dataset = pickle.load(file)
```
### The structure of dataset:

List of dataset is consisted of dict.

A sample:

```
  {
     "gid": 618395,
     "token": "0439fa3666",
     "title": "(Kouroumu 8) [Handful☆Happiness! (Fuyuki Nanahara)] TOUHOU GUNMANIA A2 (Touhou Project)",
     "title_jpn": "(紅楼夢8) [Handful☆Happiness! (七原冬雪)] TOUHOU GUNMANIA A2 (東方Project)",
     "category": "Non-H",//10 Categories of e-hentai
     "thumb":"https://ehgt.org/14/63/1463dfbc16847c9ebef92c46a90e21ca881b2a12-1729712-4271-6032-jpg_l.jpg"//Url of thumbnails
     "uploader": "avexotsukaai",
     "posted": "1376143500",//Unix timestamp of upload
     "filecount": "20",//pages number
     "filesize": 51210504,//File size
     "expunged": false,
     "rating": "4.43"，
     "torrentcount": "0",
     'Favorited': 103,//Favorite Number
     "tags": [
       "parody:touhou project",
       "group:handful happiness",
       "artist:nanahara fuyuki",
       "full color",
       "artbook",
       "male:xxxxx",
       "female:xxxxx"
        ]
   }

```

## Recommendation algorithm

Using each tag as a dimension of vector, compute the cosine of the angle between two vectors as their degree of similarity.

Inputing a gid, the algorithm will return the highest similarity 20 works.

### Usage
```
$python3 recommendation.py
Loading...
Please enter gid:
627651
[クラスメイトショック(三上小又 弘崎真史)]破顔一笑(らき☆すた) (中文)    gid:627648    like:8    rate:4.28
[クラスメイトショック(三上小又 弘崎真史)]破顔二笑(らき☆すた) (中文)    gid:627651    like:6    rate:4.36
Classmate Shock 1, 2, and 3 [Eng]    gid:189174    like:60    rate:4.77
(三上小又)[クラスメイトショック]破顔四笑(らき☆すた)    gid:598282    like:4    rate:3.56
[三上小又] クラスメイトショック 破顔四笑 (らき☆すた) [英訳]    gid:632989    like:39    rate:4.78
(C73) [しもやけ堂 (逢魔刻壱)] CICADA DRIZZLE (らき☆すた) [中国翻訳]    gid:55073    like:20    rate:4.09
(C73) [しもやけ堂 (逢魔刻壱)] CICADA DRIZZLE (らき☆すた) [中国翻訳]    gid:371302    like:27    rate:4.53
(C72) [うろぴょん☆ (うろたん)] クリームコロネ症候群 (らき☆すた) [中国翻訳]    gid:304405    like:36    rate:3.88
幸運星 歡樂漫畫吧～Lucky Spiral～ COMPTIQ編 中文版    gid:248131    like:3    rate:4.8
[Nijigen☆Goten] Erotic☆Star    gid:82902    like:2    rate:2.63
(C72) [MGW (位相同爆)] レアステ (らき☆すた) [英訳]    gid:71273    like:42    rate:4.25
(C72) [MGW (位相同爆)] レアステ (らき☆すた) [ポルトガル翻訳]    gid:99394    like:2    rate:3.3
(サンクリ39) [東ガル会 (快楽園梅香)] LUCKY POINT WINTER (らき☆すた) [英訳]    gid:240981    like:23    rate:4.54
(C72) [偽MIDI泥の会 (石恵)] HiGiiRa (らき☆すた) [中国翻訳]    gid:336135    like:117    rate:4.79
(サンクリ35) [3 colors cat (みけ田みい吉)] KIRARAKI (らき☆すた) [中国翻訳]    gid:336793    like:13    rate:4.5
(サンクリ36) [東ガル会 (快楽園梅香)] LUCKY POINT (らき☆すた) [英訳]    gid:1006962    like:18    rate:4.41
(C76) (同人誌) [メカニカルペンシル] かが·ほん (らき☆すた) (CN)    gid:148260    like:12    rate:4.69
7 horas de momentos rosas con konata en el karaoke (Lucky Star Spanish)    gid:170835    like:12    rate:4.64
Lucky Star H Girls Collection    gid:198585    like:8    rate:3.63
Brillian Star(mori kohichiroh &amp; sakura akami) eng    gid:240997    like:10    rate:4.39
Please enter gid:

```