---
layout: default
# parent: tips
summary: ことばのつかいかた
---

# 一次独立

「一次独立」とはいいますが, 実際は英語の linear independence を訳したものなので, 線形独立のほうが正しいんじゃないかなって思います.

## 正確な定義

$n$ 本のベクトル $\vec{v_1}, \vec{v_2}, \dots, \vec{v_n}$ が**線形独立**である (linearly independent) とは, $c_1, c_2, \dots, c_n$ をスカラーとして,

$$ \sum_{i=1}^n c_i \vec{v_i} = 0 \ \ \Rightarrow \ \ c_1 = c_2 = \cdots =c_n = 0 $$

が成り立つことをいう. また, 線形独立でないことを線形従属という.

## 具体例

### 平面上のベクトル

普段はこんな感じで使います.

> $s \vec{a} + t \vec{b} = 0$ を満たす実数 $s, t$ の組が $s=t=0$ のみのとき, $\vec{a}$ と $\vec{b}$ は一次独立である.

そして**平面上のベクトルでは特に**

> $\vec{a} \neq \vec{0}$, $\vec{b} \neq \vec{0}$ で, $\vec{a}$ と $\vec{b}$ が平行でない
> $\Leftrightarrow$ $s \vec{a} + t \vec{b} = 0$ を満たす実数 $s, t$ の組が $s=t=0$ のみ

が成り立ちます. そこで, 記述答案に軽率に

> $\vec{a}$ と $\vec{b}$ は一次独立なので,

と書いても, 結果的にうまくいってしまいます.