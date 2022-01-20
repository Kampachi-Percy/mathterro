---
layout: default
parent: sandbox
summary: 
---

# 漸化式 解説編 <!-- omit in toc -->

いろいろな漸化式の解き方をまとめます。問題編も併せて参考にしてください。

- [概要](#概要)
- [最終目標](#最終目標)
- [かんたん](#かんたん)
    - [調和数列型](#調和数列型)
    - [特殊解型](#特殊解型)
    - [n 次式型](#n-次式型)
    - [指数型](#指数型)
    - [階比数列型](#階比数列型)
    - [対数型](#対数型)
    - [簡易分数型](#簡易分数型)
- [むずかしい](#むずかしい)
    - [和 Sn 型](#和-sn-型)
    - [f(n)f(n+1) で割る型](#fnfn1-で割る型)
    - [1 次分数型](#1-次分数型)
    - [隣接 3 項間型](#隣接-3-項間型)
    - [連立漸化式](#連立漸化式)

## 概要

- 解ける漸化式しか出ない
- 等差型・等比型(特殊解型)・階差型のいずれかに帰着する
- どうしても無理なら、一般項を予想して数学的帰納法で証明する
- 必ず $n=1$ で検算する

## 最終目標

等差型・等比型・階差型のいずれかに帰着させる。

- 等差型 $a_{n+1}-a_n = d$
- 等比型 $a_{n+1} = ra_n$
- 階差型 $a_{n+1}-a_n = f(n)$

どうしても無理そうなら、$a_1, a_2, a_3, \cdots$ を列挙して、一般項を予想する。うまく予想できれば、数学的帰納法で証明することができる。

## かんたん

### 調和数列型

$$\frac{1}{a_{n+1}} - \frac{1}{a_n} = d$$

逆数が等差数列になる数列を調和数列という。$b_n = \dfrac{1}{a_n}$ とおくと $b_{n+1} - b_n = d$ となって等差型になる。

$$a_{n+1}a_n + pa_{n+1} - pa_n = 0$$

見た目は全然違うが、**$a_n \neq 0$ を確認したあと**、両辺を $a_{n+1}a_n$ で割ると調和数列になる。

### 特殊解型

$$ a_{n+1} = pa_n + q $$

漸化式で最も重要な型。頑張って変形するとだいたい特殊解型になる。

特性方程式 $\alpha = p\alpha + q$ を解いて、辺々を引くと、等比型になる。

$$
\begin{align}
a_{n+1} &= pa_n + q \newline
-) \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \alpha &= p\alpha + q\newline
\underline{a_{n+1} - \alpha} &= p(\underline{a_n - \alpha})
\end{align}
$$

$\lbrace a_n - \alpha\rbrace$ は、初項 $a_1-\alpha$ 、公比 $p$ の等比数列である。

ちなみに、「特性方程式」と仰々しい名前がついているが、ただの便宜的な呼び名であり、深い意味はない。[^1]

### n 次式型

$$ a_{n+1} = pa_n + f(n) $$

等比型の目標の式を先に書き、元の漸化式と係数比較する。ここでは $f(n)$ が $1$ 次式の場合と $2$ 次式の場合を説明する。

まず、$f(n)$ が $1$ 次式の場合、目標の式は以下のようになる。

$$ \underline{a_{n+1}+\alpha(n+1)+\beta} = p(\underline{a_n+\alpha n+\beta}) $$

下線部が左辺 $n+1$ 右辺 $n$ でまとまっていることを確認してほしい。この式を整理して、

$$ a_{n+1} = pa_n + \underline{(p\alpha-\alpha) n + (p\beta -\alpha -\beta)} $$

下線部が $1$ 次式になっているので、$f(n)$ と係数比較して $\alpha$, $\beta$ を求める。

次に、$f(n)$ が $2$ 次式の場合、目標の式は以下のようになる。

$$ \underline{a_{n+1}+\alpha(n+1)^2+\beta(n+1)+\gamma}=p(\underline{a_n+\alpha n^2+\beta n+\gamma}) $$

下線部が左辺 $n+1$ 右辺 $n$ でまとまっていることを確認してほしい。$1$ 次式の解き方と同じく、整理して $f(n)$ と係数比較すると $\alpha$, $\beta$, $\gamma$ が求まる。

### 指数型

$$ a_{n+1} = pa_n + r^n $$

両辺を $r^{n+1}$ で割ると、

$$ \frac{a_{n+1}}{r^{n+1}} = \frac{p}{r} \cdot \frac{a_n}{r^n} + \frac{1}{r} $$

となり、$b_n = \dfrac{a_n}{r^n}$ とおくと特殊解型になる。

### 階比数列型

$$ a_{n+1} = f(n)a_n $$ 

$n \geqq 2$ のとき、$a_{n+1}=f(n)a_n$ より $a_n=f(n-1)a_{n-1}$ だから、右辺が $a_1$ になるまで繰り返す。

$$
\begin{align}
a_n &= f(n-1)a_{n-1} \newline
&= f(n-1)f(n-2)a_{n-2} \newline
&= f(n-1)f(n-2)f(n-3)a_{n-3} \newline
&= \cdots \newline
&= f(n-1)f(n-2)f(n-3) \cdots f(2)f(1)a_1
\end{align}
$$

### 対数型

$$ a_{n+1}a_n = {a_n}^p $$

積 $a_{n+1}a_n$ や累乗 ${a_n}^p$ を含む数列は、**両辺が正であることを確認してから**、両辺の対数をとる。

$$ \log a_{n+1}a_n = \log {a_n}^p $$

対数の計算規則を思い出して、

$$ \log a_{n+1} + \log a_n = p \log a_n $$

$b_n = \log a_n$ とおくと等比型になる。

### 簡易分数型

$$ a_{n+1} = \frac{pa_n}{qa_n+r} $$

**$a_n \neq 0$ を確認したあと**、両辺の逆数をとって分解する。

$$ \frac{1}{a_{n+1}} = \frac{qa_n+r}{pa_n} = \frac{r}{p} \cdot \frac{1}{a_n} +\frac{q}{p} $$

$b_n = \dfrac{1}{a_n}$ とおくと特殊解型になる。



## むずかしい


### 和 Sn 型

$a_1 = S_1$ から初項を求めたあと、和と一般項の関係 $a_{n+1} = S_{n+1} - S_n$ を用いて $S_n$ を消去する。

### f(n)f(n+1) で割る型

$$ f(n)a_{n+1} = f(n+1)a_n + g(n) $$

うまく両辺を割ると、階差数列型にできることがある。いい感じの $f(n)$ を見つけるのが難しい。

どうにかして $f(n)$ を見つけたら、両辺を $f(n)f(n+1)$ で割ると特殊解型になる。

$$ \frac{a_{n+1}}{f(n+1)} = \frac{a_n}{f(n)} + \frac{g(n)}{f(n)f(n+1)} $$


### 1 次分数型

$$ a_{n+1} = \frac{pa_n+q}{ra_n+s} $$

まず、特性方程式 $\alpha = \dfrac{p\alpha+q}{r\alpha+s}$ を解き、$\alpha$ を求める。

<details markdown="1">
<summary>なぜ？</summary>

どうにかして等比型

$$ \frac{a_{n+1}-\alpha_1}{a_{n+1}-\alpha_2} = R \cdot \frac{a_n - \alpha_1}{a_n - \alpha_2} $$

となるように変形したい。

$$ \begin{align}
\frac{a_{n+1}-\alpha_1}{a_{n+1}-\alpha_2} &= \frac{\dfrac{pa_n+q}{ra_n+s}-\alpha_1}{\dfrac{pa_n+q}{ra_n+s}-\alpha_2} \newline
&= \frac{pa_n+q-\alpha_1(ra_n+s)}{pa_n+q-\alpha_2(ra_n+s)} \newline
&= \frac{(p-r\alpha_1)a_n+q-s\alpha_1}{(p-r\alpha_2)a_n+q-s\alpha_2} \newline
&= \frac{\dfrac{p-r\alpha_1}{p-r\alpha_2}a_n+\dfrac{q-s\alpha_1}{p-r\alpha_2}}{a_n+\dfrac{q-s\alpha_2}{p-r\alpha_2}} \newline
\end{align} $$

係数を比較して

$$ R = \frac{p-r\alpha_1}{p-r\alpha_2},\ -R\alpha_1 = \frac{q-s\alpha_1}{p-r\alpha_2},\ \alpha_2 = \frac{q-s\alpha_2}{p-r\alpha_2} $$

$R$ を消去して整理すると

$$ \alpha_1 = \frac{p\alpha_1+q}{r\alpha_1+s},\ \alpha_2 = \frac{p\alpha_2+q}{r\alpha_2+s} $$

つまり、$\alpha_1$ と $\alpha_2$ は

$$ \alpha = \frac{p\alpha+q}{r\alpha+s} $$

の異なる $2$ 解である。【説明終わり】

</details>

求めた $\alpha$ を両辺から引く。$\alpha$ は $2$ つ求まるが、どちらを使ってもよい。

$$ a_{n+1} - \alpha = \frac{P(a_n-\alpha)}{ra_n+s} $$

となり、$b_n = a_n - \alpha$ とおくと[簡易分数型](#簡易分数型)になる。

### 隣接 3 項間型

$$ a_{n+2}+pa_{n+1}+qa_n=0 $$

まず、特性方程式 $\alpha^2+p\alpha+q=0$ を解き、$2$ 解 $s$, $t$ を求める。

<details markdown="1">
<summary>なぜ？</summary>

どうにかして等比型

$$ \underline{a_{n+2}-sa_{n+1}} = t(\underline{a_{n+1}-sa_n}) $$

となるように変形したい。この式を整理すると

$$ a_{n+2} - (s+t)a_{n+1} + sta_n = 0 $$

となる。元の式と係数を比較して、

$$ s+t=-p, \ \ \ \ \ st=q  $$

だから、解と係数の関係より、$s$, $t$ は $\alpha$ の $2$ 次方程式

$$ \alpha^2+p\alpha+q=0 $$

の $2$ 解であることがわかる。【説明終わり】

</details>

求めた $2$ 解 $s$, $t$ を、等比型の以下の式

$$ \underline{a_{n+2}-sa_{n+1}} = t(\underline{a_{n+1}-sa_n}) $$

に代入し、$\lbrace a_{n+1}-sa_n \rbrace$ の一般項を求めると

$$ a_{n+1}-sa_n = r^n $$

の[指数型](#指数型)になる。

<details markdown="1">
<summary>$s \neq t$ のときに使える別解</summary>

$$ \begin{align}
a_{n+2}-sa_{n+1} &= t(a_{n+1}-sa_n) \newline
a_{n+2}-ta_{n+1} &= s(a_{n+1}-ta_n)
\end{align} $$

から $\lbrace a_{n+1}-sa_n \rbrace$ と $\lbrace a_{n+1}-ta_n \rbrace$ の一般項をそれぞれ求めて、辺々を引いて $a_{n+1}$ を消去することもできる。

</details>

### 連立漸化式

$$\left\lbrace
\begin{align}
a_{n+1} = pa_n + qb_n \newline
b_{n+1} = ra_n + sb_n
\end{align}
\right.$$

係数が対称になっているなら連立して解く。対称でないなら[隣接 3 項間型](#隣接-3-項間型)に帰着させる。

まず、係数が対称になっているときを説明する。

$$\left\lbrace
\begin{align}
a_{n+1} = pa_n + qb_n \newline
b_{n+1} = qa_n + pb_n
\end{align}
\right.$$

$2$ 式の和と差はそれぞれ

$$\left\lbrace
\begin{align}
\underline{a_{n+1} + b_{n+1}} = (p+q)(\underline{a_n+b_n}) \newline
\underline{a_{n+1} - b_{n+1}} = (p-q)(\underline{a_n-b_n})
\end{align}
\right.$$

で、これはいずれも等比型なので、

$$\left\lbrace
\begin{align}
a_n+b_n = (a_1+b_1)\cdot(p+q)^{n-1} \newline
a_n-b_n = (a_1-b_1)\cdot(p-q)^{n-1}
\end{align}
\right.$$

と表せる。この $2$ 式の和と差をとると $a_n$, $b_n$ がそれぞれ求まる。

次に、係数が対称でないときを説明する。

$$\left\lbrace
\begin{align}
a_{n+1} = pa_n + qb_n \newline
b_{n+1} = ra_n + sb_n
\end{align}
\right.$$

$a_{n+1} = pa_n + qb_n$ より、$b_n = \dfrac{1}{q} (a_{n+1} - pa_n)$, $b_{n+1} = \dfrac{1}{q} (a_{n+2} - pa_{n+1})$ が成り立つ。$b_{n+1} = ra_n + sb_n$ に代入すると、[隣接 3 項間型](#隣接-3-項間型)になる。


[^1]: 数学では「ある式の特徴を示す数を求めるシンプルな方程式」のことを雑に「特性方程式」と呼ぶことが多い。根源は行列の固有多項式にある。