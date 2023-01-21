# lt-chill

Twitter APIからデータを取得して、khcoderで分析してみる遊び

# X-WIndowsの起動

khcodernを動かすのに必要

公式サイトからインストールし、起動すればok
'''
https://sourceforge.net/projects/vcxsrv/
'''

# perlの必要モジュールインストール

perlは標準で入ってるはずなのでモジュールのみインストール
'''
perl -MCPAN -e shell

install Jcode*
install Tk*
install DBI
install DBD::CSV
install File::BOM*
sudo install Lingua::JA::Regular::Unicode
install Net::Telnet
install Excel::Writer::XLSX
install DBD::mysql
install Spreadsheet::ParseExcel::FmtJapan
install Spreadsheet::ParseXLSX
install Statistics::ChisqIndep*
install Statistics::Lite*
install Unicode::Escape*
install Algorithm::NaiveBayes*
install Lingua::Sentence*
install Proc::Background
'''

# Rのインストール
'''
sudo apt install r-base

R

install.packages("ade4", dependencies=TRUE)
install.packages("amap", dependencies=TRUE)
install.packages("Cairo", dependencies=TRUE)
install.packages("cluster", dependencies=TRUE)
install.packages("codetools", dependencies=TRUE)
install.packages("colorspace", dependencies=TRUE)
install.packages("dichromat", dependencies=TRUE)
install.packages("foreign", dependencies=TRUE)
install.packages("ggdendro", dependencies=TRUE)
install.packages("ggplot2", dependencies=TRUE)
install.packages("ggnetwork", dependencies=TRUE)
install.packages("ggsci", dependencies=TRUE)
install.packages("gtable", dependencies=TRUE)
install.packages("igraph", dependencies=TRUE)
install.packages("KernSmooth", dependencies=TRUE)
install.packages("lattice", dependencies=TRUE)
install.packages("maptools", dependencies=TRUE)
install.packages("MASS", dependencies=TRUE)
install.packages("Matrix", dependencies=TRUE)
install.packages("mgcv", dependencies=TRUE)
install.packages("munsell", dependencies=TRUE)
install.packages("nlme", dependencies=TRUE)
install.packages("nnet", dependencies=TRUE)
install.packages("permute", dependencies=TRUE)
install.packages("pheatmap", dependencies=TRUE)
install.packages("plyr", dependencies=TRUE)
install.packages("proto", dependencies=TRUE)
install.packages("RcolorBrewer", dependencies=TRUE)
install.packages("Rcpp", dependencies=TRUE)
install.packages("reshape2", dependencies=TRUE)
install.packages("rgl", dependencies=TRUE)
install.packages("rpart", dependencies=TRUE)
install.packages("scales", dependencies=TRUE)
install.packages("scatterplot3d", dependencies=TRUE)
install.packages("slam", dependencies=TRUE)
install.packages("som", dependencies=TRUE)
install.packages("sp", dependencies=TRUE)
install.packages("spatial", dependencies=TRUE)
install.packages("stringr", dependencies=TRUE)
install.packages("survival", dependencies=TRUE)
install.packages("vegan", dependencies=TRUE)
install.packages("wordcloud", dependencies=TRUE)
'''

# Mecabのインストール

公式サイトからインストール
'''
http://taku910.github.io/mecab/#download

tar zxvf mecab-0.996.tar.gz
cd mecab-0.996/
./configure --with-charset=utf8
sudo make install
'''

# Mecab辞書のインストール
'''
git clone https://github.com/neologd/mecab-ipadic-neologd.git
cd mecab-ipadic-neologd
./bin/install-mecab-ipadic-neologd -n
'''

# KHcoderの設定

perl kh_coder.plで初回実行するとconfig/coder.iniが作成される。
'''
sql_username    ユーザ名
sql_password    パスワード
'''
